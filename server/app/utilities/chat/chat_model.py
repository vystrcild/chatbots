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

class Chat:
    def __init__(self, temperature=0.4, model_name="gpt-3.5-turbo"):
        self.temperature = temperature
        self.model_name = model_name
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

    def prepare_chat_input(self, db_messages):
        chat_input = []
        for message in reversed(db_messages):
            if message.type == "human":
                message_object = HumanMessage(content=message.text)
            elif message.type == "ai":
                message_object = AIMessage(content=message.text)
            else:
                message_object = SystemMessage(content=message.text)
            chat_input.append(message_object)

        return chat_input

    def get_response(self, messages=[]):
        chat = ChatOpenAI(temperature=self.temperature, openai_api_key=self.openai_api_key, model_name=self.model_name)
        response = chat.generate(messages)
        response_message_object = response.generations[0][0].message
        response_text = response.generations[0][0].text
        total_tokens = response.llm_output["token_usage"]["total_tokens"]

        return {
            "response_message_object": response_message_object,
            "response_text": response_text,
            "total_tokens": total_tokens
        }

    def generate_chat_reply(self, text):
        reply = {
            "user": "OpenAI Chat",
            "type": "ai",
            "text": str(text.lstrip()),
            "datetime": str(datetime.now()),
            "room": "chat_test"
        }
        return reply