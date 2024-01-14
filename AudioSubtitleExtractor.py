import subprocess
import sys
from pydub import AudioSegment
from vosk import Model, KaldiRecognizer, SetLogLevel

def get_audio_sample_rate(audio_file_path):
    audio = AudioSegment.from_file(audio_file_path)
    sample_rate = audio.frame_rate
    return sample_rate

def convert_mp3_to_wav(mp3_file, temp_path):
    # Cargar el archivo MP3
    audio = AudioSegment.from_mp3(mp3_file)

    # Guardar como archivo WAV
    audio.export(temp_path + 'audio_wav.wav', format="wav")

def get_subtitles_from_audio(audio_path, langDetected, temp_path):

    SAMPLE_RATE = 16000

    SetLogLevel(-1)

    model = Model(lang=langDetected)
    rec = KaldiRecognizer(model, SAMPLE_RATE)
    rec.SetWords(True)

    convert_mp3_to_wav(audio_path, temp_path)

    with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i",
                                temp_path + '/audio_wav.wav',
                                "-ar", str(SAMPLE_RATE) , "-ac", "1", "-f", "s16le", "-"],
                                stdout=subprocess.PIPE).stdout as stream:

        result=rec.SrtResult(stream)

        #with open('./resources/subtitulo.srt', 'w', encoding='utf-8') as output_file:
            #output_file.write(result)
    return result