# St. Cecilia Catholic School Chatbot
# sccs_bot
import os
import PyPDF2
from chatlas import ChatOpenAI
from shiny.express import ui

# Load environment variables
key = os.getenv("OPENAI_API_KEY")
cal_path = "materials/25-26-Calendar.pdf"
handbook_path = "materials/St.-Cecilia-Family-Handbook2024.pdf"

# Function to extract text from a PDF file                          
def extract_text_from_pdf(pdf_path):                                
    text = ""                                                       
    with open(pdf_path, 'rb') as file:                              
        reader = PyPDF2.PdfReader(file)                             
        for page in reader.pages:                                   
            text += page.extract_text() + "\n"                      
    return text                                                     
                                                                    
# Specify the path to your PDF file                                 
cal_extracted = extract_text_from_pdf(cal_path) 
handbook_extracted = extract_text_from_pdf(handbook_path)              

# Create the chat client
chat_client = ChatOpenAI(
    api_key=key,
    model="gpt-4o-mini",
    system_prompt=f"""
    Please review the following calendar and family handbook and use them to answer questions. When you provide an answer, please provide the specific location(s) in the calendar or handbook where you found the answer. If you are unable to answer a question after reviewing the calendar and handbook, please do not make up an answer – simply say "I do not see that information in the calendar or handbook".

    We have a daughter that is going to start in Pre-K 4 in August 2025.

    <cal_extracted>
    {cal_extracted}
    </cal_extracted>

    <handbook_extracted>
    {handbook_extracted}
    </handbook_extracted>
    """
)

# Set some Shiny page options
ui.page_opts(
    title="SCCS Bot",
    fillable=True,
    fillable_mobile=True,
)

# Create and display a Shiny chat component
chat = ui.Chat(
    id="chat",
    messages=["Hello! I can review the SCCS 2025-2026 calendar (updated February 10, 2025) and the SCCS Family Handbook (updated September 2024). How can I help you today?"],
)
chat.ui()

# Store chat state in the url when an "assistant" response occurs
chat.enable_bookmarking(chat_client, bookmark_store="url")

# Generate a response when the user submits a message
@chat.on_user_submit
async def handle_user_input(user_input: str):
    response = await chat_client.stream_async(user_input)
    await chat.append_message_stream(response)
