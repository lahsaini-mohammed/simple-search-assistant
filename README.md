This project implements a two-agent system for web search and question answering using the Langroid framework. The system consists of an Assistant agent that breaks down complex questions and a WebSearcher agent that performs web searches to answer these questions.

## Project Structure

- **core.py**: Contains the main logic for setting up and managing the agents and tasks.
- **cli.py**: Provides a command-line interface for interacting with the system.
- **web.py**: Offers a web-based interface using Chainlit for user interaction.

## How It Works

1. **Assistant Agent**: 
   - Breaks down complex questions into simpler sub-questions.
   - Interacts with the Search Agent to gather necessary information.
   - Compiles a final answer once enough information is gathered.

2. **Search Agent**:
   - Performs web searches using DuckDuckGo.
   - Provides concise answers based on search results.
   - Works as a sub-task under the Assistant agent.

## Sample Questions:

- The actress that had the role of Martha Alston, plays what role in Finding Nemo?
- Who was the president of the United States when the first Star Wars movie was released?
- Which actress is noted for having bipolar disorder and portraying Princess Leia in the Star Wars films?
- what is the currency used in the country that contains Oujda?
- Which character does the actress who went to Napanee District Secondary School play in Over the Hedge?
- What nation bordering Russia has a religious leader named Filaret?
- Who was the actress who played Miss Casswell and had an affair with John Kennedy?
- What is the capital of the country with the Cherifian National Anthem?
- Which country speaks Arabic and has a Berber language as its official language?
- In 2012, who ran for Vice President with the politician who held the governmental position Under Secretary of Defense for Personnel and Readiness?

## Requirements
`Langroid[chainlit]`

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/lahsaini-mohammed/simple-search-assistant.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
    Ensure you have Python 3.11+ installed, then run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Environment Variables**:
Create a .env file in the root directory and add your Groq api key:
    ```
    GROQ_API_KEY= gsk_...
    ```
## Usage

### CLI Interface

- Run the CLI interface with: `python cli.py`

### Web Interface

- Run the web interface with: `chainlit run web.py`