from app.agents.tools.web_search import search_web

def research_agent(state):
    print("Research Agent Running...")

    topic = state["topic"]

    docs = search_web(topic)

    state["documents"] = docs
    state["research_notes"] = docs  # ✅ add this if writer uses it

    print("RESEARCH OUTPUT:", state.get("documents"))
    print("RESEARCH NOTES:", state.get("research_notes"))

    return state