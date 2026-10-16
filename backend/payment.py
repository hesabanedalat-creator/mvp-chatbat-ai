# payment.py
class PaymentSystem:
    def create_invoice(self, customer_id: str, amount: int, currency: str = "IRT"):
        """ساخت فاکتور برای ایران (تومان)"""
        if currency == "IRT":
            return f"https://zarinp.al/{amount}?customer={customer_id}"
        elif currency == "CNY":
            return f"https://wechat.pay/{amount}?customer={customer_id}"