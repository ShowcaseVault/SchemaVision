# SchemaVision

SchemaVision turns natural‑language questions into precise SQL queries using your database schema. It ensures queries are schema‑aware (no hallucinated tables or columns) and can optionally persist question/answer pairs for review.

## What it does
- Translates plain‑English questions into SQL.
- Reads a cached schema from `schema/db_schema.json` or, if absent/empty, crawls the live database to build it.
- Generates SQL strictly from the known schema (tables, columns, and relationships).
- Returns only the raw SQL string as the final answer.
- Can batch through example questions and save results to `schema/questions_answers.json`.

## How it works (the idea)
- **Tool‑driven agent**
  - `read_schema_tool`: Loads `schema/db_schema.json` safely. If missing/empty/invalid, it indicates that state to the agent.
  - `crawl_schema_tool`: Uses SQLAlchemy’s Inspector to introspect the database (tables, columns, foreign keys) and writes a compact schema map to `schema/db_schema.json`.
- **Prompted protocol** (enforced in the agent prompt)
  - Always read the schema first.
  - If empty or missing, crawl the DB, then read the schema again.
  - Build SQL using only the discovered schema. Use explicit JOINs. Default to ANSI SQL if dialect is unclear.
  - Output only the SQL text (no markdown, no explanations).
- **Orchestration**
  - A LangChain agent (Groq LLM + schema tools) reads/maintains the schema and returns only the SQL. It can also batch questions and persist Q&A if desired.

## Graph Visualization
- `create_graph.py`: Creates a graph of the database schema using NetworkX and Matplotlib.
- Allows to visualize the schema in a graph format.