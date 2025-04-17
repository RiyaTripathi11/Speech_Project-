from langchain_groq import ChatGroq
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from config import GROQ_API_KEY

# Initialize Groq Chat Model
chat_model = ChatGroq(model_name="mixtral-8x7b-32768", api_key=GROQ_API_KEY)

def chat_with_ai(user_input):
    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content=user_input)
    ]
    response = chat_model.invoke(messages)
    return response.content
