import openai
from config import OPENAI_API_KEY, PERSONA, DEFAULT_LANGUAGE
from langdetect import detect

openai.api_key = OPENAI_API_KEY

def chat_with_openai(prompt, language=None):
    if not language:
        language = DEFAULT_LANGUAGE
    # Prefix prompt with persona and language info
    prompt = f"[Persona: {PERSONA} | Language: {language}]\n" + prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].text.strip()
