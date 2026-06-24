#!/usr/bin/env python3
"""
Call local Ollama HTTP API to generate follow-up questions using model ollama/llama3.2:3b.
Requires Ollama server running at http://localhost:11434.
"""
import json
import sys
from urllib.request import Request, urlopen

MODEL = "ollama/llama3.2:3b"
URL = "http://localhost:11434/api/generate"

transcript = """
I arrived in London from Jamaica in 1963 when I was 21 years old.
I first worked on London Transport and later became a bus driver.
Housing was difficult to find and many landlords refused to rent to Black people.
My church community became an important source of support.
I eventually bought a home, raised three children and remained active in community organisations.
"""

prompt = f"""
You are a Follow-up Questions Agent. Read the transcript below and produce 6 conversational,
open-ended follow-up questions grouped by the themes: Migration, Work, Housing, Family, Community.
For each question include a one-line rationale referencing the transcript and a Sensitive: yes/no flag.
Do not invent facts; base questions only on the transcript.

Transcript:
{transcript}

Output format:
### Migration
1. Question
   - Rationale: ...
   - Sensitive: yes/no

Produce exactly 6 questions in total, prioritising one per theme then allocate extras to gaps.
Tone: conversational.
"""

data = {
    "model": MODEL,
    "prompt": prompt,
    "max_tokens": 800,
}

req = Request(URL, data=json.dumps(data).encode("utf-8"), headers={"Content-Type": "application/json"})

def main():
    try:
        with urlopen(req, timeout=30) as resp:
            resp_data = resp.read().decode("utf-8")
            # Ollama may stream or return JSON; try to parse JSON first
            try:
                parsed = json.loads(resp_data)
                # Common field: 'text' or 'generated' depending on server
                text = parsed.get('text') or parsed.get('generated') or parsed.get('output')
                if isinstance(text, list):
                    text = "\n".join(text)
                if not text:
                    # try to extract any nested fields
                    text = resp_data
            except Exception:
                text = resp_data
            print(text)
    except Exception as e:
        print(f"Request failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
