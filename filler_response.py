from utils.latency import log

async def filler_speech():
    """
    Short filler speech used to reduce
    perceived latency while heavy work runs.
    """
    log('Speaking: "Let me check the technical manual for that..."')
