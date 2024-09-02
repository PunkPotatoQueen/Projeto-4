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
        # return equacoes(selected_eq, quantity_eq)
        return redirect(url_for("equacoes", selected_eq=selected_eq, quantity_eq=quantity_eq))

@app.route("/equacoes",  methods=["GET","POST"])
def equacoes():
    selected_eq = request.args.get("selected_eq")
    quantity_eq = request.args.get("quantity_eq")
    base = select_base(selected_eq,quantity_eq)
    
    if request.method == "GET":
        return render_template('equacoes.html', result=base)
    
    if request.method == "POST":
        
        return render_template('equacoes.html', result=base)
    

@app.route("/resultados", methods=["POST"])
def gera_resultados():
    return
    # if request.method == "POST":
    #     for i in 
    #         mp_result = request.form.get[f"MP_result_{i}"]
    #         fe_result = request.form.get[f"FE_result_{i}"]
    #         vn_result = request.form.get[f"VN_result_{i}"]

@app.route("/gerar-docx")
def relatorio_docx():
    generate_random_docx()

    return redirect(url_for('static', filename='docs/teste01.docx'))

@app.route("/gerar-xlsx")
def planilha_xlsx():

    return redirect(url_for('static', filename='planilhas/planilha.xlsx'))


if __name__ == '__main__':
    app.run(debug=True)