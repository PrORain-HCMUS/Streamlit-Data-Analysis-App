from langchain_community.llms.groq import Groq

llm = Groq(model="llama3-8b-8192", api_key="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")
print(llm.invoke("Say hello in Vietnamese"))
