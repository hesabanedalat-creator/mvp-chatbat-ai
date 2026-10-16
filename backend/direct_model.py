# D:\ai-website-chatbot\backend\direct_model.py
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import threading
import queue

class QwenDirect:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.loaded = False
        self.queue = queue.Queue()
        
    def load_model(self):
        """لود مدل در پس‌زمینه"""
        try:
            print("📥 در حال لود مدل Qwen...")
            model_name = "Qwen/Qwen2.5-0.5B-Instruct"  # نسخه سبک‌تر
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float16,
                device_map="cpu",  # روی CPU اجرا شود
                low_cpu_mem_usage=True
            )
            self.loaded = True
            print("✅ مدل لود شد!")
        except Exception as e:
            print(f"❌ خطا در لود مدل: {e}")
    
    def chat(self, message: str, max_length: int = 50) -> str:
        """چت مستقیم"""
        if not self.loaded:
            return "مدل در حال لود شدن است..."
        
        try:
            inputs = self.tokenizer(
                f"پاسخ کوتاه بده: {message[:100]}",
                return_tensors="pt",
                truncation=True,
                max_length=50
            )
            
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=max_length,
                    temperature=0.7,
                    do_sample=True
                )
            
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            # حذف پرسش از پاسخ
            if "پاسخ کوتاه بده:" in response:
                response = response.split("پاسخ کوتاه بده:")[1].strip()
            
            return response[:150]
            
        except Exception as e:
            return f"خطا در پردازش: {str(e)[:50]}"

# راه‌اندازی
qwen = QwenDirect()

# لود در تابع جداگانه
def start_loading():
    qwen.load_model()

threading.Thread(target=start_loading, daemon=True).start()

# تابع اصلی چت
def chat_with_bot(customer_id: str, message: str) -> str:
    if not qwen.loaded:
        return "🔄 چت بات در حال راه‌اندازی..."
    return qwen.chat(message)