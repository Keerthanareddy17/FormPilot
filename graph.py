from typing import List, Dict, Optional, TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda, Runnable
from agents.field_mapper import map_field_label_to_key
from utils.memory_manager import get_value, update_memory

class GraphState(TypedDict):
    fields: List[Dict]
    mapped_fields: Optional[List[Dict]]
    filled_fields: Optional[List[Dict]]
    missing_fields: Optional[List[Dict]]
    fallbacks: Optional[Dict]
    final_fields: Optional[List[Dict]]

def label_mapper_node(state: GraphState) -> GraphState:
    mapped_fields = []
    for field in state["fields"]:
        mapped_key = map_field_label_to_key(field["label"])
        mapped_fields.append({
            "label": field["label"],
            "type": field["type"],
            "mapped_key": mapped_key
        })
    return {**state, "mapped_fields": mapped_fields}

def memory_fetcher_node(state: GraphState) -> GraphState:
    filled_fields = []
    for field in state["mapped_fields"]:
        val = get_value(field["mapped_key"])
        filled_fields.append({**field, "value": val})
    return {**state, "filled_fields": filled_fields}

def missing_detector_node(state: GraphState) -> GraphState:
    missing = []
    for field in state["filled_fields"]:
        if field.get("value") in [None, ""]:
            missing.append(field)
    return {**state, "missing_fields": missing}

def fallback_generator_node(state: GraphState) -> GraphState:
    fallbacks = {}
    for field in state.get("missing_fields", []):
        placeholder = f"[Please fill {field['label']}]"
        fallbacks[field["mapped_key"]] = placeholder
        update_memory(field["mapped_key"], placeholder)
    return {**state, "fallbacks": fallbacks}

def final_consolidator_node(state: GraphState) -> GraphState:
    final_fields = []
    for field in state["filled_fields"]:
        val = get_value(field["mapped_key"])
        final_fields.append({**field, "value": val})
    return {**state, "final_fields": final_fields}

def build_autoform_graph() -> Runnable:
    graph = StateGraph(GraphState)

    graph.add_node("label_mapper", label_mapper_node)
    graph.add_node("memory_fetcher", memory_fetcher_node)
    graph.add_node("missing_detector", missing_detector_node)
    graph.add_node("fallback_generator", fallback_generator_node)
    graph.add_node("final_consolidator", final_consolidator_node)

    graph.set_entry_point("label_mapper")
    graph.add_edge("label_mapper", "memory_fetcher")
    graph.add_edge("memory_fetcher", "missing_detector")
    graph.add_edge("missing_detector", "fallback_generator")
    graph.add_edge("fallback_generator", "final_consolidator")
    graph.add_edge("final_consolidator", END)

    return graph.compile()

autoform_graph = build_autoform_graph()

def run_autoform_graph(fields: List[Dict]) -> List[Dict]:
    initial_state: GraphState = {"fields": fields}
    result = autoform_graph.invoke(initial_state)
    return result["final_fields"]
