# run_server.py
from fastapi import FastAPI
from pydantic import BaseModel
from chat_qwen import chat_with_bot
import uvicorn

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    customer_id: str

@app.post("/chat")
async def chat(request: ChatRequest):
    response = chat_with_bot(request.customer_id, request.message)
    return {"answer": response}

@app.get("/")
async def root():
    return {"status": "Chatbot API is running"}

if __name__ == "__main__":
    print("🚀 سرور چت بات در حال راه‌اندازی...")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")