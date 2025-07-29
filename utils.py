from gen_ai_hub.proxy.native.openai import chat
from typing import List, Dict, Any, Optional

def call_llm(messages: List[Dict[str, str]], model_name: str = "gpt-4.1") -> str:
    """
    Call the SAP GenAI Hub API with the given messages using the native OpenAI-compatible interface.
    
    Args:
        messages: List of message dictionaries with 'role' and 'content' keys
        model_name: Name of the model to use (default: "gpt-4")
        
    Returns:
        The generated response as a string
        
    Raises:
        Exception: If there's an error calling the API
    """
    try:
        # Call the chat completions API using the native OpenAI-compatible interface
        response = chat.completions.create(
            model_name=model_name,
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        
        # Extract and return the response text
        if hasattr(response, 'choices') and len(response.choices) > 0:
            return response.choices[0].message.content.strip()
        else:
            raise ValueError("No response content in API response")
            
    except Exception as e:
        raise Exception(f"Error calling SAP GenAI Hub: {str(e)}")
