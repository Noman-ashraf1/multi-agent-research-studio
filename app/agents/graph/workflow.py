from langgraph.graph import StateGraph

from app.agents.graph.state import ResearchState
from app.agents.planner import planner_agent
from app.agents.researcher import research_agent
from app.agents.summarize import summarizer_agent
from app.agents.writer import writer_agent
from app.agents.critic_agent import critic_agent
from app.agents.refiner_agent import refiner_agent


graph = StateGraph(ResearchState)

graph.add_node("planner", planner_agent)
graph.add_node("researcher", research_agent)
graph.add_node("summarizer", summarizer_agent)
graph.add_node("writer", writer_agent)
graph.add_node("critic", critic_agent)
graph.add_node("refiner", refiner_agent)

graph.set_entry_point("planner")

graph.add_edge("planner", "researcher")
graph.add_edge("researcher", "summarizer")
graph.add_edge("summarizer", "writer")
graph.add_edge("writer", "critic")


def route_after_critic(state):
    if state.get("score", 0) < 7:
        return "refiner"
    return "__end__"


graph.add_conditional_edges(
    "critic",
    route_after_critic,
    {
        "refiner": "refiner",
        "__end__": "__end__"
    }
)

graph.add_edge("refiner", "__end__")

workflow = graph.compile()