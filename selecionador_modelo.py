import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE=os.getenv('GEMINI_API_KEY')
genai.configure(api_key=CHAVE_API_GOOGLE)
modelo='gemini-2.5-flash'

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f'Erro: {e}')

system_prompt="""
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

user_prompt=carrega(r'C:\Users\raimu\Documents\GitHub\MeusProjetos\gemini\dados\lista_de_compras_100_clientes.csv')
print(f'Conteúdo lido: {user_prompt}')
flash_model=genai.GenerativeModel(f'models/{modelo}')
qnt_tokens=flash_model.count_tokens(user_prompt)

TOKEN_LIMIT=3000

if qnt_tokens.total_tokens>=TOKEN_LIMIT:
    modelo='gemini-2.5-pro'

print(f'O modelo selecionado foi: {modelo}')

llm=genai.GenerativeModel(
    model_name=modelo,
    system_instruction=system_prompt
)

response=llm.generate_content(user_prompt)
print(f'Respostas:\n{response.text}')