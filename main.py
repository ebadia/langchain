from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import argparse
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--language", type=str, default="python")
parser.add_argument("--task", type=str, default="print numbers 1 to 10")
args = parser.parse_args()

llm = OpenAI()

code_prompt = PromptTemplate(
    template="Write a short {language} function that will {task}",
    input_variables=["language", "task"],
)
code_chain = LLMChain(llm=llm, prompt=code_prompt)

result = code_chain({"language": args.language, "task": args.task})

# result = llm("Escribe un poema muy corto")
print(result["text"])
