import openai

def get_key_point_from_subtitles(text, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": 'En una frase corta y concisa de no mas de 15 palabrsa, dime el tema más importante del que se habla en los siguientes subtitulos:' + text}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    messages = [{"role": "user", "content": 'Dime, sin enumerarlas, entre 1 y 3 puntos clave, usando frases de no mas de 10 palabras, relacionados con el tema: ' + response.choices[0].message["content"] + '; que se mencionen en los subtitulos:' + text}]
    response2 = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    #with open('./resources/keypoint.txt', 'w', encoding='utf-8') as output_file:
    #            output_file.write(response.choices[0].message["content"])
    
    #with open('./resources/keypoint2.txt', 'w', encoding='utf-8') as output_file:
    #            output_file.write(response2.choices[0].message["content"])
    
    return response.choices[0].message["content"] + response2.choices[0].message["content"]