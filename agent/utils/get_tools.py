import json
from langchain.tools import tool
from agent.utils.read_schema import read_schema
from agent.utils.crawl_schema import crawl_schema


# ----------------------------
# Tool: read schema
# ----------------------------
@tool
def read_schema_tool() -> str:
    """Returns the current database schema as a JSON string."""
    return read_schema()

# ----------------------------
# Tool: run crawler
# ----------------------------
@tool
def crawl_schema_tool() -> str:
    """Runs the schema crawler and returns the result."""
    return crawl_schema()

tools = [read_schema_tool, crawl_schema_tool]
