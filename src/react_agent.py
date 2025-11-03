import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain.memory import ConversationBufferMemory
from tools import tools

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# References: #https://arxiv.org/abs/2210.03629 
# https://smith.langchain.com/hub/hwchase17/react?organizationId=ddc97521-be46-4819-b31a-1849c06d7ff3 
# https://python.langchain.com/api_reference/langchain/agents/langchain.agents.react.agent.create_react_agent.html 
# By using langsmith portal, we can trace the workflow for monitoring purpose.

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3, openai_api_key=OPENAI_API_KEY)

# ReAct prompt
prompt = hub.pull("hwchase17/react")

if "chat_history" not in prompt.input_variables:
    prompt.input_variables.append("chat_history")
prompt.template = ("The conversation so far:\n{chat_history}\n\n" + prompt.template)

# Create memory
memory = ConversationBufferMemory(memory_key="chat_history", input_key="input", return_messages=True)

# Build agent and executor
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True, handle_parsing_errors=True)


def run_agent(query):
    response = agent_executor.invoke({"input": query})
    return response["output"]

if __name__ == "__main__":
    print("🤖 ChatBMW Welcomes you\n")
    while True:
        user_input = input("User: ")
        if user_input in ["exit", "quit"]:
            break
        response = run_agent(user_input)
        print(f"Agent: {response}\n")
