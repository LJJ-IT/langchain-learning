import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv() # 加载环境变量

# 初始化checkpointer
checkpointer = SqliteSaver(sqlite3.connect("checkpoint.db", check_same_thread=False))
# 自动建表
checkpointer.setup()

# 创建agent
agent = create_agent(
    "deepseek-chat",
    checkpointer=checkpointer,
)

config = {"configurable": {"thread_id": "thread_1"}}
response1 = agent.invoke(
    {"messages": [HumanMessage(content="你知道我喜欢什么吗。")]},
    config
)
print(response1)