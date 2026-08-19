from mcp.server.fastmcp import FastMCP

mcp = FastMCP("BNT Gambia Evidence")

@mcp.tool()
def search_evidence(query: str) -> str:
    """
    Search the BNT Gambia evidence database.
    """
    return f"Evidence search requested for: {query}"

if __name__ == "__main__":
    mcp.run()
