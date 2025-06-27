import chatlas as ctl
from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv("OPENAI_API_KEY")

# Optional (but recommended) model and system_prompt
chat = ctl.ChatOpenAI(
    model="gpt-4o-mini",
    api_key=key,
    system_prompt=f"""
    Please review the following calendar and answer questions about it.
    <cal>
    {cal.json}
    </cal>
    """
)

cal = ctl.content_pdf_file("materials/25-26-Calendar.pdf")
cal.parse_obj

# Send user prompt to the model for a response.
rockets_goat = chat.chat("Who is the best Houston Rockets player of all time?")
rockets_goat.content

chat.chat("How many days is St. Cecilia's closed from August to December 2025?")
chat.chat("what does is St. Cecilia's closed in August 2025?", cal)
chat.chat("Please use the calendar to answer all questions.", cal)

# https://posit-dev.github.io/chatlas/get-started/system-prompt.html

