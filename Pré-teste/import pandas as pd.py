import pandas as pd
import numpy as np

# ==============================================================================
# 1. DADOS HISTÓRICOS (Extraídos do Memórias de Cálculo - Backtest / Risco.csv)
#    Usados diretamente no código devido a problemas na leitura do CSV original.
# ==============================================================================
# Retornos Brutos Anuais (Decimais)
data = {
    'Ano': list(range(1995, 2018)),
    'PE': [0.24, 0.30, 0.29, 0.17, 0.39, 0.04, -0.11, -0.04, 0.24, 0.29, 0.27, 0.38, 0.25, -0.29, 0.17, 0.21, 0.07, 0.14, 0.21, 0.10, 0.09, 0.11, 0.22],
    'RV': [0.37, 0.23, 0.33, 0.28, 0.21, -0.09, 0.08, -0.22, 0.28, 0.11, 0.05, 0.16, 0.05, -0.37, 0.26, 0.15, 0.02, 0.16, 0.32, 0.14, 0.01, 0.12, 0.22], 
    'RF': [0.23, 0.01, 0.10, 0.15, -0.08, 0.17, 0.06, 0.15, 0.00, 0.04, 0.03, 0.02, 0.10, 0.20, -0.11, 0.08, 0.16, 0.03, -0.09, 0.11, 0.01, 0.01, 0.03]
}
df_returns = pd.DataFrame(data)

# Tratamento de dados: Imputando o retorno faltante de RV (2001) com a média histórica
mean_rv = df_returns['RV'].mean()
df_returns['RV'].fillna(mean_rv, inplace=True)

# Cálculo das estatísticas históricas
historical_means = df_returns[['PE', 'RV', 'RF']].mean()
historical_stds = df_returns[['PE', 'RV', 'RF']].std()
correlation_matrix = df_returns[['PE', 'RV', 'RF']].corr()

# Matriz de Covariância e Decomposição de Cholesky
cov_matrix = correlation_matrix * np.outer(historical_stds, historical_stds)
L = np.linalg.cholesky(cov_matrix)

# ==============================================================================
# 2. FUNÇÃO GENERALIZADA DE MONTE CARLO
# ==============================================================================
def run_monte_carlo(horizonte, target_liquido, gasto_rate, alocacao):
    """Roda a simulação de Monte Carlo para um cenário específico."""
    
    N_SIMULATIONS = 10000
    INITIAL_PORTFOLIO = 20_000_000.00
    TAX_RATE = 0.15
    
    final_portfolios = []
    success_count = 0

    for _ in range(N_SIMULATIONS):
        portfolio = INITIAL_PORTFOLIO
        
        # Gera retornos aleatórios e correlacionados [PE, RV, RF]
        random_returns = np.random.normal(0, 1, (horizonte, 3)) @ L.T + historical_means.values
        
        for year in range(horizonte):
            
            ret_PE_bruto = random_returns[year, 0]
            ret_RV_bruto = random_returns[year, 1]
            ret_RF_bruto = random_returns[year, 2]
            
            # 1. Gasto Anual
            gasto_anual = portfolio * gasto_rate
            
            # 2. Imposto sobre RF (ANUAL)
            ret_RF_liquido = ret_RF_bruto * (1 - TAX_RATE)

            # 3. Imposto sobre PE (A cada 7 ANOS)
            tax_PE_rate = TAX_RATE if (year + 1) % 7 == 0 else 0.0
            ret_PE_liquido = ret_PE_bruto * (1 - tax_PE_rate)

            # 4. RV é Bruto (Acumulação)
            ret_RV_liquido = ret_RV_bruto

            # 5. Retorno Ponderado Líquido
            retorno_ponderado = (
                alocacao[0] * ret_PE_liquido +
                alocacao[1] * ret_RV_liquido +
                alocacao[2] * ret_RF_liquido
            )
            
            # 6. Atualiza o Patrimônio
            portfolio = portfolio * (1 + retorno_ponderado) - gasto_anual
            
            if portfolio <= 0:
                portfolio = 0
                break
                
        final_portfolios.append(portfolio)
        
        # Checa sucesso (Comparação com o TARGET LÍQUIDO)
        if portfolio >= target_liquido:
            success_count += 1

    # 7. Análise de Resultados
    success_rate = success_count / N_SIMULATIONS
    percentile_10 = np.percentile(final_portfolios, 10)
    
    return success_rate, percentile_10

