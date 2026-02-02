import asyncio
from utils.latency import log

async def streaming_asr():
    """
    Simulates a streaming ASR system by yielding
    partial transcripts over time.
    """
    partial_transcripts = [
        "Why is my router overheating",
        "Why is my router overheating and what about",
        "Why is my router overheating and what about the second one"
    ]

    for text in partial_transcripts:
        await asyncio.sleep(0.12)  # simulate ASR delay
        log(f'ASR partial: "{text}"')
        yield text
