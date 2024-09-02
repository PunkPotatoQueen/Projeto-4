from flask import Flask, render_template, request, redirect, url_for
from libs.docx_manipulator import DocxGenerator, generate_random_docx
from utils import *

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == "POST":
        selected_eq = request.form.get('eq_select').strip()
        quantity_eq = request.form.get('eq_quantity').strip()

        return redirect(url_for("equacoes", selected_eq=selected_eq, quantity_eq=quantity_eq))

@app.route("/equacoes",  methods=["GET","POST"])
def equacoes():
    global selected_eq_atual
    global quantity_eq_atual
    if request.method == "GET":
        selected_eq = request.args.get("selected_eq")
        quantity_eq = request.args.get("quantity_eq")
        selected_eq_atual = selected_eq
        quantity_eq_atual = quantity_eq

        base = select_base(selected_eq_atual,quantity_eq_atual)
        return render_template('equacoes.html', result=base)
    
    if request.method == "POST":
        
        valores_totais = []
        if selected_eq_atual == "valor 3":
            for i in range(int(quantity_eq_atual)):
                valores_atuais = [] 
                mp_result = request.form.get(f"MP_result_{i}")
                fe_result = request.form.get(f"FE_result_{i}")
                vn_result = request.form.get(f"VN_result_{i}")
                valores_totais.append(valores_atuais.extend([mp_result,fe_result,vn_result]))
            return gera_resultados(valores_totais)
        else:
            for i in range(int(quantity_eq_atual)):
                valores_atuais = []
                mp_result = request.form.get(f"MP_result_{i}")
                fe_result = request.form.get(f"FE_result_{i}")
                vn_result = request.form.get(f"VN_result_{i}")
                valores_atuais.extend([mp_result,fe_result,vn_result])
                if selected_eq_atual == "valor 2":
                    fc_result = request.form.get(f"FC_result_{i}")
                    valores_atuais.append(fc_result)
                valores_totais.append(valores_atuais)
            return gera_resultados(valores_totais)


@app.route("/resultados", methods=["POST"])
def gera_resultados(respostas):
    return print(respostas)

@app.route("/gerar-docx")
def relatorio_docx():
    generate_random_docx()

    return redirect(url_for('static', filename='docs/teste01.docx'))

@app.route("/gerar-xlsx")
def planilha_xlsx():

    return redirect(url_for('static', filename='planilhas/planilha.xlsx'))


if __name__ == '__main__':
    app.run(debug=True)