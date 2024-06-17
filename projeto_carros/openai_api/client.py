'''
from openai import OpenAI

client = OpenAI(
    api_key = 'api-key' #colocar a api-key gerada

)

def get_car_ai_bio(model, brand, year):
    message= (colocar entre aspas triplas) Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas do modelo. Descreva especificações técnicas desse modelo.
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )
    return response.choices[0].message.content

'''