import srt

def extract_timestamps_from_srt(srt_text):
    subtitles = list(srt.parse(srt_text))

    timestamps = []

    while subtitles:
    # Extraer y eliminar el elemento en la posición 0
        current_subtitle = subtitles.pop(0)
        this_section_start = current_subtitle.start
        this_section_end = current_subtitle.end
        while subtitles and subtitles[0].start == this_section_end:
            next_subtitle = subtitles.pop(0)
            this_section_end = next_subtitle.end

        timestamps.append(f"{this_section_start};{this_section_end}")
    
    return timestamps

def save_timestamps_to_file(timestamps, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for timestamp in timestamps:
            file.write(f"{timestamp}\n")

def calculate_sequencies_from_subtitles(srt_text):
    ts = extract_timestamps_from_srt(srt_text)
    save_timestamps_to_file(ts, "./resources/marcas_de_tiempo.txt")
    return ts