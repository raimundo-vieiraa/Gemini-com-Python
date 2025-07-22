import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

MODELO_FLASH='gemini-2.5-flash'
MODELO_PRO='gemini-2.5-pro'

CUSTO_ENTRADA_FLASH = 1
CUSTO_SAIDA_FLASH = 2.5

CUSTO_ENTRADA_PRO = 2.5
CUSTO_SAIDA_PRO = 15

model_flash=genai.get_model(f'models/{MODELO_FLASH}')
limits_flash_models={
    'tokens_entrada' : model_flash.input_token_limit,
    'tokens_saida' : model_flash.output_token_limit
}

print(f'Limites do modelo flash são:\n{limits_flash_models}\n')

model_pro=genai.get_model(f'models/{MODELO_PRO}')
limits_pro_models={
    'tokens_entrada' : model_pro.input_token_limit,
    'tokens_saida' : model_pro.output_token_limit
}

print(f'Limites do modelo pro são:\n{limits_pro_models}\n')

llm_flash=genai.GenerativeModel(
    f'models/{MODELO_FLASH}'
)

number_tokens_flash=llm_flash.count_tokens('O que é uma calça de shopping?')
print(f'A quantidade de tokens do modelo flash é: {number_tokens_flash}\n')

llm_pro=genai.GenerativeModel(
    f'models/{MODELO_PRO}'
)

number_tokens_pro=llm_pro.count_tokens('O que é uma calça de shopping?')
print(f'A quantidade de tokens do modelo pro é: {number_tokens_pro}')

quantidade_tokens = llm_flash.count_tokens("O que é uma calça de shopping?")
print(f"A quantidade de tokens é: {quantidade_tokens}")

reply = llm_flash.generate_content("O que é uma calça de shopping?")
tokens_prompt = reply.usage_metadata.prompt_token_count
tokens_resposta = reply.usage_metadata.candidates_token_count

custo_total = (tokens_prompt * CUSTO_ENTRADA_FLASH) / 1000000 + (tokens_resposta * CUSTO_SAIDA_FLASH) / 1000000
print(f"Custo Total U$ Flash: ", custo_total)

custo_total = (tokens_prompt * CUSTO_ENTRADA_PRO) / 1000000 + (tokens_resposta * CUSTO_SAIDA_PRO) / 100.000
print(f"Custo Total U$ Pro: ", custo_total)

#Custo Total U$ Flash:  0.001575
#Custo Total U$ Pro:  93.900025