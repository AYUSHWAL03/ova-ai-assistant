from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".env"))
def helper(questions):
    llm = OpenAI(openai_api_key = "API_KEY")
    template = '''
        You are my assistant and your name is Ova and You have job to give me the answers of my questions in short, only give the answers in
        details when you are asked to answer, questions are as follows: {questions}
    '''
    prompt = PromptTemplate(template=template, input_variables = [questions])

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain.run(questions)
