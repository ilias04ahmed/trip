# Orquestador de llamadas a OpenAI u otro modelo de IA
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_itinerary_text(preferences: dict) -> str:
    prompt = (
        f"Crear un itinerario de {preferences['duration_days']} días "
        f"para un viajero con intereses {preferences['interests']} "
        f"y presupuesto {preferences['budget']}. "
    )
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=800
    )
    return response.choices[0].text.strip()
