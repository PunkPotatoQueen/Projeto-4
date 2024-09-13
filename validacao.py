def validar_valores(valores, tipo):
    erros = []

    for i, valor in enumerate(valores):
        if tipo == "valor 3":
            if len(valor) != 3 or not all(isinstance(v, (int, float)) for v in valor):
                erros.append(f"Erro na Equação {i + 1}: Todos os valores devem ser números válidos.")
        else:
            if len(valor) < 3 or not all(isinstance(v, (int, float)) for v in valor[:3]):
                erros.append(f"Erro na Equação {i + 1}: Massa Padrão, Fator de Equivalência e Volume de NaOH devem ser números válidos.")
            if tipo == "valor 2" and (len(valor) < 4 or not isinstance(valor[3], (int, float))):
                erros.append(f"Erro na Equação {i + 1}: Fator de Correção deve ser um número válido.")

    return erros

def validar_entrada(entrada):
    if entrada is None or entrada.strip() == "":
        return False, "Valor não pode ser vazio."
    try:
        float(entrada) 
        return True, ""
    except ValueError:
        return False, "Valor deve ser um número válido."
