import time

def calcular_fator_correcao(pureza_real):
    fator_correcao = pureza_real / 100
    return fator_correcao

def calcular_concentracao_sem_correcao(massa_padrao, fator_equivalencia, volume_naoh):
    concentracao_naoh = (massa_padrao * fator_equivalencia) / volume_naoh
    return concentracao_naoh

def calcular_concentracao_com_correcao(massa_padrao, fator_correcao, fator_equivalencia, volume_naoh):
    concentracao_naoh = (massa_padrao * calcular_fator_correcao(fator_correcao) * fator_equivalencia) / volume_naoh
    return concentracao_naoh

def calcular_concentracao_molar(massa_soluto, massa_molar, volume_solucao):
    concentracao = massa_soluto / (massa_molar * volume_solucao)
    return concentracao


#     #Utilizando exemplos padrão
#     massa_padrao = 0.85
#     fator_equivalencia = 1
#     volume_naoh = 0.025

#     concentracao_naoh_sem_correcao = calcular_concentracao_sem_correcao(massa_padrao, fator_equivalencia, volume_naoh)
#     print(f"Concentração de NaOH sem correção: {concentracao_naoh_sem_correcao:.4f} mol/L")

#     #Exemplo de pureza real usando o padrão primário de KHP (99.8)
#     pureza_real = 99.8
#     fator_correcao = calcular_fator_correcao(pureza_real)
#     concentracao_naoh_com_correcao = calcular_concentracao_com_correcao(massa_padrao, fator_correcao, fator_equivalencia, volume_naoh)
#     print(f"Concentração de NaOH com correção: {concentracao_naoh_com_correcao:.4f} mol/L")

#     # Exemplo de uso de concentração molar
#     massa_soluto = 1.0 # g
#     massa_molar = 204.22 # g/mol para KHP
#     volume_solucao = 0.025 # L

#     concentracao_molar = calcular_concentracao_molar(massa_soluto, massa_molar, volume_solucao)
#     print(f"Concentração molar: {concentracao_molar:.4f} mol/L")


#     print(f"O tempo de execução das formulas  foi de {end-start} milisegundos")
