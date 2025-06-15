import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

groq_llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))

# Define the prompt template
with open("prompts/field_mapper_prompt.txt", "r") as f:
    prompt_template_str = f.read()

prompt = PromptTemplate(
    input_variables=["label"],
    template=prompt_template_str
)

# Create the LLMChain
field_mapper_chain = LLMChain(llm=groq_llm, prompt=prompt)

def map_field_label_to_key(label_text: str) -> str:
    """
    Uses Groq-hosted LLaMA to map a field label to a known structured profile key.
    """
    result = field_mapper_chain.invoke({"label": label_text})
    return result["text"].strip().lower()

