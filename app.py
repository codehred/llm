import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

class TutorIA:
    def __init__(self):
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.gemini_key = os.getenv("GEMINI_API_KEY")
        self.modo = None
        self.client = None
        self.chat = None
        self.historial_openai = []
        self.sys_instruct = "Eres un Tutor de Ingeniería. Guía al alumno sin dar la respuesta directa."

        if self.openai_key:
            from openai import OpenAI
            self.modo = "OPENAI"
            self.client = OpenAI(api_key=self.openai_key)
            print("💡 Usando motor de OpenAI")
        elif self.gemini_key:
            self.modo = "GEMINI"
            self.client = genai.Client(api_key=self.gemini_key)
            self.chat = self.client.chats.create(
                model="gemini-2.5-flash", 
                config=types.GenerateContentConfig(system_instruction=self.sys_instruct)
            )
            print("💡 Usando motor de Google Gemini")
        else:
            print("❌ Error: No se encontró ninguna API KEY en .env")
            exit()

    def responder(self, mensaje):
        if self.modo == "GEMINI":
            response = self.chat.send_message(mensaje)
            return response.text
        
        elif self.modo == "OPENAI":
            self.historial_openai.append({"role": "user", "content": mensaje})
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": self.sys_instruct}, *self.historial_openai]
            )
            texto = response.choices[0].message.content
            self.historial_openai.append({"role": "assistant", "content": texto})
            return texto

def iniciar_tutor():
    tutor = TutorIA()
    
    print("\n--- 🎓 Tutor Virtual Activo ---")
    print("(Escribe 'salir' para finalizar)")
    
    while True:
        try:
            user_input = input("\nEstudiante: ")
            if user_input.lower() in ["salir", "exit", "quit"]: 
                break
            
            if not user_input.strip(): continue

            respuesta = tutor.responder(user_input)
            print(f"\nTutor: {respuesta}")
            
        except Exception as e:
            print(f"\n❌ Error al procesar: {e}")

if __name__ == "__main__":
    iniciar_tutor()