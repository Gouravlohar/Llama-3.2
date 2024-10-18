from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

def main():
    print("LLama 3.2 ChatBot")

    template = """Question: {question}

    Answer: Let's think step by step."""

    prompt = ChatPromptTemplate.from_template(template)

    model = OllamaLLM(model="llama3.2")

    chain = prompt | model

    while True:
        question = input("Enter your question here (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break

        print("Thinking...")
        answer = chain.invoke({"question": question})
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()