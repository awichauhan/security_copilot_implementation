from pydantic import BaseModel, Field


# The JSON sent by the frontend: {"prompt": "your question"}.
class ChatRequest(BaseModel):
    prompt: str


# A future retrieved source. These fields are a simple starting point for RAG.
class Source(BaseModel):
    title: str
    content: str


# The JSON our backend sends back to the frontend.
class ChatResponse(BaseModel):
    response: str
    # Give each response its own empty list. We will add sources when RAG exists.
    sources: list[Source] = Field(default_factory=list)
