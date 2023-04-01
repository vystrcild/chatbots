from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

messages = [[
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="Translate this sentence from English to French. I love programming."),
    AIMessage(content="Why???"),
    HumanMessage(content="Why not?"),
    AIMessage(content="Because I hate you!"),
    HumanMessage(content="Why? :("),
]]


def chat_model(temperature=0.4, model_name="gpt-3.5-turbo", messages=[]):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    chat = ChatOpenAI(temperature=temperature, openai_api_key=OPENAI_API_KEY, model_name=model_name)
    response = chat.generate(messages)
    response_message_object = response.generations[0][0].message
    response_text = response.generations[0][0].text
    total_tokens = response.llm_output["token_usage"]["total_tokens"]

    return {
        "response_message_object": response_message_object,
        "response_text": response_text,
        "total_tokens": total_tokens
    }

def generate_chat_reply(text):
    reply = {
        "user": "OpenAI Chat",
        "type": "ai",
        "text": str(text.lstrip()),
        "datetime": str(datetime.now()),
        "room": "chat_test"
    }
    return reply