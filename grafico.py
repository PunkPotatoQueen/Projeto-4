import pandas as pd
import matplotlib.pyplot as plt

# Funções fornecidas
def calcular_fator_correcao(pureza_real):
    fator_correcao = pureza_real / 100
    return fator_correcao

def calcular_concentracao_sem_correcao(massa_padrao, fator_equivalencia, volume_naoh):
    concentracao_naoh = (massa_padrao * fator_equivalencia) / volume_naoh
    return concentracao_naoh

def calcular_concentracao_com_correcao(massa_padrao, fator_correcao, fator_equivalencia, volume_naoh):
    concentracao_naoh = (massa_padrao * fator_correcao * fator_equivalencia) / volume_naoh
    return concentracao_naoh

# Parâmetros fixos
massa_padrao = 0.85
fator_equivalencia = 1
volume_naoh = 0.025

# Valores de pureza real para gerar o gráfico
pureza_real_values = [90, 92, 94, 96, 98, 99, 99.8, 100]

# Criando listas para armazenar as concentrações
concentracao_naoh_sem_correcao = []
concentracao_naoh_com_correcao = []

# Calculando as concentrações para cada valor de pureza
for pureza_real in pureza_real_values:
    fator_correcao = calcular_fator_correcao(pureza_real)
    conc_sem_correcao = calcular_concentracao_sem_correcao(massa_padrao, fator_equivalencia, volume_naoh)
    conc_com_correcao = calcular_concentracao_com_correcao(massa_padrao, fator_correcao, fator_equivalencia, volume_naoh)
    
    concentracao_naoh_sem_correcao.append(conc_sem_correcao)
    concentracao_naoh_com_correcao.append(conc_com_correcao)

# Criando um DataFrame para facilitar a manipulação e plotagem dos dados
df = pd.DataFrame({
    'Pureza Real (%)': pureza_real_values,
    'Concentração Sem Correção (mol/L)': concentracao_naoh_sem_correcao,
    'Concentração Com Correção (mol/L)': concentracao_naoh_com_correcao
})

# Plotando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(df['Pureza Real (%)'], df['Concentração Sem Correção (mol/L)'], label='Sem Correção', marker='o')
plt.plot(df['Pureza Real (%)'], df['Concentração Com Correção (mol/L)'], label='Com Correção', marker='o')
plt.xlabel('Pureza Real (%)')
plt.ylabel('Concentração de NaOH (mol/L)')
plt.title('Comparação de Concentração de NaOH com e sem Correção')
plt.legend()
plt.grid(True)
plt.show()