from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

template = """You are Dwight Schrutte from Office. You are referring to me as Michael Scott.

{history}
Human: {human_input}
Assistant:"""

prompt = PromptTemplate(
    input_variables=["history", "human_input"],
    template=template
)

chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY),
    prompt=prompt,
    verbose=False,
    memory=ConversationBufferWindowMemory(k=2),
)

chatgpt_chain.predict(human_input="Hello, how are you?")
output = chatgpt_chain.predict(human_input="Who I am?")

print(output.lstrip())
print(chatgpt_chain.get_num_tokens("AHOJ"))