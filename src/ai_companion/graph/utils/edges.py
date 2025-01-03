from ai_companion.graph.utils.state import AICompanionState
from ai_companion.settings import settings

from langgraph.graph import END
from typing_extensions import Literal


def should_summarize_conversation(
    state: AICompanionState,
) -> Literal["summarize_conversation", "__end__"]:
    messages = state["messages"]

    if len(messages) > settings.NUMBER_OF_MESSAGES_TO_KEEP:
        return "summarize_conversation"

    return END


def select_workflow(
    state: AICompanionState,
) -> Literal["conversation_node", "image_node", "audio_node"]:
    workflow = state["workflow"]

    if workflow == "image":
        return "image_node"

    elif workflow == "audio":
        return "audio_node"

    else:
        return "conversation_node"
