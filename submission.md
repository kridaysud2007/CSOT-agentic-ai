# GenAI-Agentic: Project Submission

## Project Overview

A terminal-based conversational AI chat agent built in Python. The app lets you pick from multiple free LLMs (via OpenRouter) and chat with them in a multi-turn conversation, with a sliding memory window to manage context length.

---

## What I Built

- A `ChatAgent` class that manages conversation state, system prompts, and API calls
- A model selection menu at startup, letting the user choose between Google Gemma 4, OpenAI GPT OSS, and NVIDIA Nemotron 3
- A sliding window memory system that keeps the last N turns in context, preventing token overflow
- Secure API key management using a `.env` file (never hardcoded)

---

## What I Learned

### 1. Working with LLM APIs
- How to call an LLM API using the OpenAI SDK pointed at a custom `base_url` (OpenRouter), making it easy to swap between different model providers
- How the chat completions format works — structuring `messages` as a list of `role`/`content` pairs (`system`, `user`, `assistant`)
- How a system prompt shapes model behaviour from the very first message

### 2. Object-Oriented Design for AI Agents
- How to encapsulate agent state (conversation history, model choice, max turns) inside a class
- Why this matters: it makes agents reusable and composable — you could spin up multiple `ChatAgent` instances with different personalities or models

### 3. Conversation Memory Management
- LLMs are stateless — every API call needs the full history sent along with it
- Implemented a **sliding window**: once the conversation exceeds `max_turns`, the oldest user+assistant turn is dropped (`messages.pop(1)` twice), keeping the system prompt intact
- This keeps token usage bounded without losing the most recent context

### 4. Environment Variables & Secret Management
- Used `python-dotenv` to load a `.env` file at runtime with `load_dotenv()`
- Accessed the key securely via `os.environ["OPENROUTER_API_KEY"]` instead of hardcoding it
- Learned the `.env` / `.env.example` pattern: commit the example with placeholder values, never commit the real secrets
- Added `.env` to `.gitignore` to prevent accidental exposure on GitHub

### 5. Git & GitHub Workflow
- Initialised a Git repository and made an initial commit
- Understood what goes into `.gitignore` and why
- Pushed a project to GitHub including a `.env.example` as documentation for future collaborators

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| OpenAI SDK | API client (pointed at OpenRouter) |
| OpenRouter | Free LLM gateway (Gemma, GPT OSS, Nemotron) |
| python-dotenv | Environment variable management |
| Git + GitHub | Version control and code hosting |

---

## Key Takeaway

This project connected the dots between **how LLMs actually work** (stateless, message-list based), **how to build around that** (maintaining history in your own code), and **professional engineering practices** (secrets management, version control). It's a foundation I can extend into more complex agentic systems.
