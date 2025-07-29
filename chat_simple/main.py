import os
from dotenv import load_dotenv
from typing import Dict, Any, Optional
from pocketflow import Node, Flow

# Load environment variables from .env file
load_dotenv()

# Import the call_llm function from utils
from common.utils import call_llm

class ChatNode(Node):
    """A node that handles the chat interaction with the user."""
    
    def prep(self, shared: Dict[str, Any]) -> Optional[list]:
        """Prepare the chat interaction.
        
        Args:
            shared: Shared state between nodes
            
        Returns:
            List of messages for the LLM, or None to end the conversation
        """
        # Initialize messages if this is the first run
        if "messages" not in shared:
            shared["messages"] = []
            print("Welcome to the AI Chat App!")
            print("Type 'exit' to end the conversation.")
        
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check if user wants to exit
        if user_input.lower() == 'exit':
            return None
        
        # Add user message to history
        shared["messages"].append({"role": "user", "content": user_input})
        
        # Return all messages for the LLM
        return shared["messages"]

    def exec(self, messages: Optional[list]) -> Optional[str]:
        """Execute the LLM call.
        
        Args:
            messages: List of messages for the LLM, or None to end the conversation
            
        Returns:
            The LLM's response, or None to end the conversation
        """
        if messages is None:
            return None
        
        # Call LLM with the entire conversation history
        try:
            response = call_llm(messages)
            return response
        except Exception as e:
            print(f"\nError calling LLM: {e}")
            return "I'm sorry, I encountered an error. Please try again."

    def post(self, shared: Dict[str, Any], prep_res: Optional[list], exec_res: Optional[str]) -> Optional[str]:
        """Handle the LLM's response.
        
        Args:
            shared: Shared state between nodes
            prep_res: Result from prep() - the list of messages
            exec_res: Result from exec() - the LLM's response
            
        Returns:
            "continue" to continue the conversation, or None to end it
        """
        if prep_res is None or exec_res is None:
            print("\nGoodbye!")
            return None  # End the conversation
        
        # Print the assistant's response
        print(f"\nAI: {exec_res}")
        
        # Add assistant message to history
        shared["messages"].append({"role": "assistant", "content": exec_res})
        
        # Loop back to continue the conversation
        return "continue"

def create_chat_flow() -> Flow:
    """Create and configure the chat flow.
    
    Returns:
        A configured Flow instance for the chat application
    """
    # Create the chat node
    chat_node = ChatNode()
    
    # Set up the self-loop to continue the conversation
    chat_node - "continue" >> chat_node  # Loop back to continue conversation
    
    # Create and return the flow
    return Flow(start=chat_node)

def main():
    """Main entry point for the chat application."""
    # Check if all required environment variables are set
    check_env_vars()
    
    # Create and run the chat flow
    flow = create_chat_flow()
    
    # Start the chat with an empty shared state
    flow.run({})

def check_env_vars():
    """Check if all required environment variables are set for SAP AI Hub."""
    required_vars = [
        "AICORE_BASE_URL",
        "AICORE_AUTH_URL",
        "AICORE_CLIENT_ID",
        "AICORE_CLIENT_SECRET",
        "AICORE_RESOURCE_GROUP"
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"Error: The following required environment variables are not set: {', '.join(missing_vars)}")
        print("Please create a .env file based on the .env.example template and provide the required values.")
        exit(1)

if __name__ == "__main__":
    main()
