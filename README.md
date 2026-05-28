# LangChain Learning: AI Private Chef

A full-stack AI application that acts as your personal chef, utilizing LangChain agents, multimodal recognition, and web search to provide tailored recipe recommendations.

## Features

- 📸 **Ingredient Recognition**: Upload photos of food to automatically identify available ingredients.
- 🔍 **Smart Recipe Search**: Integrates Tavily to find recipes based on your current ingredients.
- 💬 **Interactive Chat**: Streamlined conversation with an AI chef agent.
- 💾 **Persistent Memory**: Maintains conversation history across sessions using SQLite.
- 🚀 **Modern Stack**: Built with FastAPI, LangChain, and Uvicorn.

## 🚀 Getting Started

### 1. Install Dependencies

Using `uv`:

```bash
uv sync
```

### 2. Configure Environment

Copy the example configuration and fill in your API keys:

```bash
cp .env.example .env
```

Update `.env` with your actual keys (SiliconFlow API Key, Tavily API Key, etc.).

### 3. Run the Application

Start the FastAPI server:

```bash
uv run python app/main.py
```

Or using Uvicorn directly:

```bash
uv run uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8001` to access the frontend.

## 📂 Project Structure

```text
langchain-learning/
├── app/
│   ├── agents/          # AI Agent logic (Multimodal model & Search)
│   ├── api/             # FastAPI routes
│   ├── common/          # Shared utilities (Logging)
│   ├── static/          # Frontend files
│   ── main.py          # Application entry point
── db/                  # SQLite database files
├── study/               # Learning scripts & experiments
└── pyproject.toml       # Project dependencies
```

## 🛠 Tech Stack

- **Python 3.13+**
- **LangChain & LangGraph**: Agent orchestration
- **FastAPI**: Web framework
- **Tavily**: Web search integration
- **SiliconFlow**: LLM provider
- **SQLite**: Local memory storage

