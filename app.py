import os
from dotenv import load_dotenv

# Cargamos variables de entorno
load_dotenv()

def configurar_tutor():
    openai_key = os.getenv("OPENAI_API_KEY")
    gemini_key = os.getenv("GEMINI_API_KEY")

    if openai_key:
        from openai import OpenAI
        print("💡 Usando motor de OpenAI")
        client = OpenAI(api_key=openai_key)
        
        def responder(mensaje, historial):
            # Historial para OpenAI
            historial.append({"role": "user", "content": mensaje})
            response = client.chat.completions.create(
                model="gpt-3.5-turbo", # O gpt-4o si el maestro tiene crédito
                messages=[
                    {"role": "system", "content": "Eres un Tutor de Ingeniería. Guía al alumno sin dar la respuesta directa."},
                    *historial
                ]
            )
            texto = response.choices[0].message.content
            historial.append({"role": "assistant", "content": texto})
            return texto
        return responder

    elif gemini_key:
        import google.generativeai as genai
        print("💡 Usando motor de Google Gemini")
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction="Eres un Tutor de Ingeniería. Guía al alumno sin dar la respuesta directa."
        )
        chat = model.start_chat(history=[])
        
        def responder(mensaje, _):
            response = chat.send_message(mensaje)
            return response.text
        return responder

    else:
        print("❌ Error: No se encontró OPENAI_API_KEY ni GEMINI_API_KEY en el archivo .env")
        exit()

def iniciar_tutor():
    responder_fn = configurar_tutor()
    historial = [] # Para OpenAI
    
    print("\n--- 🎓 Tutor Virtual Activo ---")
    while True:
        user_input = input("\nEstudiante: ")
        if user_input.lower() in ["salir", "exit"]: break
        
        respuesta = responder_fn(user_input, historial)
        print(f"\nTutor: {respuesta}")

if __name__ == "__main__":
    iniciar_tutor()