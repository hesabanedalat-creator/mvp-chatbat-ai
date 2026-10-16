import os
from typing import Optional
from ctransformers import AutoModelForCausalLM
import threading

class GGUFModel:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialize()
            return cls._instance
    
    def _initialize(self):
        model_path = os.path.join(os.path.dirname(__file__), "model.gguf")
        
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"فایل مدل یافت نشد: {model_path}")
        
        print(f"🔄 لود مدل GGUF از: {model_path}")
        
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            model_type="qwen",
            gpu_layers=0,
            context_length=2048,
            threads=4,
            batch_size=1
        )
        print("✅ مدل لود شد!")
    
    def generate(self, prompt: str, max_tokens: int = 100) -> str:
        try:
            # فرمت Qwen
            formatted_prompt = f"<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
            
            response = self.model(
                formatted_prompt,
                max_new_tokens=max_tokens,
                temperature=0.3,
                top_p=0.9,
                repetition_penalty=1.1,
                stop=["<|im_end|>", "\n\n", "user:", "User:"]
            )
            
            # پاک‌سازی پاسخ
            cleaned = response.strip()
            if "<|im_start|>" in cleaned:
                cleaned = cleaned.split("<|im_start|>")[0].strip()
            
            return cleaned if cleaned else "پاسخی دریافت نشد."
            
        except Exception as e:
            return f"خطا: {str(e)[:50]}"

# شی اصلی
qwen_model = GGUFModel()

def chat_gguf(message: str) -> str:
    return qwen_model.generate(message)