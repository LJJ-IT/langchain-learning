from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os
load_dotenv() # 加载环境变量

model= init_chat_model(
    model=os.getenv("QWEN_MODEL_NAME"),
    model_provider="openai",
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url=os.getenv("SILICONFLOW_BASE_URL"),
)

@tool
def get_weather(city: str) -> str:
    """Get the weather for a city"""
    return f"{city}的天气是晴朗的"

agent = create_agent(model=model, tools=[get_weather])
message=HumanMessage([
    {"type": "text", "text": "请描述以下图片的内容"},
    {"type": "image", "url": "https://tse3-mm.cn.bing.net/th/id/OIP-C.BTnQOgzj11V54KJ6VR31sgHaE7?o=7rm=3&rs=1&pid=ImgDetMain&o=7&rm=3"}
])
print("调用大模型...")
stream = agent.stream(
    {"messages": [message]},
    stream_mode="messages"
)

for chunk,metadata in stream:
    if chunk.content:
        print(chunk.content, end="", flush=True)


# response = agent.invoke(
#     {"messages": [
#         SystemMessage("你是一个天气助手,请使用工具来回答用户问题"),
#         HumanMessage("你好我是虎哥"),
#         AIMessage("你好虎哥，很高兴认识你"),
#         HumanMessage("合肥今天天气如何"),
#         ]}
# )
#更加漂亮的打印响应
