from dotenv import load_dotenv
from langchain.chat_models import init_chat_model# 初始化大模型
import os

load_dotenv() # 加载环境变量

#让langchain自动寻找去找模型配置
model1=init_chat_model(model="deepseek-v4-flash")
print(type(model1))

#langchain不支持的模型提供商
model2=init_chat_model(
    model=os.getenv("MODEL_NAME"),
    model_provider="openai",#因为硅基流动langchain不支持，所以用openai的provider,硅基流动兼容openai的api
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url=os.getenv("SILICONFLOW_BASE_URL"),
)
print(type(model2))

print("调用deepseek-ai/DeepSeek-V4-Flash模型...")
for chunk in model2.stream("你好你是谁"):
    print(chunk.content, end="", flush=True)