# ==============================================================================
# 3. DEFINIÇÃO E EXECUÇÃO DOS CENÁRIOS (6 CENÁRIOS)
# ==============================================================================
# Targets líquidos ajustados para o horizonte estendido (Base: 3,02% a.a.)
TARGETS_ESTENDIDOS = {
    70: 153_005_105.10, # 70 anos de projeção a 3,02%
    60: 114_444_245.80, # 60 anos de projeção a 3,02%
    25: 42_076_443.34   # 25 anos de projeção a 3,02%
}

# Cenários de Simulação (Alocação: [PE, RV, RF])
# PE está na posição 0, RV na 1, RF na 2
cenarios = [
    # Fase 1: 30 Anos (Alocação: 50% PE, 40% RV, 10% RF)
    {'fase': 'Fase 1 (Base)', 'horizonte': 60, 'gasto': 0.02, 'target': 114_444_245.80, 'alocacao': np.array([0.25, 0.70, 0.05])},
    {'fase': 'Fase 1 (Estendido)', 'horizonte': 70, 'gasto': 0.02, 'target': TARGETS_ESTENDIDOS[70], 'alocacao': np.array([0.25, 0.70, 0.05])},
    
    # Fase 2: 40 Anos (Alocação: 35% PE, 45% RV, 20% RF)
    {'fase': 'Fase 2 (Base)', 'horizonte': 50, 'gasto': 0.04, 'target': 84_992_089.42, 'alocacao': np.array([0.25, 0.675, 0.075])},
    {'fase': 'Fase 2 (Estendido)', 'horizonte': 60, 'gasto': 0.04, 'target': TARGETS_ESTENDIDOS[60], 'alocacao': np.array([0.25, 0.675, 0.075])},
    
    # Fase 3: 75 Anos (Alocação: 20% PE, 35% RV, 45% RF)
    {'fase': 'Fase 3 (Base)', 'horizonte': 15, 'gasto': 0.05, 'target': 30_000_218.09, 'alocacao': np.array([0.25, 0.40, 0.35])},
    {'fase': 'Fase 3 (Estendido)', 'horizonte': 25, 'gasto': 0.05, 'target': TARGETS_ESTENDIDOS[25], 'alocacao': np.array([0.25, 0.40, 0.35])},
]

resultados_mc = []

for cenario in cenarios:
    taxa_sucesso, p10 = run_monte_carlo(
        cenario['horizonte'], 
        cenario['target'], 
        cenario['gasto'], 
        cenario['alocacao']
    )
    
    # Cálculo do Retorno Ponderado Bruto (para a Memória de Cálculo)
    ret_PE, ret_RV, ret_RF = 0.12, 0.07, 0.04 # Retornos Brutos das premissas
    retorno_bruto_ponderado = (
        cenario['alocacao'][0] * ret_PE +
        cenario['alocacao'][1] * ret_RV +
        cenario['alocacao'][2] * ret_RF
    )

    resultados_mc.append({
        'Fase': cenario['fase'],
        'Horizonte': f"{cenario['horizonte']} anos",
        'Retorno Bruto Ponderado': retorno_bruto_ponderado,
        'Target Líquido': cenario['target'],
        'Taxa de Sucesso (MC)': taxa_sucesso,
        'Patrimônio no 10º Percentil (P10)': p10,
    })

# ==============================================================================
# 4. TABULAÇÃO FINAL (Memória de Cálculo)
# ==============================================================================

df_final = pd.DataFrame(resultados_mc)

# Formatando para a Memória de Cálculo
df_final['Retorno Bruto Ponderado'] = df_final['Retorno Bruto Ponderado'].map('{:.2%}'.format)
df_final['Target Líquido'] = df_final['Target Líquido'].map('US$ {:,.2f}'.format)
df_final['Taxa de Sucesso (MC)'] = df_final['Taxa de Sucesso (MC)'].map('{:.2%}'.format)
df_final['Patrimônio no 10º Percentil (P10)'] = df_final['Patrimônio no 10º Percentil (P10)'].map('US$ {:,.2f}'.format)

pd.set_option('display.max_columns', None)  # Garante que todas as colunas sejam mostradas
pd.set_option('display.width', None)        # Garante que não quebre as colunas na visualização
print(df_final)