from chatlas import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv("OPENAI_API_KEY")

# Optional (but recommended) model and system_prompt
chat = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=key,
    system_prompt="You are a helpful assistant.",
)

# Send user prompt to the model for a response.
chat.chat("Who is the best Houston Rockets player of all time?")
