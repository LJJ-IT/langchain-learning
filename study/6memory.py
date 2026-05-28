# langchain提供的checkpointer的默认实现，基于内存存储
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv() # 加载环境变量
# 创建智能体时指定checkpointer，LangChain会自动帮我们管理历史会话记忆
agent = create_agent(
    "deepseek-chat",
    checkpointer=InMemorySaver()
)
# 设定thread_id，作为会话标识
config = {"configurable": {"thread_id": "thread_1"}}

# 第一次对话
response1 = agent.invoke(
    {"messages": [HumanMessage(content="你好，我叫劫，我最喜欢猫猫。")]},
    config
)

# 第二次对话（同一进程）
response2 = agent.invoke(
    {"messages": [HumanMessage(content="你知道我叫啥吗？我最喜欢的是啥？")]},
    config
)

print(response1)
print(response2)
