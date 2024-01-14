import os
from datetime import datetime
from moviepy.video.io.VideoFileClip import VideoFileClip

def toms(tiempo_str):
    tiempo_obj = datetime.strptime(tiempo_str, "%H:%M:%S.%f")
    segundos_totales = tiempo_obj.hour * 3600 + tiempo_obj.minute * 60 + tiempo_obj.second + tiempo_obj.microsecond / 1e6
    return f"{segundos_totales:.6f}"

def extract_clips_from_video(video_file_path, timestmaps, output_folder):
    for idx, line in enumerate(timestmaps):
        start_time, end_time = map(str.strip, line.split(';'))
        output_clip_path = f"{output_folder}/clip_{idx + 1}.mp4"

        #clip = VideoFileClip(video_file_path).subclip(start_time, end_time)
        clip = VideoFileClip(video_file_path).subclip(toms(start_time), toms(end_time))
        clip.write_videofile(output_clip_path, codec="libx264", audio_codec="aac")

def cut_cilps_from_sequencies(timestamps, video_path, temp_folter):
    output_folder = temp_folter + "/clips"
    if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    extract_clips_from_video(video_path, timestamps, output_folder)
    return output_folder