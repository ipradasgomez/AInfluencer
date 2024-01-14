import whisper

def transcribe(audio_path):
    model = whisper.load_model("base")

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio_path)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    langDetected = max(probs, key=probs.get)
    print(f"Detected language: {langDetected}")

    # decode the audio
    options = whisper.DecodingOptions(fp16 = False)
    result = whisper.decode(model, mel, options)

    # print the recognized text
    return langDetected, result.text

    #with open('./tmp/transcription.txt', 'w', encoding='utf-8') as archivo:
    #    archivo.write(result.text)
