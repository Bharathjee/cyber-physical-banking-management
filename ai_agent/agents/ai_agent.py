import os
import uuid
import time
from typing import Dict, List, Any, Generator
from dotenv import load_dotenv

import uuid
from .planner import Planner
from .tools import tools
from .memory import Memory

load_dotenv()

class AgentController:
    def __init__(self):
        self.planner = Planner()
        self.tools = tools
        self.memory = Memory()
        self.max_steps = 20
        self.step_delay = 1.0  # For demo streaming

    def execute_goal(self, goal: str, session_id: str = None) -> Generator[str, None, None]:
        if not session_id:
            session_id = str(uuid.uuid4())
        
        self.memory.new_session(goal)
        self.memory.add_message(int(session_id), 'user', goal)

        history = self.memory.get_history(int(session_id))
        
        for step in range(self.max_steps):
            yield f"Step {step + 1}: Planning...\n"
            time.sleep(self.step_delay)
            
            plan = self.planner.create_plan(goal, history)
            yield f"Plan: {plan['reasoning']}\nNext action: {plan['action']}\n"
            self.memory.add_message(int(session_id), 'assistant', plan['reasoning'])
            
            if plan['action'] == 'complete':
                yield "Goal completed!\n"
                break
            
            try:
                # Execute tool
                tool_result = self.tools.execute(plan['tool_call'])
                yield f"Tool result: {tool_result}\n"
                self.memory.add_message(int(session_id), 'tool', tool_result, plan['tool_call']['id'])
                history = self.memory.get_history(int(session_id))
            except Exception as e:
                error_msg = f"Tool failed: {str(e)}"
                yield error_msg + "\n"
                self.memory.add_message(int(session_id), 'tool', error_msg)
                # Replan on failure
        
        yield "Execution finished.\n"

    def chat(self, message: str, session_id: str) -> str:
        # Simple chat wrapper
        history = self.memory.get_history(int(session_id))
        response = self.planner.plan_response(message, history)
        self.memory.add_message(int(session_id), 'user', message)
        self.memory.add_message(int(session_id), 'assistant', response)
        return response

