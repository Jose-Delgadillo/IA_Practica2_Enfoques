"""
Prácticas de Inteligencia Artificial  
Reconocimiento del Habla: Uso de SpeechRecognition
"""

import speech_recognition as sr

# =======================
# Reconocimiento de Voz
# =======================
def reconocimiento_de_voz():
    # Inicializar el reconocedor de voz
    reconocedor = sr.Recognizer()

    # Usar el micrófono como fuente de entrada
    with sr.Microphone() as fuente:
        print("Ajustando ruido ambiente. Por favor espere...")
        # Ajusta el ruido ambiente (para eliminar ruidos de fondo)
        reconocedor.adjust_for_ambient_noise(fuente, duration=1)

        print("Por favor, hable ahora...")
        # Escucha la entrada de voz desde el micrófono
        audio = reconocedor.listen(fuente)

    try:
        # Usar Google Web Speech API para convertir la voz en texto
        print("Reconociendo...")
        texto = reconocedor.recognize_google(audio, language="es-ES")  # Idioma: Español
        print(f"Texto reconocido: {texto}")
    except sr.UnknownValueError:
        print("Lo siento, no pude entender lo que dijiste.")
    except sr.RequestError as e:
        print(f"Hubo un error con el servicio de reconocimiento de Google: {e}")

# Ejecutar el reconocimiento de voz
reconocimiento_de_voz()
