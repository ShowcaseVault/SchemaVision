def extract_response_and_usage(agent_output):
    """
    Extracts the content and usage metadata from the final message 
    of a LangChain agent response.
    """
    try:
        # 1. Access the list of messages
        messages = agent_output.get('messages', [])
        
        if not messages:
            return {"error": "No messages found in output"}
        
        # 2. Get the last message (the final AI response)
        last_message = messages[-1]
        
        # 3. Extract Content
        # Handle cases where message is a Dict or an Object (LangChain Message)
        if isinstance(last_message, dict):
            content = last_message.get('content', '')
            # Try to find usage in dict keys
            usage = last_message.get('usage_metadata') or \
                    last_message.get('response_metadata', {}).get('token_usage')
        else:
            # Access via Object attributes
            content = getattr(last_message, 'content', '')
            
            # Standard LangChain usage attribute (preferred)
            usage = getattr(last_message, 'usage_metadata', None)
            
            # Fallback: Check inside response_metadata if usage_metadata is empty
            if not usage:
                response_meta = getattr(last_message, 'response_metadata', {})
                usage = response_meta.get('token_usage')

        return {
            "response": content,
            "usage": usage
        }

    except Exception as e:
        return {"error": str(e)}