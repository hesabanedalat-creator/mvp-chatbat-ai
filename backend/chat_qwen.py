# D:\ai-website-chatbot\backend\chat_qwen.py
from llama_cpp import Llama
import os

MODEL_PATH = r"D:\ai-website-chatbot\backend\AI\qwen2.5-3b-instruct-q4_k_m.gguf"

# لود مدل
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=1024,
    n_threads=4,
    n_batch=512,
    verbose=False
)

print("✅ مدل GGUF لود شد!")

def chat_with_bot(customer_id: str, message: str) -> str:
    """تابع اصلی چت"""
    try:
        prompt = f"<|im_start|>user\n{message}<|im_end|>\n<|im_start|>assistant\n"
        
        output = llm(
            prompt,
            max_tokens=60,
            temperature=0.3,
            stop=["<|im_end|>", "\n\n"],
            echo=False
        )
        
        response = output["choices"][0]["text"].strip()
        return response if response else "پاسخ دریافت شد"
        
    except Exception as e:
        return f"خطا: {str(e)[:50]}"