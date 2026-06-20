# ⚡ Socratic Debate Coach

A domain-specific AI chatbot that challenges your arguments using the Socratic method. Built with Python and powered by LLaMA 3 running locally via Ollama.

## What It Does
- Takes any opinion or argument from the user
- Always argues the **opposing side** using probing questions
- Exposes logical gaps and assumptions in your reasoning
- Rejects off-topic questions and redirects back to debate
- Remembers full conversation context across multiple turns

## Tech Stack
- Python 3
- [Ollama](https://ollama.com) — runs LLaMA 3 locally
- `ollama` Python library

## Installation

1. Install [Ollama](https://ollama.com) and pull the model:
ollama run llama3
2. Install the Python dependency:
pip install ollama
3. Run the chatbot:
python chatbot.py

## Example Interaction
You: Social media is ruining society

Coach: Can you define what you mean by "ruining society"? What specific aspects are being negatively impacted?


You: What is 5+5?

Coach: I'm here to challenge your arguments. Present a claim.

## How It Works
| Concept | Implementation |
|---|---|
| System Prompt | Defines the coach's role and domain restrictions |
| Context Memory | Full conversation history sent with every message |
| Domain Restriction | Off-topic queries redirected via system prompt rules |
