def validar_entrada(valor, min_val=None, max_val=None):

    try:
        valor_float = float(valor)

        if min_val is not None and valor_float < min_val:
            return False, f"Valor menor que o mínimo permitido ({min_val})"

        if max_val is not None and valor_float > max_val:
            return False, f"Valor maior que o máximo permitido ({max_val})"

        return True, ""

    except ValueError:
        return False, "Valor inválido, por favor insira um número"
