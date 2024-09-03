import concurrent.futures, app, time

cf = concurrent.futures
calculus = app

def thread_concentracao_sem_correcao(valores):
    with cf.ThreadPoolExecutor() as executor:
        results = executor.map(lambda args: calculus.calcular_concentracao_sem_correcao(*args), valores)
        # results = [executor.submit(calculus.calcular_concentracao_sem_correcao,*args) for args in valores]
        resultados = []
        for f in results:
            resultados.append(f)

        return resultados

def thread_concentracao_com_correcao(valores):
    with cf.ThreadPoolExecutor() as executor:
        results = executor.map(lambda args: calculus.calcular_concentracao_com_correcao(*args), valores)
        # results = [executor.submit(calculus.calcular_concentracao_com_correcao,*args) for args in valores]
        resultados = []
        for f in results:
            resultados.append(f)

        return resultados

def thread_concentracao_molar(valores):
    with cf.ThreadPoolExecutor() as executor:
        results = executor.map(lambda args: calculus.calcular_concentracao_molar(*args), valores)
        # results = [executor.submit(calculus.calcular_concentracao_molar, *args) for args in valores]
        resultados = []
        for f in results:
            resultados.append(f)

        return resultados

if __name__ == "__main__":
        
    start = time.perf_counter()

    valores_sc = [[0.85,1,0.025],[0.1,10,0.05],[0.1,45,12]]  # Exemplo para o calculo de 3 concentrações sem correção
    valores_cc = [[0.85,99.8,1,0.025],[0.1,80,10,0.05],[0.1,100,45,12]]  # Exemplo para o calculo de 3 concentrações com correção
    valores_m = [[1,204.22,0.025],[5,102,0.5],[10,500,1]] # Exemplo para o calculo de 3 concentrações molares

    thread_concentracao_sem_correcao(valores_sc)
    thread_concentracao_com_correcao(valores_cc)
    thread_concentracao_molar(valores_m)

    end = time.perf_counter()
    print(f"{end - start} miliseconds")



