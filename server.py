import os

from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    "BNT Gambia Evidence",
    stateless_http=True,
)


@mcp.tool()
def search_evidence(query: str) -> str:
    """Search BNT Gambia evidence sources."""
    return f"Evidence search requested for: {query}"


# ASGI application for Uvicorn/Render
app = mcp.streamable_http_app()
