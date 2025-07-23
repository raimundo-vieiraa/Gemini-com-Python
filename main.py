import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE=os.getenv('GEMINI_API_KEY')
genai.configure(api_key=CHAVE_API_GOOGLE)
MODELO_ESCOLHIDO='gemini-2.5-flash'

prompt_system='Liste apenas os nomes dos produtos, e ofereça uma breve descrição.'

configure_model={
    "temperature" : 2.0,
    "top_p" : 0.9,
    "top_k" : 64,
    "max_output_tokens" : 8192,
    "response_mime_type" : "text/plain"
}

llm=genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=prompt_system,
    generation_config=configure_model
)
pergunta='Liste três produtos de moda sustentável para ir ao shopping.'
resposta=llm.generate_content(pergunta)
print(f'A resposta gerada para a pergunta é:{resposta.text}')