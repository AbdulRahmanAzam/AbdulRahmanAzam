#!/usr/bin/env python3
"""
Picks a random AI / agentic-web quote and replaces the content between
<!-- QUOTE_START --> and <!-- QUOTE_END --> markers in README.md.
"""

import random
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Curated AI · Agents · MCP quote bank
# ---------------------------------------------------------------------------
QUOTES: list[tuple[str, str | None]] = [
    # Original / community
    ("The future belongs to those who can orchestrate intelligence — not just consume it.", None),
    ("An agent that cannot explain its actions is not trustworthy. Transparency is not optional; it's architectural.", None),
    ("MCP is to AI agents what HTTP is to the web — a universal protocol for tool-augmented intelligence.", None),
    ("Multi-agent systems are the new microservices: composable, specialised, and collectively unstoppable.", None),
    ("Context engineering is the real skill in the age of LLMs — garbage in, garbage out; enlightenment in, excellence out.", None),
    ("RAG isn't a technique, it's a philosophy — always ground your AI in verifiable truth.", None),
    ("The agentic web is unfolding. Build your place in it before someone else's agent does.", None),
    ("LLMs are the runtime; AI agents are the application layer; humans are the product managers.", None),
    ("Autonomy without accountability is chaos. The best agents know exactly when to ask a human.", None),
    ("We're not building smarter tools — we're building smarter workflows that amplify human intent.", None),
    ("AI is not about replacing human thinking. It's about delegating the predictable so humans can own the creative.", None),
    ("A well-engineered system prompt is worth more than a thousand fine-tuning steps.", None),
    ("The best AI product is one where the AI almost disappears — leaving only a seamless experience.", None),
    ("Tool-calling LLMs are the dawn of intent-driven computing. Prompts are the new programs.", None),
    ("The goal is not to automate jobs — it's to automate everything boring so you can focus on what's brilliant.", None),
    ("Ship slow agents, lose the market. Ship fast agents with no guardrails, lose the trust. Find the balance.", None),
    ("Every great agentic system starts with a tiny, well-scoped tool call.", None),
    ("The measure of an AI agent isn't its token count — it's the real-world task it actually completes.", None),
    # Attributed
    ("Artificial intelligence is the new electricity.", "Andrew Ng"),
    ("The question is not whether intelligent machines can have emotions, but whether machines without emotions can be truly intelligent.", "Marvin Minsky"),
    ("Every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it.", "John McCarthy"),
    ("By far the greatest danger of Artificial Intelligence is that people conclude too early that they understand it.", "Eliezer Yudkowsky"),
    ("Intelligence is the ability to adapt to change.", "Stephen Hawking"),
    ("Machines take me by surprise with great frequency.", "Alan Turing"),
    ("The real question is not whether machines think but whether men do.", "B.F. Skinner"),
    ("It's not that we use technology, we live technology.", "Godfrey Reggio"),
]


def format_quote(text: str, author: str | None) -> str:
    if author:
        return f'> *"{text}"* — **{author}**'
    return f'> *"{text}"*'


def update_readme(quote_block: str, readme_path: Path = Path("README.md")) -> None:
    content = readme_path.read_text(encoding="utf-8")
    pattern = r"(<!-- QUOTE_START -->).*?(<!-- QUOTE_END -->)"
    replacement = f"<!-- QUOTE_START -->\n{quote_block}\n<!-- QUOTE_END -->"
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    if new_content == content:
        raise RuntimeError("QUOTE markers not found in README.md — check that <!-- QUOTE_START --> and <!-- QUOTE_END --> exist.")
    readme_path.write_text(new_content, encoding="utf-8")


if __name__ == "__main__":
    text, author = random.choice(QUOTES)
    block = format_quote(text, author)
    update_readme(block)
    print(f"✅ Updated quote:\n{block}")
