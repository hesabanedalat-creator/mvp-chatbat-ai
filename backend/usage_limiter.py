# usage_limiter.py
from datetime import datetime, timedelta

class UsageLimiter:
    def __init__(self):
        self.usage = {}  # {customer_id: {"messages": 0, "reset_date": ...}}
    
    def check_limit(self, customer_id: str) -> bool:
        """بررسی محدودیت ماهیانه"""
        if customer_id not in self.usage:
            self.usage[customer_id] = {
                "messages": 0,
                "reset_date": datetime.now() + timedelta(days=30)
            }
        
        usage_data = self.usage[customer_id]
        
        # ریست ماهیانه
        if datetime.now() > usage_data["reset_date"]:
            usage_data["messages"] = 0
            usage_data["reset_date"] = datetime.now() + timedelta(days=30)
        
        # محدودیت 1000 پیام در ماه
        if usage_data["messages"] >= 1000:
            return False
        
        usage_data["messages"] += 1
        return True