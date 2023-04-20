# Interactive-ChatGPT-CLI

An interactive command-line interface for chatting with OpenAI's GPT models, including GPT-4 and GPT-3.5-turbo. Supports
various modes with memory for follow-up questions and streaming live responses.

## Prerequisites

- Python 3.11 is recommended.
- You need an OpenAI API key. Obtain one from the [OpenAI website](https://platform.openai.com/account/api-keys).

## Installation

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Configuration

Add your OpenAI API key in the environment variables, or modify `config.py` and edit `OPENAI_API_KEY` to replace it with
your API key instead of getting it from the environment.
Usage

To run the application with GPT-4, you can use various modes:

### Memory mode - (supports follow-up questions but uses more tokens and is slightly slower than non-memory mode.)

With memory and live Streaming response.

```bash
python cli.py --memory-stream
```

With memory:

```bash
python cli.py --memory
```
**To send a message, press "Esc + Return" while using the chatbot.**
**To reset the memory**
Inside the session, type ```!reset-memory``` and press **"Esc + Return"**

### Non Memory Mode - Doesnt support follow up questions. Best fit for single request and response.
### Non memory mode - Streaming response 

```bash
python cli.py
```

### Non-memory mode without streaming or live response

```bash
python cli.py --no-stream
```
To use the GPT-3.5-turbo model, pass the extra argument `--gpt3`:

```bash
python cli.py --memory-stream --gpt3
python cli.py --memory --gpt3
python cli.py --gpt3
python cli.py --no-stream --gpt3
```

To exit the session:
type ```!exit``` and press **"Esc + Return"**

## Known Issues
1. Chat typing animation for non-live response mode is not displaying the time properly.

