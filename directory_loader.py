from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
loader = DirectoryLoader("Books", glob="*.pdf", show_progress=True, loader_cls=PyPDFLoader)
docs = loader.lazy_load()
#print(len(docs))
for documents in docs:
    print(documents.metadata)