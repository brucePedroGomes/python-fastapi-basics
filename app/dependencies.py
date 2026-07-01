from fastapi import Header


async def get_api_version(x_api_version: str | None = Header(default=None)) -> str:
    """Read an optional API version header."""
    return x_api_version or "v1"
