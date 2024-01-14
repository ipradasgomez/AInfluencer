from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def combine_clips(clips_folder, output_path, intro_path):
    clips = []
    
    # Lista todos los archivos en el directorio
    files = os.listdir(clips_folder)

    # Filtra solo los archivos, excluyendo directorios
    files = [file for file in files if os.path.isfile(os.path.join(clips_folder, file))]

    try:
        clip = VideoFileClip(intro_path)
        clips.append(clip)
    except Exception:
        pass

    # Lee cada clip en la carpeta y agrega a la lista
    for i in range(1, len(files) + 1):
        clip_path = os.path.join(clips_folder, f"clip_{i}.mp4")
        try:
            clip = VideoFileClip(clip_path)
            clips.append(clip)
        except FileNotFoundError:
            break

    # Combina los clips en un solo video
    final_clip = concatenate_videoclips(clips, method="compose")

    # Guarda el video combinado
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

def ensamble_video(video_output, clips_folder, intro_path):
    combine_clips(clips_folder, video_output, intro_path)
    print(f"Video combinado guardado en: {video_output}")