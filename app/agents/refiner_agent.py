from app.agents.llm.llm import llm


def refiner_agent(state):
    print("Refiner Agent Running...")

    critique = state.get("critique", {})
    score = critique.get("score", 0)

    # Skip refinement if report is already good
    if score >= 9:
        print("High quality report detected. Skipping refinement.")
        return state

    prompt = f"""
You are an expert research report editor.

TASK:
Improve the report using the critic feedback.

STRICT RULES:
1. Fix every issue identified by the critic.
2. Add missing sections if mentioned.
3. Remove hallucinated information.
4. Improve clarity, readability, and structure.
5. Follow the provided outline.
6. Use ONLY information present in the context.
7. Never invent facts.
8. If information is missing, write:
   "Not found in sources."
9. Return ONLY the final improved report.

TOPIC:
{state.get("topic")}

OUTLINE:
{state.get("outline")}

CONTEXT:
{state.get("context")}

CRITIC FEEDBACK:
{critique}

REPORT:
{state.get("report")}
"""

    try:
        response = llm.invoke(prompt).content

        if response and len(response.strip()) > 100:
            state["report"] = response
            print("Report refined successfully")
        else:
            print("Refiner returned invalid output. Keeping original report.")

    except Exception as e:
        print(f"Refiner Error: {e}")

    return state