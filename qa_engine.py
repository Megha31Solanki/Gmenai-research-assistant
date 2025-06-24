def answer_question(text, question):
    from langchain.chains.qa_with_sources import load_qa_with_sources_chain
    from langchain.vectorstores import FAISS
    from langchain.embeddings.openai import OpenAIEmbeddings
    from langchain.text_splitter import CharacterTextSplitter

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = splitter.split_text(text)
    vectorstore = FAISS.from_texts(texts, OpenAIEmbeddings())
    docs = vectorstore.similarity_search(question)
    return docs[0].page_content, "Justified from top match"
