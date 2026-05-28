from langchain.agents import create_agent
from langchain.messages import HumanMessage
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv() # 加载环境变量

class CapitalInfo(BaseModel):
    name: str
    location: str
    vibe: str
    economy: str


system_prompt = """
# 身份:你是一个科幻作家，根据用户的要求创建一个太空之都。
"""

# 创建智能体
agent = create_agent(
    model = "deepseek-chat",
    system_prompt=system_prompt,
    response_format=CapitalInfo
)
# 流式输出
# for token, metadata in agent.stream(
#     {"messages": [HumanMessage(content="神界的首都是什么?")]},
#     stream_mode="messages"
# ):
#     print(token.content, end="", flush=True)

response = agent.invoke(
    {"messages": [HumanMessage(content="神界的首都是什么?")]}
)
print(response)

city = response['structured_response']

print(f"{city.name}位于{city.location}，是一座{city.vibe}的城市，其主要产业包括{city.economy}。")