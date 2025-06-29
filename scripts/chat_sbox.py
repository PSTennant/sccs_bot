import chatlas as ctl
import os
import PyPDF2

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

# Optional (but recommended) model and system_prompt
chat = ctl.ChatOpenAI(
    model="gpt-4o-mini",
    api_key=key,
    system_prompt=f"""
    Please review the following calendar and family handbook and use them to answer questions. When you provide an answer, please provide the specific location(s) in the calendar or handbook where you found the answer. If you are unable to answer a question after reviewing the calendar and handbook, please do not make up an answer – simply say "I do not see that information in the calendar or handbook".

    We have a daughter that is going to start in Pre-K 4 in August 2025.

    <cal_extracted>
    {cal_extracted}
    </cal_extracted>

    <handbook_extracted>
    {handbook_extracted}
    </handbook_extracted>
    """)

# Run the chatbot
chat.app()
