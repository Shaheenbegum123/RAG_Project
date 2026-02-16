import os
import warnings
warnings.filterwarnings("ignore")

os.environ["USER_AGENT"] = "rag-app"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# 1. LOAD MULTIPLE PDFs

pdf_files = [
    "Books/Building Machine Learning Systems with Python.pdf",
    "Books/Introduction to Machine Learning with Python ( PDFDrive.com )-min.pdf",
    "Books/Practical Machine Learning with Python.pdf"
]
docs = []

print("Loading PDFs...")

for pdf in pdf_files:
    if os.path.exists(pdf):
        loader = PyPDFLoader(pdf)
        docs.extend(loader.load())
        print(f"Loaded: {pdf}")
    else:
        print(f"File not found: {pdf}")

print(f"\nTotal pages loaded: {len(docs)}")

# 2. SPLIT INTO CHUNKS

print("\nSplitting documents...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=40
)

chunks = text_splitter.split_documents(docs)

print(f"Total chunks created: {len(chunks)}")

# 3. LOAD EMBEDDING MODEL

print("\nLoading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4. CREATE / LOAD CHROMA DATABASE

db_path = "chroma_db"

if os.path.exists(db_path):

    print("\nLoading saved Chroma database (FAST)...")

    vector_store = Chroma(
        persist_directory=db_path,
        embedding_function=embeddings
    )

else:

    print("\nCreating Chroma database (First time only, may take few minutes)...")

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=db_path
    )

    vector_store.persist()

    print("Chroma database saved successfully!")


print("\nRAG System Ready!")


# 5. QUERY LOOP

while True:

    query = input("\nEnter your query (type exit to stop): ").strip()

    if query.lower() == "exit":

        print("Exiting system...")
        break


    if query == "":

        print("Please enter a valid query.")
        continue


    print("\nSearching...\n")


    results = vector_store.similarity_search(query, k=12)


    # Remove duplicates
    seen = set()

    main_points = []


    for doc in results:

        text = doc.page_content.strip()

        first_sentence = text.split(".")[0].strip()


        if first_sentence not in seen and len(first_sentence) > 20:

            seen.add(first_sentence)

            main_points.append(first_sentence)


        if len(main_points) == 8:

            break


    print("Main Points:\n")


    if len(main_points) == 0:

        print("No relevant information found.")

    else:

        for i, point in enumerate(main_points, 1):

            print(f"{i}. {point}.")


    print("\nDone.")
