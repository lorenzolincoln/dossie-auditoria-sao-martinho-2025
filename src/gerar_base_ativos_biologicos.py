import pandas as pd
import numpy as np

def gerar_base_ativos_biologicos(n_linhas=500000, seed=42):
    # Fixar semente para reprodutibilidade do dossiê
    np.random.seed(seed)
    
    # 1. Parâmetros Reais Extraídos das Fontes
    # Saldo real Nível 3 em 31 de março de 2025 (em milhares de R$, convertido para R$ nominal)
    saldo_contabil_alvo = 1405729000  
    taxa_desconto_base = 0.1028 # Taxa de desconto de 10,28% ao ano em 2025 
    
    print(f"Iniciando geração da base com {n_linhas} registros...")
    
    # 2. Geração das variáveis base (Simulado)
    id_talhao = np.arange(1, n_linhas + 1)
    cod_fazenda = np.random.choice(['FAZ-SM-MATRIZ', 'FAZ-SM-FILIAL1', 'FAZ-SM-FILIAL2', 'FAZ-SM-FILIAL3'], size=n_linhas)
    estagio_corte = np.random.choice(['Cana-planta', 'Soca 1', 'Soca 2', 'Soca 3', 'Soca 4'], size=n_linhas)
    
    # Áreas entre 0.5 e 2.0 hectares por talhão fragmentado
    area_ha = np.random.uniform(0.5, 2.0, size=n_linhas) 
    
    # Produtividade variando conforme o estágio de corte (TCH)
    produtividade_estimada = np.random.normal(loc=85.0, scale=10.0, size=n_linhas)
    
    # 3. Geração do Valor Justo Base e Distribuição Proporcional
    # Para garantir que a soma bata EXATAMENTE com R$ 1.405.729.000
    valor_base_bruto = area_ha * produtividade_estimada
    fator_proporcao = saldo_contabil_alvo / valor_base_bruto.sum()
    valor_justo_correto = valor_base_bruto * fator_proporcao
    
    # 4. Construção do DataFrame
    df = pd.DataFrame({
        'id_talhao': id_talhao,
        'cod_fazenda': cod_fazenda,
        'area_ha': np.round(area_ha, 2),
        'estagio_corte': estagio_corte,
        'produtividade_estimada': np.round(produtividade_estimada, 2),
        'taxa_desconto_aplicada': taxa_desconto_base,
        'valor_justo_contabil': np.round(valor_justo_correto, 2),
        'anomalia_inserida': 'Sem anomalia'
    })
    
    # Ajuste fino de arredondamento para o saldo bater exatamente no centavo
    diferenca = saldo_contabil_alvo - df['valor_justo_contabil'].sum()
    df.loc[0, 'valor_justo_contabil'] += diferenca
    df['valor_justo_contabil'] = np.round(df['valor_justo_contabil'], 2)
    
    # 5. Inserção de Erros/Inconsistências Propositais para Teste de Auditoria
    # Erro A: Área negativa (Falha de sistema/Controle Interno)
    idx_erro_a = np.random.choice(df.index, size=200, replace=False)
    df.loc[idx_erro_a, 'area_ha'] = df.loc[idx_erro_a, 'area_ha'] * -1
    df.loc[idx_erro_a, 'anomalia_inserida'] = 'Área Negativa'
    
    # Erro B: Taxa de desconto divergente (Risco de avaliação inadequada)
    idx_erro_b = np.random.choice(df[df['anomalia_inserida'] == 'Sem anomalia'].index, size=350, replace=False)
    df.loc[idx_erro_b, 'taxa_desconto_aplicada'] = 0.0514 # Metade da taxa oficial
    df.loc[idx_erro_b, 'valor_justo_contabil'] = df.loc[idx_erro_b, 'valor_justo_contabil'] * 1.5 
    df.loc[idx_erro_b, 'anomalia_inserida'] = 'Taxa Desconto Incorreta e Superavaliação'
    
    return df

# Execução
df_ativos = gerar_base_ativos_biologicos(n_linhas=500000)
saldo_gerado = df_ativos['valor_justo_contabil'].sum()

print(f"Base sintética gerada com sucesso!")
print(f"Total de Linhas: {len(df_ativos)}")
print(f"Saldo Contábil Total Gerado (R$): {saldo_gerado:,.2f}")
print(f"O saldo confere com a evidência pública (1.405.729.000,00)? {'Sim' if round(saldo_gerado, 2) == 1405729000.00 else 'Não'}")

# Exportações simuladas para o repositório GitHub
# df_ativos.to_csv('gabarito_ativos_biologicos_2025.csv', index=False)
# df_ativos.drop(columns=['anomalia_inserida']).to_csv('cliente_ativos_biologicos_2025.csv', index=False)
