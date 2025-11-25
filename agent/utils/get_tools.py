from langchain.tools import tool
from agent.utils.read_schema import read_schema
from agent.utils.crawl_schema import crawl_schema

# ----------------------------
# Tool: read schema
# ----------------------------
@tool
def read_schema_tool() -> str:
    """
    Reads the cached database schema from the JSON file. 
    ALWAYS call this tool first to understand the tables, columns, and relationships.
    """
    return read_schema()

# ----------------------------
# Tool: run crawler
# ----------------------------
@tool
def crawl_schema_tool() -> str:
    """
    Connects to the live database to extract and save the schema structure.
    Use this tool ONLY if 'read_schema_tool' returns an empty result, an error, or indicates the schema is missing.
    """
    return crawl_schema()

tools = [read_schema_tool, crawl_schema_tool]
