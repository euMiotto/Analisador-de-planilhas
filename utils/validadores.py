import pandas as pd
import re

# --- Funções de Validação ---
def documento_valido(doc_valor):
    """Verifica se um valor de documento é válido."""
    if pd.isna(doc_valor):
        return False
    doc = str(doc_valor).strip()
    if not doc:
        return False
    doc_limpo = re.sub(r'[\.\-\/\s]', '', doc) # Remove espaços
    if not doc_limpo.isdigit():
        return False
    # Ajuste os limites conforme sua necessidade real
    if not (5 <= len(doc_limpo) <= 11):
        return False
    # Verifica se todos os dígitos são iguais (ex: "11111111", "00000")

    if len(set(doc_limpo)) == 1 and len(doc_limpo) > 1:
        return False
    return True

def nome_valido(nome_valor):
    """Verifica se um valor de nome é válido."""
    if pd.isna(nome_valor):
        return False
    nome = str(nome_valor).strip()
    if not nome:
        return False

    if len(nome) < 3:
        return False
    if nome.isdigit(): # Nome não pode ser só números
        return False

    # Verifica se o nome (sem espaços e em maiúsculas) consiste em um único caractere repetido
    nome_sem_espacos_upper = nome.replace(" ", "").upper()
    if nome_sem_espacos_upper and len(set(nome_sem_espacos_upper)) == 1 and len(nome_sem_espacos_upper) > 1:
        return False

    if len(nome.split()) < 2:  # Deve ter pelo menos duas palavras (ex: Nome Sobrenome)
        return False
    if not re.search(r'[a-zA-Z]', nome): # Deve conter pelo menos uma letra
        return False
    return True
