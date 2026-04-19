from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import List
from config import OLLAMA_CONFIG 

class AIResponse(BaseModel):
    summary: str = Field(description="A concise summary of the user's input.")
    sentiment:int = Field(description="Sentiment score of the user's input, ranging from 0 (negative) to 1 (positive).")
    response: str = Field(description="The AI-generated response based on the user's input.")

json_parser=JsonOutputParser(pydantic_object=List[AIResponse])

def init_model():
    model = OllamaLLM(
        model=OLLAMA_CONFIG["model"],
        base_url=OLLAMA_CONFIG["base_url"],
        temperature=OLLAMA_CONFIG["temperature"],
        max_tokens=OLLAMA_CONFIG["max_tokens"]
    )
    return model
llm = init_model()

# in the assitant: we have given instructions to respond only in JSON format with specific keys. This is important because it allows us to easily parse the response and extract the relevant information. By using a structured format like JSON, we can ensure that the response is consistent and can be easily processed by our application, else it can be blank with string response which can be done by removing json parser and changing the template to respond in string format.
template=PromptTemplate(
    template="""
    System: {system_prompt}
    User: {user_prompt}
    Assistant: Respond only in JSON with keys:
      summary, sentiment, response 
    """,
    input_variables=["system_prompt", "user_prompt"]
    )

def gen_ai_reponse(system_prompt,user_prompt):
    chain= template | llm | json_parser
    return chain.invoke({
        "system_prompt": system_prompt,
        "user_prompt": user_prompt
        })

def generate_response(system_prompt, user_prompt):
   return gen_ai_reponse(system_prompt, user_prompt)