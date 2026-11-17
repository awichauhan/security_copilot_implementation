import httpx

from config import settings


async def generate_response(prompt: str) -> str:
    # This HTTP client lets our backend talk to the local Ollama server.
    # async with closes the client when we finish; await waits for the answer.
    async with httpx.AsyncClient(timeout=180.0) as client:
        result = await client.post(
            f"{settings.ollama_url.rstrip('/')}/api/generate",
            json={
                "model": settings.model_name,
                "prompt": prompt,
                "stream": False,  # Wait for the complete answer in one response.
            },
        )

    # Convert Ollama's JSON into a dictionary and return the answer text.
    data = result.json()
    return data["response"]
