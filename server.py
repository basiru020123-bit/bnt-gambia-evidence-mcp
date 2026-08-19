from mcp.server.fastmcp import FastMCP

mcp = FastMCP("BNT Gambia Evidence")


@mcp.tool()
def search_evidence(query: str) -> str:
    """Search BNT Gambia evidence sources."""
    return f"Evidence search requested for: {query}"


app = mcp.streamable_http_app()
