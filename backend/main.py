# main.py - نسخه نهایی
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from chat_qwen import chat_with_bot
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# سرو دادن فایل‌های استاتیک (ویجت)
app.mount("/static", StaticFiles(directory="../widget"), name="static")

class ChatRequest(BaseModel):
    message: str
    customer_id: str

@app.post("/chat")
async def chat(request: ChatRequest):
    response = chat_with_bot(request.customer_id, request.message)
    return {"answer": response}

@app.get("/")
async def root():
    return {"message": "چت بات API فعال است"}

if __name__ == "__main__":
    import uvicorn
    print("🚀 سرور و ویجت روی پورت 8000")
    print("📌 ویجت: http://localhost:8000/static/iframe.html")
    print("📌 API: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)