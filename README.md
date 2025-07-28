# 🧠 Proyecto de Desarrollo IA - Resumen Automático de Textos

Este proyecto consiste en una API desarrollada en Python que permite recibir un texto largo mediante un endpoint y devolver un resumen breve del mismo, utilizando la API de inteligencia artificial de OpenAI (ChatGPT).

El objetivo es aplicar técnicas de procesamiento automático de lenguaje natural y conocimientos de desarrollo backend, como la creación de endpoints, integración con APIs externas y manejo de datos.

---

## ⚙️ Tecnologías utilizadas

- **Python 3.10+**
- **FastAPI** – Framework web para construir la API
- **Uvicorn** – Servidor ASGI para ejecutar FastAPI
- **OpenAI API** – Modelo GPT-3.5-Turbo para generar resúmenes
- **python-dotenv** – Para cargar claves desde archivos `.env`

---

## 🚀 Instrucciones para ejecutar el proyecto localmente

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/resumen-ia.git
cd resumen-ia
```

### 2. Crear y configurar el entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear un archivo `.env` con tu clave API

En el directorio raíz del proyecto, crear un archivo llamado `.env` y agregar tu clave:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Ejecutar el servidor

```bash
uvicorn main:app --reload
```

### 6. Probar la API

Abrí tu navegador y entrá en:

```
http://127.0.0.1:8000/docs
```

Allí vas a encontrar la documentación interactiva y podrás probar el endpoint `/summarize`.


## 🔐 Instrucciones para obtener la clave API de OpenAI

1. Crear una cuenta en [https://platform.openai.com](https://platform.openai.com)
2. Ir a [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
3. Hacer clic en "Create new secret key"
4. Copiar la clave (formato `sk-...`) y pegarla en tu archivo `.env` como:

   ```
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
   ```

## 📌 Endpoint disponible

### `POST /summarize`

**Descripción:** Recibe un texto largo y devuelve un resumen de entre 3 y 5 frases.

**Prompt:** Actuá como un asistente experto en lenguaje natural. Leé atentamente el siguiente texto y generá un resumen claro, objetivo y coherente en español. El resumen debe tener entre 3 y 5 frases completas, mantener las ideas principales, evitar repetir conceptos y no incluir información irrelevante ni inventada.

**Body JSON:**

```json
{
  "text": "Texto largo en español que querés resumir..."
}
```

**Respuesta exitosa:**

```json
{
  "summary": "Este es el resumen generado por la IA."
}
```

---

## 💬 Autor

Desarrollado como parte del Proyecto de Desarrollo IA – Versión Avanzada.
