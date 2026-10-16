# ذخیره موقت محتوا در حافظه
INGESTED_CONTENT = {}

def ingest_content(customer_id: str, text: str):
    INGESTED_CONTENT[customer_id] = text

def get_content(customer_id: str) -> str:
    return INGESTED_CONTENT.get(customer_id, "")
