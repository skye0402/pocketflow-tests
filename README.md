# SAP GenAI Hub Chat Application with PocketFlow

A simple text-based chat application that integrates SAP GenAI Hub with PocketFlow for agentic workflows.

## Features

- Simple command-line chat interface
- Integration with SAP GenAI Hub's language models
- Built with PocketFlow for agentic workflow management
- Environment variable based configuration
- Support for chat history and context

## Prerequisites

- Python 3.8+
- SAP Business Technology Platform (BTP) account with access to SAP AI Core and GenAI Hub
- Required environment variables (see Configuration section)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd pocketflow
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root with the following variables:
   ```
   AICORE_BASE_URL=your_ai_core_base_url
   AICORE_AUTH_URL=your_ai_core_auth_url
   AICORE_CLIENT_ID=your_client_id
   AICORE_CLIENT_SECRET=your_client_secret
   AICORE_RESOURCE_GROUP=your_resource_group
   ```

2. Replace the placeholder values with your actual SAP BTP credentials.

## Usage

### Chat Example

To start the simple chat application:

1. Navigate to the project root directory:
   ```bash
   cd /path/to/pocketflow
   ```

2. Activate the virtual environment (if not already activated):
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Run the chat application:
   ```bash
   python -m chat_simple.main
   ```

4. Start chatting! Type your messages and press Enter. To exit, type 'exit' or press Ctrl+C.

### MCP Server Example

To run the MCP server example that demonstrates tool usage:

1. Make sure your virtual environment is activated
2. Run the following command to test a calculation:
   ```bash
   python -m mcp_simple.main --"What is 10 minus 2?"
   ```

3. Try other operations:
   ```bash
   python -m mcp_simple.main --"What is 15 plus 27?"
   python -m mcp_simple.main --"What is the weather in Tokyo?"
   ```

### Other Examples

*More examples coming soon!*

## Project Structure

- `chat_simple/`: Simple chat application example
  - `main.py`: Main application script with the chat interface
- `common/`: Shared utilities
  - `utils.py`: Utility functions for interacting with SAP GenAI Hub
- `.env.example`: Example environment variables file (copy to .env and fill in your credentials)
- `requirements.txt`: Python dependencies

## Troubleshooting

- **Error: No deployment found with model_name**
  - Verify that the model name in `utils.py` matches a model available in your SAP GenAI Hub deployment.
  - Check that your SAP BTP account has access to the requested model.

- **Authentication errors**
  - Double-check your environment variables in the `.env` file.
  - Ensure your SAP BTP account has the necessary permissions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [SAP GenAI Hub](https://help.sap.com/doc/generative-ai-hub-sdk/CLOUD/en-US/index.html)
- [PocketFlow](https://github.com/The-Pocket/PocketFlow)
