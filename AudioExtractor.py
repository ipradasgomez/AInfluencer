from moviepy.editor import VideoFileClip

def extract_audio(video_path, audio_output_path):
    # Carga el video
    video = VideoFileClip(video_path)
    
    # Extrae el audio del video
    audio = video.audio
    
    # Guarda el audio extraído en un archivo de audio
    audio.write_audiofile(audio_output_path)
    
    # Cierra el video y el audio
    video.close()
    audio.close()