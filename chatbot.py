import os
import streamlit as st
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Carregar os PDFs da pasta 'inputs'
def load_pdfs(pdf_folder):
    pdf_texts = []
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            with fitz.open(os.path.join(pdf_folder, filename)) as doc:
                text = ''
                for page in doc:
                    text += page.get_text()
                pdf_texts.append(text)
    return pdf_texts

# Processar o texto dos PDFs e gerar embeddings
def create_embeddings(texts, model):
    embeddings = model.encode(texts, convert_to_tensor=True)
    return embeddings

# Indexar os embeddings usando FAISS
def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings.cpu().numpy())
    return index

# Função para buscar a resposta mais relevante
def search(query, index, model, texts):
    query_embedding = model.encode([query], convert_to_tensor=True)
    D, I = index.search(query_embedding.cpu().numpy(), k=1)
    best_match = I[0][0]
    return texts[best_match]

# Configurações do Streamlit
st.title("Chatbot Baseado em Conteúdo de PDFs")
st.write("Pergunte algo sobre o conteúdo dos PDFs carregados.")

# Carregar os PDFs e processar
pdf_folder = 'inputs'
pdf_texts = load_pdfs(pdf_folder)

# Criar embeddings com o modelo pré-treinado
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
embeddings = create_embeddings(pdf_texts, model)

# Criar o índice FAISS
index = create_faiss_index(embeddings)

# Chatbot: Receber pergunta do usuário
user_input = st.text_input("Pergunta:")

# Buscar a resposta e exibir
if user_input:
    response = search(user_input, index, model, pdf_texts)
    st.write("Resposta:")
    st.write(response)
