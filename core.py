"""
2-Agent system where:
- Assistant takes user's (complex) question, breaks it down into smaller pieces
    if needed
- WebSearch takes Assistant's question, uses the Search tool to search the web
    (using DuckDuckGo), and returns a coherent answer to the Assistant.

Once the Assistant thinks it has enough info to answer the user's question, it
says DONE and presents the answer to the user.
"""

from dotenv import load_dotenv
import langroid as lr
import langroid.language_models as lm
from langroid.agent.tools.duckduckgo_search_tool import DuckduckgoSearchTool

def setup_agents(model: str = "groq/llama3-8b-8192"):
    
    load_dotenv()

    llm_config = lm.OpenAIGPTConfig(
        chat_model=model,
        chat_context_length=8192,
        temperature=0,
        max_output_tokens=200,
    )
    search_tool_handler_method = DuckduckgoSearchTool.default_value("request")

    assistant_config = lr.ChatAgentConfig(
        system_message="""
        You are a resourceful assistant, able to think step by step to answer
        complex questions from the user. You must break down complex questions into
        simpler questions that can be answered by a web search. You must ask me 
        (the user) each question ONE BY ONE, and I will do a web search and send you
        a brief answer. Once you have enough information to answer my original
        (complex) question, you MUST say DONE and present the answer to me.
        """,
        llm=llm_config,
        vecdb=None,
    )

    search_agent_config = lr.ChatAgentConfig(
        llm=llm_config,
        vecdb=None,
        system_message=f"""
        You are a web-searcher. For any question you get, you must use the
        `{search_tool_handler_method}` tool/function-call to get up to 3 results.
        I WILL SEND YOU THE RESULTS; DO NOT MAKE UP THE RESULTS!!
        Once you receive the results, you must compose a CONCISE answer 
        based on the search results and say DONE and show the answer to me,
        in this format:
        DONE [... your CONCISE answer here ...]
        IMPORTANT: YOU MUST WAIT FOR ME TO SEND YOU THE 
        SEARCH RESULTS BEFORE saying you're DONE.
        """,
    )

    assistant_agent = lr.ChatAgent(assistant_config)
    search_agent = lr.ChatAgent(search_agent_config)
    search_agent.enable_message(DuckduckgoSearchTool)

    return assistant_agent, search_agent

def create_task(agent, name):
    """
    Wrap the given agent in a Task class, which enables it to interact with other agents 
    """
    return lr.Task(
        agent,
        name=name,
        llm_delegate=True,
        single_round=False,
        interactive=False,
    )

def setup_tasks():
    assistant_agent, search_agent = setup_agents()
    assistant_task = create_task(assistant_agent, "Assistant")
    search_task = create_task(search_agent, "Search")
    assistant_task.add_sub_task(search_task)
    return assistant_task