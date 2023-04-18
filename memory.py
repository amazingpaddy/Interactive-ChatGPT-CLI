from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationEntityMemory
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain.chat_models import ChatOpenAI

from chat_gpt import ChatGPT
from config import OPENAI_API_KEY, CHAT_SETTINGS


class MemoryManager:
    """
    MemoryManager is a class that manages memory-related functionalities for the chat application.
    It initializes and manages ConversationEntityMemory and ConversationChain objects.
    """

    def __init__(self, chat_gpt: ChatGPT, is_stream: bool = False):
        """
        Initializes a new MemoryManager instance.

        :param chat_gpt: ChatGPT object to be used for language generation.
        :param is_stream: If True, use streaming mode (currently not implemented).
        """
        self.llm = None
        self.entity_memory = None
        self.conversation_chain = None
        self.chat_gpt = chat_gpt
        self.init_memory(is_stream)

    def init_memory(self, is_stream: bool):
        """
        Initializes memory-related components.

        :param is_stream: If True, use streaming mode (currently not implemented).
        """
        if is_stream:
            pass
        else:
            # Initialize the ChatOpenAI instance for language generation.
            self.llm = ChatOpenAI(temperature=CHAT_SETTINGS['temperature'],
                                  openai_api_key=OPENAI_API_KEY,
                                  model_name=self.chat_gpt.model_name,
                                  max_tokens=CHAT_SETTINGS['max_tokens'],
                                  verbose=True)
        # Initialize the ConversationEntityMemory instance for storing entity information.
        self.entity_memory = ConversationEntityMemory(llm=self.llm, k=1000)

        # Initialize the ConversationChain instance for managing the conversation process.
        self.conversation_chain = ConversationChain(llm=self.llm,
                                                    prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
                                                    memory=self.entity_memory)
