# Basic local model app

Browser (HTML + JavaScript) → FastAPI → Ollama → FastAPI → Browser

Each submission is independent. There is no conversation history or database.
FastAPI serves the page and API together, so only one app server is needed.

## Run

1. Install Ollama from https://ollama.com/download and start the Ollama app.
2. Download the model in a terminal:

   ```sh
   ollama pull llama3.2:1b
   ```

3. Open a terminal in this folder and run:

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

4. Open http://127.0.0.1:8000 in your browser. Enter a prompt and click Send prompt.

If using Ollama's CLI without its desktop app, run `ollama serve` in another terminal first. If Ollama is already running, no extra server is needed.

To use another downloaded model, change `MODEL_NAME` in `.env` to its name and restart the backend.

## How the code works

- `index.html`: sends `{ "prompt": "..." }` to `POST /api/prompt` using fetch.
- `api/routes.py`: receives the prompt as a `ChatRequest` and calls `llm/ollama.py`.
- `llm/ollama.py`: calls Ollama with `stream: false` to wait for the complete response.
- FastAPI returns `{ "response": "...", "sources": [] }`; JavaScript displays that text.

The model runs through Ollama; FastAPI handles HTTP requests. No API key is needed for the local Ollama server. The first model download requires internet access.

## Learning notes

The code intentionally contains just the basic successful request flow, with comments explaining each step. There is no custom error handling. Ollama must be running and the model must be downloaded before you send a prompt.

Read `index.html` starting at `sendPrompt()`, then `api/routes.py` starting at `generate()`, then `llm/ollama.py`, then return to `index.html` to see how the answer is displayed. Each click sends a new, independent prompt.

## Folder structure

```text
local-prompt-app/
├── main.py             # Creates FastAPI and includes the router
├── config.py           # Settings class and .env loading
├── .env                # Local setting values
├── .env.example        # Example settings to copy if .env is missing
├── index.html          # Frontend
├── requirements.txt
├── api/
│   ├── __init__.py
│   ├── models.py       # ChatRequest, ChatResponse, Source
│   └── routes.py       # Page and prompt endpoints
├── llm/
│   ├── __init__.py
│   └── ollama.py       # HTTP call to Ollama
├── rag/
│   └── __init__.py     # Empty for now
└── scripts/
    ├── __init__.py
    └── README.md       # Future helper scripts
```

`__init__.py` marks a folder as a Python package; these files can be empty.

## Settings and response models

Install the updated dependencies in your existing virtual environment:

```sh
pip install -r requirements.txt
```

`.env` is included locally. If it is missing, copy `.env.example` to `.env`.
`Settings` reads `OLLAMA_URL`, `MODEL_NAME`, and `DB_URL` from that file.
Matching environment variables override values from `.env`. Restart the backend after editing settings.
`DB_URL` is only a placeholder; there is no database connection yet.

`ChatRequest` describes the incoming prompt. `ChatResponse` describes the outgoing
answer and its sources. `Source` currently has `title` and `content` fields for
future RAG work. The endpoint always returns an empty sources list for now:

```json
{"response": "The model's answer", "sources": []}
```

The frontend still displays `data.response`, so it needs no changes.
You can inspect these models interactively at http://127.0.0.1:8000/docs.
