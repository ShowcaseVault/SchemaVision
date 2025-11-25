from langchain.agents import create_agent
from agent.utils.extract_response import extract_response_and_usage
from agent.utils.get_tools import tools
from agent.client.groq_client import groq
from agent.prompt.agent_prompt_basic import agent_prompt


from config.config import settings
# -----
# Load response file
response_file = settings.RESPONSE_FILE
# -----

# ----------------------------
# Init agent
# ----------------------------
agent = create_agent(
    model=groq,
    tools=tools,
    system_prompt= agent_prompt
)

# ----------------------------
# Ask the agent a question
# ----------------------------
def ask(question:str):
    result = agent.invoke(
        {"messages": [{"role": "user", "content": f"{question}"}]}
    )
    response = extract_response_and_usage(result)
    return response


if __name__ == "__main__":
    import json
    # ----------------------------
    # Load schema on multiple questions, we only need to crawl, if schema is not available
    from agent.utils.read_schema import load_schema
    from agent.utils.crawl_schema import crawl_schema
    schema = load_schema()
    if not schema:
        crawl_schema()
    # -------------------------
    questions = [
        "Who are the customers in the database?",
        "What is the email of customer 'John Doe'?",
        "How many invoices has customer 'Jane Smith' made?",
        "Which genre has the most tracks?",
        "How much revenue has each artist generated?",
        "Who are the top 5 customers who spent the most?",
        "What is the total revenue per month in 2009?"
    ]

    store = []

    for number, question in enumerate(questions, start=1):
        print(f"Question {number}: {question}")
        response = ask(question)
        print(f"Response {number}: {response.get('response')}")

        store.append({
            "question": question,
            **response
        })

    # Save to a JSON file
    with open(response_file, "w") as f:
        json.dump(store, f, indent=4)

    print("Saved all Q&A to questions_answers.json")