import pandas as pd
from utils.validadores import documento_valido, nome_valido
from utils.excel_estilos import aplicar_destaques_excel

def analisar_e_destacar(arquivo_excel_entrada, nome_planilha, linha_cabecalho, arquivo_excel_saida):
    try:
        df = pd.read_excel(arquivo_excel_entrada, sheet_name=nome_planilha, header=linha_cabecalho)
    except FileNotFoundError:
        print(f"❌ ERRO: Arquivo '{arquivo_excel_entrada}' não encontrado.")
        return
    except Exception as e:
        print(f"❌ ERRO ao ler o arquivo Excel '{arquivo_excel_entrada}', planilha '{nome_planilha}': {e}")
        return

    # Limpa espaços extras dos nomes das colunas
    df.columns = df.columns.str.strip()
    
    df.dropna(how='all', inplace=True)

    colunas_chave_para_verificar_fim = ['Documento', 'Nome do Visitante']

    colunas_chave_existentes = [col for col in colunas_chave_para_verificar_fim if col in df.columns]

    if not df.empty and colunas_chave_existentes:
        
        tem_dados_nas_colunas_chave = df[colunas_chave_existentes].notna().any(axis=1)
        
        if tem_dados_nas_colunas_chave.any(): 
            
            ultimo_indice_com_dados = tem_dados_nas_colunas_chave[tem_dados_nas_colunas_chave].index[-1]
            
            df = df.loc[:ultimo_indice_com_dados]
            print(f"ℹ️ INFO: Dados processados até a linha de índice {ultimo_indice_com_dados} (após remoção de brancos no final).")
        else:
           
            print("⚠️ ATENÇÃO: Nenhuma linha com dados nas colunas chave ('Documento', 'Nome do Visitante') foi encontrada após a limpeza inicial.")
            print("           Verifique se a planilha contém os dados esperados ou se a linha do cabeçalho está correta.")
    elif df.empty:
        print("ℹ️ INFO: DataFrame ficou vazio após remover linhas totalmente em branco.")
    
    if df.empty:
        print("ℹ️ INFO: O DataFrame está vazio. Nenhuma análise ou destaque será realizado.")
        
        return


    #colunas  para validação
    colunas_necessarias = ['Documento', 'Nome do Visitante']
    colunas_processaveis = [] # Lista de colunas que existem e serão processadas

    for coluna_esperada in colunas_necessarias:
        if coluna_esperada in df.columns:
            colunas_processaveis.append(coluna_esperada)
        else:
            print(f"⚠️ ATENÇÃO: A coluna '{coluna_esperada}' não foi encontrada na planilha '{nome_planilha}'.")
            print(f"   Colunas disponíveis: {df.columns.tolist()}")
            print(f"   A validação para '{coluna_esperada}' será ignorada.")

    
    if 'Documento' in colunas_processaveis:
        df['Documento'] = df['Documento'].astype(str) # Garante que a coluna é string
        df['__Documento_Inválido__'] = ~df['Documento'].apply(documento_valido)
    else:
        # Se a coluna 'Documento' não existe, cria uma flag padrão
        df['__Documento_Inválido__'] = False 

    if 'Nome do Visitante' in colunas_processaveis:
        df['Nome do Visitante'] = df['Nome do Visitante'].astype(str) # Garante que a coluna é string
        df['__Nome_Inválido__'] = ~df['Nome do Visitante'].apply(nome_valido)
    else:
        # Se a coluna 'Nome do Visitante' não existe, cria uma flag padrão
        df['__Nome_Inválido__'] = False

    # Checa caso o df se torne vazio após manipulação
    if df.empty:
        print(f"✅ Planilha '{arquivo_excel_saida}' não foi modificada ou criada pois não havia dados para processar após validações.")
        return

#Depuração
    print("\n--- DEBUG: Amostra de Dados com Flags ---")
    colunas_debug = []
    
    # Adiciona colunas para debug apenas se elas e suas flags correspondentes existirem
    if 'Documento' in df.columns and '__Documento_Inválido__' in df.columns : colunas_debug.extend(['Documento', '__Documento_Inválido__'])
    if 'Nome do Visitante' in df.columns and '__Nome_Inválido__' in df.columns: colunas_debug.extend(['Nome do Visitante', '__Nome_Inválido__'])
    
    if colunas_debug and not df.empty:
        print(df[colunas_debug].head(10)) # Mostra as 10 primeiras linhas das colunas de debug
        if '__Documento_Inválido__' in df.columns:
            print(f"Total de documentos marcados como inválidos: {df['__Documento_Inválido__'].sum()}")
        if '__Nome_Inválido__' in df.columns:
            print(f"Total de nomes marcados como inválidos: {df['__Nome_Inválido__'].sum()}")
    elif not df.empty:
        print("Nenhuma coluna de validação principal ('Documento', 'Nome do Visitante') foi efetivamente processada para flags.")
    print("---------------------------------------\n")

#Salvar excel
    colunas_flags_para_remover = [flag_col for flag_col in ['__Documento_Inválido__', '__Nome_Inválido__'] if flag_col in df.columns]
    df_para_salvar = df.drop(columns=colunas_flags_para_remover, errors='ignore') # errors='ignore' para não falhar se coluna já foi removida ou não existe

    try:
        # abre o arquivo openxl 
        df_para_salvar.to_excel(arquivo_excel_saida, index=False)
        print(f"ℹ️ INFO: Planilha base (sem estilos) salva em '{arquivo_excel_saida}'. Iniciando aplicação de estilos.")
    except Exception as e:
        print(f"❌ ERRO ao salvar o arquivo Excel inicial '{arquivo_excel_saida}': {e}")
        return

    # Define quais colunas de dados devem ser destacadas e quais flags indicam invalidade
    mapeamento_destaques = {}
    if 'Documento' in colunas_processaveis: # Se a coluna 'Documento' foi processada
        mapeamento_destaques['Documento'] = '__Documento_Inválido__'
    if 'Nome do Visitante' in colunas_processaveis: # Se a coluna 'Nome do Visitante' foi processada
        mapeamento_destaques['Nome do Visitante'] = '__Nome_Inválido__'

    if mapeamento_destaques:
         aplicar_destaques_excel(arquivo_excel_saida, df.copy(), mapeamento_destaques)
    else:
        print("ℹ️ INFO: Nenhuma coluna configurada para destaque. Arquivo salvo sem estilos adicionais.")


#Entrada principal

if __name__ == '__main__':
    
    #Arquivo de entrada! 
    print("---- AUDITORIA DE PLANILHA -----")
    arquivo_de_entrada = input("Digite o nome do seu arquivo (coloque xlsx no final): ") # Coloque o nome do seu arquivo Excel aqui
    
    # Nome da planilha/aba ---- ALTERAR CASO NECESSARIO ___
    nome_da_planilha_no_arquivo = 'Plan1' 
    
    # Linha do cabeçalho -1 
    linha_onde_comeca_o_cabecalho = 2
    
    # Nome saida do arquivo
    arquivo_de_saida_final = input("Digite o nome de saida do arquivo com (xlsx no final): ") 

# chamada
    analisar_e_destacar(
        arquivo_de_entrada,
        nome_da_planilha_no_arquivo,
        linha_onde_comeca_o_cabecalho,
        arquivo_de_saida_final
    )
