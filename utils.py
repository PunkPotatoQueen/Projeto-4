def select_base(selected_eq , quantity_eq):
    result=''

    if selected_eq == "valor 3":
        for i in range(int(quantity_eq)):
            base_cm=f"""
            <label >Equação {i}:</label>
            <label for="MS_result_{i}">Massa do Soluto:</label>
            <input type="int" name="MS_result_{i}" id="MS_result_{i}" required>
            <label for="MM_result_{i}">Massa Molar:</label>
            <input type="int" name="MM_result_{i}" id="MM_result_{i}" required>
            <label for="VS_result_{i}">Volume do Soluto:</label>
            <input type="int" name="VS_result_{i}" id="VS_result_{i}" required>"""
            result += '<br>' + base_cm
            i+=1

        return result
    else: 
        for i in range(int(quantity_eq)):
            base_csc= f"""
            <label >Equação {i}:</label>
            <label for="MP_result_{i}">Massa Padrão:</label>
            <input type="int" name="MP_result_{i}" id="MP_result_{i}" required>
            <label for="FE_result_{i}">Fator de equivalência:</label>
            <input type="int" name="FE_result_{i}" id="FE_result_{i}" required>
            <label for="VN_result_{i}">Volume de NaOH:</label>
            <input type="int" name="VN_result_{i}" id="VN_result_{i}" required>"""
            if selected_eq == "valor 2":
                correcao = """
            <label for= "FC_result_{i}">Fator de Correção:</label>
            <input type="int" name="FC_result_{i}" id="FC_result_{i}" required>"""
                base_csc += correcao

            result += '<br>' + base_csc
            i+=1
        return result