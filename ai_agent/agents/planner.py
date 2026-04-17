import os
import openai
from typing import Dict, List, Any
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

class Planner:
    def __init__(self):
        self.model = 'gpt-4o-mini'  # Cost-effective, capable

    def create_plan(self, goal: str, history: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        LLM plans next step/tool based on goal + history.
        Returns: {'reasoning': str, 'action': 'complete|tool', 'tool_call': dict}
        """
        history_str = '\n'.join([f"{h['role']}: {h['content']}" for h in history[-10:]])  # Last 10
        
        system_prompt = """
        You are an AI agent planner for banking tasks. Analyze goal + history, output JSON:
        {
          "reasoning": "Your step-by-step thinking",
          "action": "complete" (if done) or "tool",
          "tool_call": {"name": "tool_name", "args": {...}, "id": "uuid"} (if tool)
        }
        Available tools: get_balance(cust_id), deposit(cust_id, amount), withdraw(cust_id, amount), 
        list_customers(), search_customers(query), calculator(expr)
        """
        
        messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': f"Goal: {goal}\nHistory:\n{history_str}"}
        ]
        
        response = client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.1
        )
        
        plan_str = response.choices[0].message.content
        # Parse JSON (simple, add error handling in prod)
        import json
        import uuid
        try:
            plan = json.loads(plan_str)
        except:
            plan = {'reasoning': plan_str, 'action': 'complete'}
        
        if plan.get('action') == 'tool' and plan.get('tool_call'):
            plan['tool_call']['id'] = plan['tool_call'].get('id', str(uuid.uuid4()))
        
        return plan

    def plan_response(self, message: str, history: List[Dict[str, Any]]) -> str:
        history_str = '\n'.join([f"{h['role']}: {h['content']}" for h in history[-10:]])
        messages = [
            {'role': 'system', 'content': 'You are a helpful banking AI assistant.'},
            {'role': 'user', 'content': f"{history_str}\nUser: {message}"}
        ]
        response = client.chat.completions.create(model=self.model, messages=messages)
        return response.choices[0].message.content

