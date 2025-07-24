# GeminiLab

Este projeto demonstra o uso da API Gemini (Google Generative AI) aplicada a tarefas de análise de sentimentos, manipulação de texto e avaliação de tokens. É uma iniciativa prática para aprofundar conhecimentos em inteligência artificial generativa e explorar o potencial da API da Google.

## 🔍 Funcionalidades

- Análise de sentimentos com IA generativa
- Seleção automatizada de modelos do Gemini
- Contador de tokens por prompt
- Organização modular do código

## 🧠 Tecnologias utilizadas

- Python 3.12+
- Biblioteca `google-generativeai`
- API Gemini da Google

## 🛠️ Como executar

1. Clone o repositório:
   
   ```bash
   git clone https://github.com/raimundo-vieiraa/gemini
   cd gemini
   
2. Crie e ative o ambiente virtual:
   
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
3. Instale as dependências:
   
   ```bash
   pip install -r requirements.txt
4. Configure sua chave da API Gemini em um arquivo .env:
   
   ```bash
   GEMINI_API_KEY=sua-chave-aqui
5. Execute os módulos desejados:
    
   ```bash
   python analisador_sentimentos.py
   ```
   ```bash
   python categorizador.py
   ```
   ```bash
   python contador_token.py
   ```
   ```bash
   python selecionador_modelo.py
   ```
   ```bash
   python main.py

## 📂 Estrutura do Projeto
📁 gemini/

 ├── .venv/                    # Ambiente virtual (Escondido no ````.gitignore````)
 
 ├── dados/                    # Armazenamento de textos ou entradas
 
 ├── analisador_sentimentos.py
 
 ├── contador_token.py
 
 ├── selecionador_modelo.py
 
 ├── requirements.txt
 
 ├── README.md

## 💡 Objetivo
Explorar, aprender e demonstrar competências práticas com LLMs e a API do Gemini, visando projetos reais, desafios de IA generativa e aplicações comerciais.

### Projeto desenvolvido como parte de estudo no curso da Alura sobre Google Gemini, com adaptações e organização próprias, realizadas por Raimundo Ruan Alexandre Vieira. Estudante de Engenharia de Software (UNICEPLAC).

   
