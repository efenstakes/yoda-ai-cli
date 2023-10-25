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
    llm = ChatOpenAI(temperature=0.5)

    # create conversation chain with a summary buffer memory
    # this will ensure we dont lose context
    conversation = ConversationChain(
        llm=llm,
        memory=ConversationSummaryBufferMemory(llm=llm),
        # prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
        verbose=False
    )

    # keep yoda terminal running until user quits with Ctrl^ + c
    while True:
        prompt = input("Ask Yoda 👉 ")
        print()
        reply = conversation.predict(input=prompt)

        print(f"Reply", color="magenta")
        print(f"{reply}", color="green")
        print()
        print()

        


if __name__ == '__main__':
    main()
