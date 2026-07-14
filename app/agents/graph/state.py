from typing import TypedDict, List, Dict


class ResearchState(TypedDict):
    topic: str
    outline: str
    documents: List[Dict]
    context: str
    report: str
    critique: Dict
    score: int