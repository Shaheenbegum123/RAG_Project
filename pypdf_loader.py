from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Books/dance.pdf")
docs = loader.load()
print(len(docs))
print(docs[0].metadata)