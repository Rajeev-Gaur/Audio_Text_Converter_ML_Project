from gtts import gTTS

def text_to_audio(text, output_file):
    # Specify the language as Hindi
    tts = gTTS(text=text, lang='hi')
    # Save the audio file
    tts.save(output_file)
    print(f"Audio saved as {output_file}")

if __name__ == "__main__":
    hindi_text = """एक बार की बात है, एक गरीब औरत थी जिसका नाम आइशा था। वह एक छोटे से गाँव में अपने माता-पिता और छोटे भाई-बहनों के साथ रहती थी।
उसके पिता एक किसान थे, लेकिन खेत बहुत उपजाऊ नहीं था, और वे अक्सर किसी तरह का गुजारा करते थे।आइशा एक बुद्धिमान और जिज्ञासु लड़की थी। वह अपने आसपास की दुनिया के बारे में जानना पसंद करती थी।
वह एक वैज्ञानिक बनने का सपना देखती थी, लेकिन वह जानती थी कि अपने परिवार की वित्तीय स्थिति के कारण उसे अपना लक्ष्य हासिल करना मुश्किल होगा !
एक दिन, आइशा के पिता बीमार पड़ गए। वह काम करने में असमर्थ थे, और परिवार की आय और भी कम हो गई। आइशा को अपने परिवार की मदद करने के लिए स्कूल छोड़ना पड़ा।"""  # Replace with your Hindi text
    output_file = "output_hindi.mp3"  # Output MP3 filename
    text_to_audio(hindi_text, output_file)
