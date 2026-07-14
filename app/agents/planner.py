from app.agents.llm.llm import llm

def planner_agent(state):
    print("Planner Agent Running...")
    topic = state["topic"]

    prompt = f"""
    Create a detailed report outline for:

    {topic}

    Return only headings.
    """

    outline = llm.invoke(prompt).content

    state["outline"] = outline
    print("PLANNER OUTPUT:", state)

    return state