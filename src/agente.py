# src/agente.py
import json
import csv
import os
from pathlib import Path
from google import genai
from config import GEMINI_API_KEY, MODELO, PERSONA_EDU

# Cliente novo da biblioteca google-genai
client = genai.Client(api_key=GEMINI_API_KEY)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def ler_csv(nome_arquivo: str) -> str:
    caminho = DATA_DIR / nome_arquivo
    linhas = []
    with open(caminho, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            linhas.append(", ".join(f"{k}: {v}" for k, v in row.items()))
    return "\n".join(linhas)


def ler_json(nome_arquivo: str) -> str:
    caminho = DATA_DIR / nome_arquivo
    with open(caminho, encoding="utf-8") as f:
        dados = json.load(f)
    return json.dumps(dados, ensure_ascii=False, indent=2)


def montar_base_conhecimento() -> str:
    base = []
    base.append("=== HISTÓRICO DE ATENDIMENTOS ===")
    base.append(ler_csv("historico_atendimento.csv"))
    base.append("=== TRANSAÇÕES DO CLIENTE ===")
    base.append(ler_csv("transacoes.csv"))
    base.append("=== PERFIL DO INVESTIDOR ===")
    base.append(ler_json("perfil_investidor.json"))
    base.append("=== PRODUTOS FINANCEIROS DISPONÍVEIS ===")
    base.append(ler_json("produtos_financeiros.json"))
    return "\n\n".join(base)


def perguntar_edu(pergunta: str, historico: list = None) -> str:
    base = montar_base_conhecimento()

    historico_txt = ""
    if historico:
        for msg in historico[-6:]:
            role = "Usuário" if msg["role"] == "user" else "EDU"
            historico_txt += f"{role}: {msg['content']}\n"

    prompt = f"""
{PERSONA_EDU}

BASE DE CONHECIMENTO (dados reais do cliente):
{base}

HISTÓRICO RECENTE DA CONVERSA:
{historico_txt}

PERGUNTA ATUAL:
{pergunta}

Responda de forma clara e didática com base apenas nos dados acima.
"""

    response = client.models.generate_content(
        model=MODELO,
        contents=prompt
    )
    return response.text