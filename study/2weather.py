from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent
import os


# 加载环境变量
load_dotenv()
model=ChatOpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url=os.getenv("SILICONFLOW_BASE_URL"),
    model=os.getenv("MODEL_NAME"),
    temperature=0.5
)

@tool
def get_weather(city: str) -> str:
    """Get the weather for a city"""
    return f"{city}的天气是晴朗的"

agent = create_agent(model=model, tools=[get_weather])

print("调用大模型...")
print(agent.invoke({"messages": [{"role": "user", "content": "明天合肥天气怎么样？"}]}))
