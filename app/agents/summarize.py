from app.agents.llm.llm import llm

def summarizer_agent(state):
    print("Summarizer Agent Running...")

    documents = state.get("documents", [])

    if not documents:
        state["context"] = "No research documents found."
        return state

    # Build clean input
    docs_text = "\n\n".join([
        f"Title: {doc.get('title')}\nContent: {doc.get('content')}"
        for doc in documents
    ])

    prompt = f"""
You are a research summarizer.

Task:
- Extract ONLY factual and useful information
- Remove noise and duplicates
- Keep key points only
- Do NOT add outside knowledge

Documents:
{docs_text}

Return a clean, structured summary with bullet points.
"""

    summary = llm.invoke(prompt).content

    state["context"] = summary

    print("SUMMARY CREATED")
    return state