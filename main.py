from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from print_color import print


def main():
    # load env vars
    load_dotenv()

    # ensure env vars are loaded
    if os.getenv("OPENAI_API_KEY") is None:
        print("OPENAI_API_KEY must be set in environment")
        exit(1)

    # create chat instance
    llm = ChatOpenAI(temperature=0.5, streaming=True)

    # create conversation chain with a summary buffer memory
    # this will ensure we dont lose context
    conversation = ConversationChain(
        llm=llm,
        memory=ConversationSummaryBufferMemory(llm=llm),
        # prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
        verbose=False
    )

    # print cli instructions
    print_cli_instructions()

    # keep yoda terminal running until user quits with Ctrl^ + c
    while True:
        print(f"Ask Yoda", color="magenta")
        print()
        # prompt = input("Ask Yoda 👉 ")
        prompt = input("👉 ")
        print()

        # check if we should quit
        if prompt.strip().lower() == "quit" or prompt.strip().lower() == "q":
            quit_cli()

        # get reply from llm
        reply = conversation.predict(input=prompt)

        print_prompt_reply(prompt=prompt, reply=reply)

        
# print cli instructions
def print_cli_instructions():
    print()
    print("Remember you can always type 'quit' or 'q' to exit the YODA CLI", color="black")
    print()

# closes the cli
def quit_cli():
    print("Yoda AI CLI is shutting down now", color="green")
    print("Bye Bye ~ Yoda", color="magenta")
    print()
    exit(0)

# prints answer
def print_prompt_reply(prompt: str, reply: str):
    print(f"Reply", color="magenta")
    print(f"{reply}", color="green")
    print()
    print()


if __name__ == '__main__':
    main()
