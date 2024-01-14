import openai

def get_correct_subtitles(subtitles, model="gpt-3.5-turbo"):
    msgIntro="Corrije ortograficamente el siguiente fichero de subtitulos. Añade comas, puntos y mayúsculas donde corresponda par aobtener un texto coherente. No modifiques el formato del fichero de subtitulos, solo el texto. Devuelve solamente el fichero de subtitulos actualizado: "
    finalMessage = msgIntro + subtitles
    messages = [{"role": "user", "content": finalMessage}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    return response.choices[0].message["content"]

def get_clean_subtitles(keyPoint, subtitles, model="gpt-3.5-turbo"):
    subtitles = get_correct_subtitles(subtitles)
    prompt="Imagina que eres un youtuber. Has creado un video cuyo tema es: " + keyPoint + ". Dado los subtitulos generados para el video borrador que has preparado: manten el saludo y despedida del locutor, si estan presentes. Elimina las secuencias o partes no relacionadas con el tema principal o que estén fuera de contexto. Manten el correcto formato srt del resultado:" + subtitles
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    with open('./resources/cleansubtitles.txt', 'w', encoding='utf-8') as output_file:
                output_file.write(response.choices[0].message["content"])

    return response.choices[0].message["content"]