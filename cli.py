import argparse
import asyncio

from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import InMemoryHistory

from chat_gpt import ChatGPT
from config import CHAT_SETTINGS
from config import OPENAI_API_KEY
from memory import MemoryManager


def create_session() -> PromptSession:
    """
    Creates a new PromptSession with in-memory history.

    :return: A new instance of PromptSession.
    """
    return PromptSession(history=InMemoryHistory())


async def get_input_async(
        session: PromptSession = None,
        completer: WordCompleter = None,
) -> str:
    """
    Asynchronously gets user input using the given PromptSession.

    :param session: A PromptSession instance for user input.
    :param completer: A WordCompleter for tab completion, if desired.
    :return: The user's input as a string.
    """
    return await session.prompt_async(
        completer=completer,
        multiline=True,
        auto_suggest=AutoSuggestFromHistory(),
    )


async def main(args):
    """
    The main asynchronous function that initializes the ChatGPT instance, handles command line arguments,
    and manages the interactive loop for user input and GPT responses.

    :param args: The command line arguments passed to the script.
    """
    model_str = "GPT4"
    chat_gpt = ChatGPT(api_key=OPENAI_API_KEY, model_name="gpt-4")
    if args.gpt3:
        model_str = "GPT3.5"
        chat_gpt = ChatGPT(api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo")
        # gpt3.5 supports fewer tokens than gpt-4
        CHAT_SETTINGS["max_tokens"] = 3000
    memory_manager = None

    if args.memory or args.memory_stream:
        memory_manager = (MemoryManager(chat_gpt=chat_gpt) if args.memory
                          else MemoryManager(chat_gpt=chat_gpt, is_stream=True))

    session = create_session()

    while True:
        print("\nYou:")
        question = await get_input_async(session=session)
        print()
        print()

        if question == "!exit":
            break
        elif question == "!help":
            print(
                """
            !help - Show this help message
            !exit - Exit the program
            """,
            )
            continue

        print(f"{model_str}:")

        if args.no_stream:
            chat_gpt.console.print(await chat_gpt.ask(prompt=question),
                                   end='', markup=True, highlight=True, emoji=True)
        elif args.memory:
            chat_gpt.console.print(await chat_gpt.ask_mem(question, memory_manager.conversation_chain),
                                   end='', markup=True, highlight=True, emoji=True)
        elif args.memory_stream:
            pass
        else:
            await chat_gpt.ask_stream(prompt=question)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpt3", action="store_true")
    parser.add_argument("--no-stream", action="store_true")
    parser.add_argument("--memory", action="store_true")
    parser.add_argument("--memory-stream", action="store_true")
    args = parser.parse_args()
    asyncio.run(main(args))
