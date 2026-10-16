import os
from fastapi import Header, HTTPException

# Configure CHATBOT_API_KEY securely in the server environment.
def get_customer(x_api_key: str = Header(...)):
    configured_key = os.getenv("CHATBOT_API_KEY")
    if not configured_key or x_api_key != configured_key:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return "configured_customer"
