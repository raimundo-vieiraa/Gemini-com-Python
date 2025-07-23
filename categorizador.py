import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE=os.getenv('GEMINI_API_KEY')
genai.configure(api_key=CHAVE_API_GOOGLE)
MODELO_ESCOLHIDO='gemini-2.5-flash'
def categorizar_produto(nome_produto,list_of_possible_categories):
    prompt_system=f"""
        Você é um categorizador de produtos.
        Você deve assumir as categorias presentes na lista abaixo.
        # Lista de Categorias Válidas
        {list_of_possible_categories.split(",")}
        # Formato da Saída
        Produto: Nome do Produto
        Categoria: apresente a categoria do produto
        # Exemplo de Saída
        Produto: Escova elétrica com recarga solar
        Categoria: Eletrônicos Verdes
        """
    llm=genai.GenerativeModel(
        model_name=MODELO_ESCOLHIDO,
        system_instruction=prompt_system
    )
    
    resposta=llm.generate_content(nome_produto)
    return resposta.text

def main():
    list_of_possible_categories='Eletrônicos Verdes,Moda Sustentável,Produtos de Limpeza,Alimentos Orgânicos, Produtos de Higienes Sustentáveis'
    
    produto=input('Informe o produto que você deseja classificar: ')

    while produto!="":
        print(f'Resposta:\n{categorizar_produto(produto,list_of_possible_categories)}')
        produto=input('Informe o produto que você deseja classificar: ')
if __name__=="__main__":
    main()