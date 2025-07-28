from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import openai

# Cargar variables de entorno desde .env
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Verificación de la API Key
if not API_KEY:
    raise RuntimeError("OPENAI_API_KEY no está definida en el archivo .env")

# Inicializar cliente OpenAI (v1.x)
client = openai.OpenAI(api_key=API_KEY)

# Inicializar FastAPI
app = FastAPI()

# Modelo de entrada
class TextInput(BaseModel):
    text: str

@app.post("/summarize")
async def summarize(input_data: TextInput):
    text = input_data.text.strip()

    if not text:
        return {"error": "No se proporcionó texto."}
    if len(text) < 50:
        return {"error": "El texto es demasiado corto para resumir (mínimo 50 caracteres)."}

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Cambiar por "gpt-4" si tenés acceso
            messages=[
                {
                    "role": "user",
                    "content": f"""Actuá como un asistente experto en lenguaje natural. Leé atentamente el siguiente texto y generá un resumen claro, objetivo y coherente en español. El resumen debe tener entre 3 y 5 frases completas, mantener las ideas principales, evitar repetir conceptos y no incluir información irrelevante ni inventada:

Texto a resumir:
\"\"\"
{text}
\"\"\"
"""
                }
            ],
            max_tokens=400,
            temperature=0.5
        )

        summary = response.choices[0].message.content
        return {"summary": summary}


    # Errores generales
    except Exception as e:
        return {"error": f"Error inesperado: {str(e)}"}
