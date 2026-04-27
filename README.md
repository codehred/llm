# Tutor Virtual Inteligente - Proyecto LLM

Este proyecto implementa un asistente educativo avanzado utilizando modelos de lenguaje de gran escala (LLM). Está diseñado para actuar como un facilitador pedagógico que guía a los estudiantes en temas de ingeniería y computación.

## Características
- **Multimodelo:** Soporte para Google Gemini 2.0+ y OpenAI GPT.
- **Pedagogía Activa:** Configurado para no dar respuestas directas, sino pistas y explicaciones.
- **Memoria de Sesión:** Mantiene el contexto de la conversación.
- **Seguridad:** Manejo de credenciales mediante variables de entorno.

## Instalación

1. Crear un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS


2. Instalar dependencias:
    ```bash
    pip install -r requirements.txt

3. Configurar el archivo .env:
Crea un archivo .env basado en .env.example y añade tu GEMINI_API_KEY.

## Uso
- Ejecuta el programa con:
    ```bash
    python app.py


## Requisitos
Python 3.9+

google-genai

python-dotenv

openai (opcional)