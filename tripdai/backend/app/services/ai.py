import os
import requests
import openai

# Lectura de claves desde variables de entorno
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
HUGGINGFACE_MODEL = os.getenv("HUGGINGFACE_MODEL", "google/flan-t5-small")

if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY


def generar_prompt(preferences: dict) -> str:
    """Construye un prompt enriquecido para el modelo."""
    intereses = ', '.join(preferences.get("interests", []))
    presupuesto = preferences.get("budget", "medio")
    dias = preferences.get("duration_days", "?")
    tipo_viajero = preferences.get("traveler_type", "mochilero")

    return (
        f"Planifica un itinerario de {dias} días para un viajero tipo {tipo_viajero} "
        f"con intereses en {intereses}, y presupuesto {presupuesto} euros. "
        f"Recomienda lugares menos turísticos, comida local, transporte barato, "
        f"alojamientos asequibles y actividades gratuitas o únicas. "
        f"Escribe de forma amigable y clara."
    )


def usar_huggingface(prompt: str) -> str:
    """Llama a la API de Hugging Face para generar texto."""
    if not HUGGINGFACE_TOKEN:
        raise ValueError("No se encontró HUGGINGFACE_API_TOKEN en el entorno.")

    url = f"https://api-inference.huggingface.co/models/{HUGGINGFACE_MODEL}"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}
    payload = {"inputs": prompt}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list):
            return data[0].get("generated_text", str(data[0])).strip()
        elif isinstance(data, dict) and "error" in data:
            raise RuntimeError(f"Error Hugging Face: {data['error']}")
        return str(data)
    except Exception as e:
        raise RuntimeError(f"Error en Hugging Face: {e}")


def usar_openai(prompt: str) -> str:
    """Llama a la API de OpenAI (text-davinci-003)."""
    if not OPENAI_API_KEY:
        raise ValueError("No se encontró OPENAI_API_KEY en el entorno.")

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=800,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        raise RuntimeError(f"Error en OpenAI: {e}")


def generate_itinerary_text(preferences: dict) -> str:
    """
    Genera un itinerario viajero usando IA (Hugging Face o OpenAI como fallback).
    """
    prompt = generar_prompt(preferences)

    # 1) Intentar Hugging Face
    if HUGGINGFACE_TOKEN:
        try:
            return usar_huggingface(prompt)
        except Exception as e:
            print(f"[INFO] Falló Hugging Face: {e}")

    # 2) Fallback a OpenAI
    if OPENAI_API_KEY:
        try:
            return usar_openai(prompt)
        except Exception as e:
            print(f"[INFO] Falló OpenAI: {e}")

    # 3) Ningún proveedor disponible
    raise RuntimeError(
        "No se pudo generar texto: necesitas configurar HUGGINGFACE_API_TOKEN o OPENAI_API_KEY"
    )
