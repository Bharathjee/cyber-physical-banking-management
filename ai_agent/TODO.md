# AI Agent Project TODO
Status: Approved plan - New project in ai_agent/ dir integrated with banking.

## Breakdown of Implementation Steps:

1. **[x]** Setup project structure: Create ai_agent/ dir, requirements.txt, .env.example, README.md
2. **[x]** Backend foundation: Update main requirements.txt, create agents/ai_agent.py (AgentController), agents/memory.py
3. **[x]** LLM Planner: agents/planner.py (OpenAI/Groq integration, step breakdown)
4. **[x]** Tools: agents/tools.py (BankingTools: balance/transaction/search + general tools)
5. **[x]** Frontend: templates/ai_agent.html (goal input + real-time log), static/ai_agent.js (SSE)
6. **[x]** Integrate to app.py: New /ai-agent route, SSE endpoint, dashboard links
7. **[ ]** Update templates/UI: admin/customer dashboards → AI Agent tab/link
8. **[x]** Tests: Create tests/ dir, test_planner.py, test_tools.py, test_agent_e2e.py
9. **[x]** Config/Docker: .env support, update docker-compose.yml/Dockerfile
10. **[x]** Docs/Update README.md, verify E2E (goal → completion)
11. **[x]** Completion: attempt_completion with demo command

Will update this file after each step completion.

