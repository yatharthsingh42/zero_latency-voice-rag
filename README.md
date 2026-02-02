Zero-Latency Voice Knowledge Base (RAG Prototype)

Overview

This project is a design-focused prototype of a low-latency, voice-first Retrieval Augmented Generation (RAG) system for a CCaaS platform.

The target scenario is a Voice AI agent that assists users with complex hardware troubleshooting by querying large technical manuals (1000+ pages) and responding via speech. The primary goal is to minimize user-perceived latency, specifically the Time to First Byte (TTFB) of audio, even when queries require multi-document retrieval and reranking.

Rather than attempting a full production deployment, this project focuses on architectural correctness, parallel execution, latency-aware design, and voice-optimized responses. Real-time audio components are simulated, while preserving realistic system behavior and timing characteristics.

Design Goals

The system is designed around the following principles:

Prioritize TTFB over total response time
In voice systems, when the user hears the first audio matters more than when the full answer completes.

Use parallelism to hide latency
Expensive operations such as retrieval and reranking should overlap with user speech or filler responses.

Treat voice as a first-class interface
Spoken output should sound natural and conversational, not like text being read aloud.

Make tradeoffs explicit
Scope is intentionally limited to highlight the core engineering challenges rather than infrastructure scale.

High-Level Architecture

Traditional voice pipelines follow a linear flow:

ASR

RAG

LLM

TTS

This design instead uses speculative and parallel execution:

Streaming ASR (partial transcripts)

Prefetch RAG

Context-aware query rewriting

Hybrid retrieval (vector + BM25)

Cross-encoder reranking

Early filler speech

Final voice-optimized answer

The key idea is that no component waits unless it absolutely must.

Chosen Approach

This implementation intentionally prioritizes system behavior and latency characteristics over full production integration.

Real-time ASR and TTS are mocked, while retrieval, reranking, and orchestration logic are implemented at a small scale. Latency is explicitly measured and logged, even when delays are simulated, to demonstrate how parallel execution reduces user-perceived delay.

This approach mirrors how such a system would behave in production while remaining feasible within intern-level constraints.

Core Components
1. Streaming ASR (Simulated)

Instead of waiting for a full transcription, the ASR produces partial transcripts incrementally.

Example partial outputs:

"Why is my router overheating"

"Why is my router overheating and what about"

"Why is my router overheating and what about the second one"

Each partial transcript can immediately trigger downstream work.

2. Speculative and Parallelized RAG

As soon as a meaningful partial transcript is produced, the system begins retrieval prefetching. Retrieval does not wait for the final user query and is updated if the query changes.

This hides retrieval latency behind the user’s speech.

3. Context-Aware Query Rewriting

Short or referential queries such as “the second one” are rewritten using conversation history before hitting the retrieval layer.

Example rewrite:
"What causes overheating in the secondary router module?"

This prevents retrieval failures and improves recall for conversational queries.

4. Hybrid Search (Vector + BM25)

Technical manuals contain both semantic explanations and exact identifiers such as model numbers or error codes.

The system uses:

Vector search for semantic relevance

BM25 keyword search for exact matches

Results from both methods are merged before reranking.

5. Cross-Encoder Reranking with Latency Masking

Cross-encoder rerankers improve accuracy but introduce additional latency.

To prevent this from delaying audio output, reranking runs asynchronously while the system begins speaking a short filler response such as:

"Let me check the technical manual for that."

Once reranking completes, the system transitions to the final answer.

6. Voice-Optimized Response Layer

Raw LLM outputs are often verbose and unsuitable for speech.

Before synthesis, responses are rewritten to:

use shorter sentences

simplify vocabulary

introduce natural pauses

apply phonetic spelling for technical terms when needed

Example:

Before:
"The thermal dissipation mechanism relies on a dual-phase heat sink assembly."

After:
"Your router is overheating because heat is not escaping properly. There is a metal heat sink inside, and it is not cooling the processor enough."

This improves listening comfort and reduces synthesis time.

Latency Awareness

Although some delays are simulated, the system explicitly logs timing to demonstrate overlap between components.

Approximate timing breakdown:

ASR partial transcript: ~150 ms

Prefetch retrieval: ~200 ms

Hybrid search: ~120 ms

Reranking: ~300 ms

Filler speech: overlaps with reranking

Time to First Audio Byte: ~500–600 ms

The emphasis is on overlapping work rather than optimizing individual components in isolation.

What Is Intentionally Out of Scope

To keep the focus on architectural and latency challenges, this prototype does not include:

real microphone capture

real streaming TTS

GPU inference

large-scale vector databases

production deployment infrastructure

These components are orthogonal to the core design goals of this exercise.


To run the demo:

python demo.py


The demo prints:

partial ASR output

when retrieval begins

when filler speech starts

when the final answer is produced

This makes the system’s timing behavior easy to observe

Key Takeaways

User-perceived latency is critical in voice systems

Parallel execution hides expensive operations

Voice interfaces require different output strategies than text interfaces

Sound architectural decisions often matter more than faster models

Future Improvements

With additional time and infrastructure, this system could be extended to support:

true streaming ASR and TTS

incremental embeddings during speech

GPU-accelerated reranking

user interruption handling (barge-in)

adaptive prosody based on confidence

