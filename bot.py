from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import requests
import openai

app = Flask(__name__)

# Configurar OpenAI API key
openai.api_key = "tu_clave_api_openai"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    # Obtener datos del webhook
    incoming_msg = request.values.get('Body', '').lower()
    media_url = request.values.get('MediaUrl0')  # URL de la nota de voz
    media_type = request.values.get('MediaContentType0')  # Tipo de archivo

    resp = MessagingResponse()

    if media_url and 'audio' in media_type:
        # Descargar la nota de voz
        audio_response = requests.get(media_url)

        # Guardar la nota de voz en el servidor temporalmente
        audio_file = "nota_de_voz.ogg"
        with open(audio_file, "wb") as f:
            f.write(audio_response.content)

        # Convertir la nota de voz a texto
        transcribed_text = convert_audio_to_text(audio_file)

        if transcribed_text:
            # Enviar el texto a la API de ChatGPT
            response_text = send_to_chatgpt(transcribed_text)

            # Responder al usuario
            resp.message(response_text)
        else:
            resp.message("No pude procesar la nota de voz.")
    else:
        resp.message("Por favor, envíame una nota de voz.")

    return str(resp)

def convert_audio_to_text(audio_file):
    # Aquí puedes usar pydub o speech_recognition para convertir el audio a texto
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language="es-ES")  # Puedes cambiar el idioma según sea necesario
        return text
    except Exception as e:
        print(f"Error al transcribir el audio: {e}")
        return None

def send_to_chatgpt(prompt):
    # Configurar y enviar el prompt a la API de OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True)
