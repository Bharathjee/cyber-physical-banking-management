import os
import re
from typing import Dict, Any
from ...data import CUSTOMERS, CUSTOMER_USERS

class BankingTools:
    def __init__(self):
        pass

    def execute(self, tool_call: Dict[str, Any]) -> str:
        name = tool_call['name']
        args = tool_call['args']
        
        if name == 'get_balance':
            cust_id = args['cust_id']
            customer = CUSTOMERS.get(cust_id)
            if customer:
                return f"Balance for {cust_id} ({customer.name}): ${customer.balance:.2f}"
            return f"Customer {cust_id} not found"
        
        elif name == 'deposit':
            cust_id = args['cust_id']
            amount = float(args['amount'])
            customer = CUSTOMERS.get(cust_id)
            if customer:
                old_balance = customer.balance
                customer.deposit(amount)
                return f"Deposited ${amount:.2f} to {cust_id}. Balance: ${customer.balance:.2f} (was ${old_balance:.2f})"
            return f"Customer {cust_id} not found"
        
        elif name == 'withdraw':
            cust_id = args['cust_id']
            amount = float(args['amount'])
            customer = CUSTOMERS.get(cust_id)
            if customer and customer.withdraw(amount):
                old_balance = customer.balance + amount
                return f"Withdrew ${amount:.2f} from {cust_id}. Balance: ${customer.balance:.2f} (was ${old_balance:.2f})"
            return "Withdraw failed: insufficient funds or customer not found"
        
        elif name == 'list_customers':
            if CUSTOMERS:
                return '\\n'.join([f"{cid}: {cust.name} (${cust.balance:.2f})" for cid, cust in CUSTOMERS.items()])
            return "No customers"
        
        elif name == 'search_customers':
            query = args['query'].lower()
            results = [f"{cid}: {cust.name} (${cust.balance:.2f})" 
                      for cid, cust in CUSTOMERS.items() if query in cust.name.lower() or query in cid.lower()]
            return '\\n'.join(results) if results else "No matches"
        
        elif name == 'calculator':
            expr = args['expr']
            try:
                result = eval(expr)  # Safe in sandbox; use sympy in prod
                return f"{expr} = {result}"
            except:
                return "Calc error"
        
        else:
            raise ValueError(f"Unknown tool: {name}")

# Global tool executor instance
tools = BankingTools()

