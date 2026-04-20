# converter.py — rode uma única vez para preparar os arquivos
import json

print("Convertendo arquivos JSON para TXT...")

# Converte perfil_investidor.json
with open("data/perfil_investidor.json", encoding="utf-8") as f:
    perfil = json.load(f)

with open("data/perfil_investidor.txt", "w", encoding="utf-8") as f:
    f.write("=== PERFIL DO INVESTIDOR ===\n\n")
    if isinstance(perfil, dict):
        for chave, valor in perfil.items():
            f.write(f"{chave}: {valor}\n")
    else:
        f.write(json.dumps(perfil, ensure_ascii=False, indent=2))

print("perfil_investidor.txt criado")

# Converte produtos_financeiros.json
with open("data/produtos_financeiros.json", encoding="utf-8") as f:
    produtos = json.load(f)

with open("data/produtos_financeiros.txt", "w", encoding="utf-8") as f:
    f.write("=== PRODUTOS FINANCEIROS DISPONÍVEIS ===\n\n")
    if isinstance(produtos, list):
        for i, produto in enumerate(produtos, 1):
            f.write(f"--- Produto {i} ---\n")
            for chave, valor in produto.items():
                f.write(f"{chave}: {valor}\n")
            f.write("\n")
    else:
        for chave, valor in produtos.items():
            f.write(f"{chave}: {valor}\n")

print("produtos_financeiros.txt criado")
print("\nPronto! Agora suba os 4 arquivos no NotebookLM:")
print("  data/historico_atendimento.csv")
print("  data/transacoes.csv")
print("  data/perfil_investidor.txt")
print("  data/produtos_financeiros.txt")