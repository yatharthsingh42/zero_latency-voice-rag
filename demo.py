import asyncio

from asr.mock_streaming_asr import streaming_asr
from rag.query_rewriter import rewrite_query
from rag.hybrid_search import hybrid_search
from rag.reranker import cross_encoder_rerank
from llm.filler_response import filler_speech
from llm.answer_generator import generate_final_answer
from voice.voice_optimizer import voice_optimize
from utils.latency import log

conversation_history = []

async def run_demo():
    """
    Orchestrates the full speculative, parallelized
    voice RAG pipeline.
    """
    prefetch_task = None
    rewritten_query = None

    
    async for partial_text in streaming_asr():
        rewritten_query = rewrite_query(partial_text, conversation_history)

        
        if prefetch_task is None:
            log("Prefetch RAG started")
            prefetch_task = asyncio.create_task(
                hybrid_search(rewritten_query)
            )

  
    documents = await prefetch_task


    filler_task = asyncio.create_task(filler_speech())
    rerank_task = asyncio.create_task(
        cross_encoder_rerank(rewritten_query, documents)
    )

    top_docs = await rerank_task

    final_answer = generate_final_answer(rewritten_query, top_docs)
    spoken_answer = voice_optimize(final_answer)

    log(f'Speaking final answer: "{spoken_answer}"')

if __name__ == "__main__":
    asyncio.run(run_demo())
