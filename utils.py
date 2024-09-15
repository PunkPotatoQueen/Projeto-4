def select_base(selected_eq , quantity_eq):
    result=''

    if selected_eq == "valor 3":

        for i in range(int(quantity_eq)):
            i+=1
            base_cm=f"""
            <label >Equação {i}:</label>
            <label for="MS_result_{i}">Massa do Soluto (mg):</label>
            <input type="number" name="MS_result_{i}" id="MS_result_{i} min="0.01" max ="100000" step="1.00" required>
            <label for="MM_result_{i}">Massa Molar (g/mol):</label>
            <input type="number" name="MM_result_{i}" id="MM_result_{i}" min="0.001" max ="300" step="0.001" required>
            <label for="VS_result_{i}">Volume do Soluto (Litros):</label>
            <input type="number" name="VS_result_{i}" id="VS_result_{i}" min="0.001" max ="5" step="0.010" required>"""
            result += '<br>' + base_cm

        return result
    else: 
        for i in range(int(quantity_eq)):
            i+=1
            base_csc= f"""
            <label >Equação {i}:</label>
            <label for="MP_result_{i}">Massa Padrão (mg):</label>
            <input type="number" name="MP_result_{i}" id="MP_result_{i}" min="1" max="10000" step="0.01" required>
            <label for="FE_result_{i}">Fator de equivalência:</label>
            <input type="number" name="FE_result_{i}" id="FE_result_{i}" min="0.1" max="10" step="0.1" required>
            <label for="VN_result_{i}">Volume de NaOH (L):</label>
            <input type="number" name="VN_result_{i}" id="VN_result_{i}" min="0.001" max="5" step="0.001" required>"""
            if selected_eq == "valor 2":
                correcao =f"""
            <label for="FC_result_{i}">Fator de Correção:</label>
            <input type="number" name="FC_result_{i}" id="FC_result_{i}" min="0.50" max="1" step="0.01" required>"""
                base_csc += correcao

            result += '<br>' + base_csc
        return result