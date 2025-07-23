import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE=os.getenv('GEMINI_API_KEY')
genai.configure(api_key=CHAVE_API_GOOGLE)
MODELO='gemini-2.5-flash'

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo,'r') as arquivo:
            dados=arquivo.read()
            return dados
    except IOError as e:
        print(f'Erro: {e}')

def salva(nome_do_arquivo,conteudo):
    try:
        with open(nome_do_arquivo,'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f'Erro ao salvar arquivo: {e}')

system_prompt=f"""
        Você é um analisador de sentimentos de avaliações de produtos.
        Escreva um parágrafo com até 50 palavras resumindo as avaliações e
        depois atribua qual o sentimento geral para o produto.
        Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

        # Formato de Saída

        Nome do Produto:
        Resumo das Avaliações:
        Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
        Ponto fortes: lista com três bullets
        Pontos fracos: lista com três bullets
    """

product_name=''
user_prompt=carrega(f'dados/avaliacoes-{product_name}.txt')

print(f'Iniciando a análise de sentimentos do produto:\n{product_name}')

llm=genai.GenerativeModel(
    model_name=MODELO,
    system_instruction=system_prompt
)

response=llm.generate_content(user_prompt)
response_text=response.text

salva(f'dados/response-{product_name}', response_text)