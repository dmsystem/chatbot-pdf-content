# Chatbot Baseado em Conteúdo de PDFs

Este projeto consiste na criação de um **chatbot interativo** que responde perguntas baseadas no conteúdo de arquivos PDF. Utilizando técnicas de **IA generativa**, **embeddings** e **buscas vetorizadas**, o sistema consegue entender e processar informações de documentos científicos, oferecendo respostas contextuais e relevantes para o usuário.

## Visão Geral

Com o aumento do volume de documentos e informações, especialmente em estudos e pesquisas acadêmicas, torna-se cada vez mais difícil organizar e acessar dados relevantes. Este projeto busca resolver esse problema utilizando IA para criar um sistema inteligente de busca e interação com os dados contidos em PDFs.

O projeto foi desenvolvido para estudantes que precisam lidar com grandes volumes de artigos, papers ou outros documentos, permitindo que extraiam informações de maneira eficiente.

## Objetivos

- Carregar arquivos PDF contendo informações relevantes.
- Criar um sistema de busca vetorial para indexar e recuperar informações dos PDFs.
- Utilizar inteligência artificial para gerar respostas com base no conteúdo dos documentos.
- Implementar um chatbot interativo para responder perguntas contextuais.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **PyMuPDF**: Biblioteca para extração de texto de arquivos PDF.
- **Sentence-Transformers**: Para gerar embeddings de texto e realizar buscas semânticas.
- **FAISS**: Biblioteca de busca vetorial para indexação e recuperação de dados.
- **Streamlit**: Para a criação de uma interface interativa para o chatbot.

## Como Rodar o Projeto

### 1. Clonando o Repositório

Primeiro, clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/SEU_USUARIO/chatbot-pdf-content.git
cd chatbot-pdf-content
