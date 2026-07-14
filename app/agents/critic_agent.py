import json

from app.agents.llm.llm import llm


def critic_agent(state):
    print("Critic Agent Running...")

    prompt = f"""
You are a strict AI research critic.

Your job is to evaluate the generated report.

RULES:
- Check if the report follows the outline.
- Check if information is supported by the provided context.
- Detect hallucinations or unsupported claims.
- Identify missing sections.
- Evaluate clarity, structure, and completeness.
- Do NOT rewrite the report.
- Return ONLY valid JSON.

OUTPUT FORMAT:
{{
  "score": 0,
  "issues": [],
  "missing_sections": [],
  "hallucinations": []
}}

TOPIC:
{state.get("topic", "")}

OUTLINE:
{state.get("outline", "")}

CONTEXT:
{state.get("context", "")}

REPORT:
{state.get("report", "")}
"""

    try:
        response = llm.invoke(prompt).content.strip()

        # Remove markdown code fences if model returns them
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        critique = json.loads(response)

    except Exception as e:
        print("Critic JSON Parse Error:", e)

        critique = {
            "score": 5,
            "issues": ["Failed to parse critic output"],
            "missing_sections": [],
            "hallucinations": []
        }

    state["critique"] = critique
    state["score"] = critique.get("score", 5)

    print("\n=== CRITIC RESULT ===")
    print("Score:", state["score"])
    print("Issues:", critique.get("issues", []))
    print("=====================\n")

    return state