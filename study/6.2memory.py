from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables import RunnableConfig
from langchain.chat_models import init_chat_model# 初始化大模型
from dotenv import load_dotenv
import os

load_dotenv() # 加载环境变量

#初始化qwen模型用来总结
qwen_model=init_chat_model(
    model=os.getenv("QWEN_MODEL_NAME"),
    model_provider="openai",
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url=os.getenv("SILICONFLOW_BASE_URL"),
)
# 初始化checkpointer
checkpointer = InMemorySaver()
# 初始化中间件
middleware = SummarizationMiddleware(
    model=qwen_model,
    trigger=("messages", 3), #  触发时机，当消息数超过3时，进行总结
    keep=("messages", 1) #  保留的会话数，超过2条
)

# 创建agent
agent = create_agent(
    model="deepseek-chat",
    middleware=[middleware],
    checkpointer=checkpointer,
)

config: RunnableConfig = {"configurable": {"thread_id": "1"}}
# 制造长会话历史
agent.invoke({"messages": "你好，我是虎哥."}, config)
agent.invoke({"messages": "我最喜欢的运动是乒乓"}, config)
agent.invoke({"messages": "我最喜欢的动物是猫猫"}, config)
# 测试效果
final_response = agent.invoke({"messages": "你还记得我吗？"}, config)


for message in final_response["messages"]:
    message.pretty_print()