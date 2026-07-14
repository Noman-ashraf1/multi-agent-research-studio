from app.agents.llm.llm import llm

def writer_agent(state):
    print("Writer Agent Running...")

    topic = state.get("topic", "")
    outline = state.get("outline", "")
    context = state.get("context", "")

    prompt = f"""
You are a professional AI research writer.

Your job is to write a COMPLETE, WELL-STRUCTURED, FACTUAL report.

STRICT RULES:
- Use ONLY the provided context
- Do NOT use external knowledge
- If information is missing, write: "Not found in sources"
- Do NOT copy text directly; always summarize
- Ensure the report is complete (no cut-off sections)
- Follow the outline structure exactly
- Write in clear academic style

TOPIC:
{topic}

OUTLINE:
{outline}

SUMMARIZED CONTEXT:
{context}

FINAL OUTPUT REQUIREMENTS:
- Fully complete report
- Proper headings
- Clean explanations
- Strong conclusion at the end
"""

    response = llm.invoke(prompt).content

    state["report"] = response

    print("Writer USED CONTEXT LENGTH:", len(context))
    print("Writer STATE KEYS:", state.keys())

    return state