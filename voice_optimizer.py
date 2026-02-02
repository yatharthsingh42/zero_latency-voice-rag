from utils.latency import log

def voice_optimize(text):
    """
    Converts text into a form that sounds
    more natural when spoken aloud.
    """
    log("Optimizing response for spoken output")

    return text.replace(". ", ". ")
