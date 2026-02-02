import asyncio
from utils.latency import log

async def hybrid_search(query):
    """
    Simulates hybrid retrieval using both
    semantic (vector) and keyword (BM25) search.
    """
    log("Hybrid search started (vector + BM25)")
    await asyncio.sleep(0.12)  

    return ["doc_router_overheating", "doc_airflow", "doc_cpu_load"]
