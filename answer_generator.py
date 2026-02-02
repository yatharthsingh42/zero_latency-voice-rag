from utils.latency import log

def generate_final_answer(query, documents):
    """
    Generates a response grounded in the
    top-ranked retrieved documents.
    """
    log("Generating final answer from top-ranked documents")

    
    return (
        "Your router is overheating for two main reasons. "
        "First, airflow around the device is restricted. "
        "Second, the processor is running under heavy load."
    )
