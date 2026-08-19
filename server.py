import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("BNT Gambia Evidence")


@mcp.tool()
def search_evidence(query: str) -> str:
    """Search BNT Gambia evidence sources."""
    return f"Evidence search requested for: {query}"


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
    )
