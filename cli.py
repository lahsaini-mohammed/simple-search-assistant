from rich import print
from rich.prompt import Prompt
from core import setup_tasks

def main() -> None:

    print(
        """
        [blue]Welcome to the Web Search Assistant!
        I will try to answer your complex questions.

        Enter x or q to quit at any point
        """
    )
    assistant_task = setup_tasks()
    while True:
        question = Prompt.ask("[red]What do you want to know?")
        if question.lower() == "x" or question.lower() == "q" or question.lower() == "quit":
            break
        assistant_task.run(question)

if __name__ == "__main__":
    main()