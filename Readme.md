# Yoda AI CLI:
## Your Wise Companion In Your CLI

Welcome to Yoda AI, your ultimate AI companion! Yoda is designed to be your go-to solution for a wide range of tasks, from answering questions and providing insights to offering assistance and entertainment. In this document, we'll introduce you to the exciting world of Yoda AI and guide you through getting started.


<img src="/showcase/cli-2.png" width="100%" />



## Introduction

Yoda AI is a cutting-edge artificial intelligence designed to enhance your daily life. It combines natural language understanding, machine learning, and a vast knowledge base to assist you with a wide range of tasks. Whether you need answers to questions, want to engage in meaningful conversations, or simply seek entertainment, Yoda AI has you covered.

## Key Features

1. Conversational AI: Hold engaging conversations with Yoda AI, just like chatting with a friend.

2. Knowledge Base: Access a wealth of information, facts, and insights across various domains.

3. Personal Assistant: Set reminders, create to-do lists, and get weather updates.

4. Entertainment: Enjoy jokes, riddles, and even some wisdom from the wise Yoda himself.

5. Customization: Tailor Yoda AI to your preferences and needs.


## Tech Used

Python: Python is the language of choice for this Yoda AI's codebase. It's a perfect language for building AI powered products with ease.

Langchain: LangChain is a framework designed to simplify the creation of applications using large language models. As a language model integration framework. It allows building complex AI and personal assistants that can supercharge productivity.

## Adding Yoda To CLI
You can easily add yoda to your cli to use in your terminal or your favorite IDE. First, clone the `Yoda AI CLI` code from github.

```sh
git clone https://github.com/efenstakes/yoda-ai-cli.git
cd yoda-ai-cli
```

Install the dependencies
``` sh
pip3 install -r requirements.txt
```

And yes, if you are wondering, you won't have to create an environment because we need to access the dependencies and `CLI` globally. Create a `.env` file and add `OPENAI_API_KEY` variable with your `openai key`.

Get path to the folder you just cloned `Yoda` to:

```sh
pwd
```

Cd to your root folder:

```sh
cd ~
```

For some people, you may have to edit .zshrc or .bashrc. You can use vi or your favorite IDE or text editor. Add an alias with your name of choice, in my case it's `yodaai`.

```sh
alias yodaai = <path-to-the-yodaai-cli-project-directory>
```

Replace `<path-to-the-yodaai-cli-project-directory>` with the directory you cloned yoda cli into.



You're done. Enjoy `Yoda CLI` now.

## Extras
I build a similar API to this in Golang and NodeJS. You can find it here in my github.


## Contact
If you wish to contact me, use my email efenstakes101@gmail.com.