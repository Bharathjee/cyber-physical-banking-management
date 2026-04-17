# AI Agent for Cyber Physical Banking 🚀

Goal-driven AI Agent with planning, tools, memory. Integrated with banking MVP.

## Features
- **Goal-based UI**: Input natural goal → watch agent plan/execute
- **Planner (LLM)**: Breaks goals into steps with reasoning
- **Tools**: Banking ops (balance/transaction), search, calc
- **Memory**: Short/long-term task history
- **Real-time**: SSE streaming of steps/tools/progress
- **Tests**: Planner/tools/E2E

## Quick Start
```bash
cd ai_agent
pip install -r requirements.txt
cp .env.example .env  # Add your API key
cd ..
python app.py
```
Visit http://localhost:5000/ai-agent

## Architecture
```
Frontend (goal) → AgentController → Planner(LLM) → ToolExecutor → Memory → Result
```

## Demo Goals
- \"Check balance for cust001\"
- \"Deposit $100 to cust001 if balance < 500\"
- \"Find customers with balance > 1000\"

## Tech
- Backend: Flask + OpenAI
- Frontend: Vanilla JS + SSE
- Tests: pytest

MIT License.

