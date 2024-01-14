import os, shutil
from AudioExtractor import extract_audio
from AudioTranscriber import transcribe
from TextKeyPointDetector import get_key_point_from_subtitles
from AudioSubtitleExtractor import get_subtitles_from_audio
from SubtitleCleaner import get_clean_subtitles
from SrtSequencyExtractor import calculate_sequencies_from_subtitles
from ClipCutter import cut_cilps_from_sequencies
from VideoEnsamblator import ensamble_video
import openai

def prerequisites(temp_path):
    openai.api_key = 'YOUR KEY'
    if not os.path.exists(temp_path):
        # Crear el directorio si no existe
        os.makedirs(temp_path)

def main():
    temp_path = './temp/'
    # Ruta del video de entrada
    video_input_path = './resources/video_original.mp4'
    # Ruta donde se guardará el archivo de audio extraído
    audio_output_path = temp_path + 'audio_extraido.mp3'
    video_output = './resources/video_final.mp4'
    intro_path = './resources/intro/intro.mp4'

    prerequisites(temp_path)

    #Extraemos el audio del video
    extract_audio(video_input_path, audio_output_path)

    #Transcribimos el audio para ayudarnos a detectar el tema
    langDetected, transcription = transcribe(audio_output_path)

    #Obtenemos los subtitulos del audio
    subtitles = get_subtitles_from_audio(audio_output_path, langDetected, temp_path)

    #Extraemos la idea principal
    topic = get_key_point_from_subtitles(subtitles)

    #Limpiamos los subtitulos
    srt_subtitles_clean=get_clean_subtitles(topic, subtitles)

    #Calculamos la secuencia de video a mantener
    timestamps = calculate_sequencies_from_subtitles(srt_subtitles_clean)

    #Cortamos los clips que deben mantenerse
    clips_folder = cut_cilps_from_sequencies(timestamps, video_input_path, temp_path)

    #Reensamblamos el video
    ensamble_video(video_output, clips_folder, intro_path)

    #cleanDirectory(temp_path)

def cleanDirectory(path):
    try:
        shutil.rmtree(path)
        print(f"La carpeta {path} y su contenido han sido eliminados.")
    except Exception as e:
        print(f"No se pudo eliminar la carpeta {path}. Error: {e}")


if __name__ == "__main__":
    main()