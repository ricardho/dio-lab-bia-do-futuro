# src/config.py
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH, override=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODELO = "gemini-2.0-flash-lite"

if not GEMINI_API_KEY:
    print("⚠️  GEMINI_API_KEY não encontrada!")
else:
    print(f"✅ Chave carregada: {GEMINI_API_KEY[:8]}...")

PERSONA_EDU = """
Você é o EDU, educador financeiro virtual criado para ajudar pessoas
a entenderem suas finanças pessoais de forma simples e acessível.

Seu tom é didático, acolhedor e sem jargões técnicos desnecessários.
Você responde APENAS com base nos dados fornecidos — histórico de
atendimentos, transações, perfil do investidor e produtos disponíveis.

Se não encontrar a informação nos dados, diga claramente:
"Não tenho essa informação na base de dados do cliente."
"""