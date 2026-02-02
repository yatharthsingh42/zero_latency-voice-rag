import asyncio
from utils.latency import log

async def cross_encoder_rerank(query, documents):
    """
    Simulates a slower but more accurate
    cross-encoder reranking step.
    """
    log("Cross-encoder reranking started")
    await asyncio.sleep(0.30)  
    log("Cross-encoder reranking finished")
  
    return documents[:1]
