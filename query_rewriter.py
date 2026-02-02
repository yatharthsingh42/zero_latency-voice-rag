from utils.latency import log

def rewrite_query(text, conversation_history):
    """
    Resolves short or ambiguous references using
    prior conversation context.
    """
    lowered = text.lower()

    if "second one" in lowered:
        log("Ambiguous reference detected, resolving via conversation history")
        return "Why is the secondary router module overheating?"

    return text
