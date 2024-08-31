from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == "POST":
        selected_eq = request.form.get('eq_select').strip()
        quantity_eq = request.form.get('eq_quantity').strip()
        return equacoes(selected_eq, quantity_eq)

Exemplo = """
<form action="/equacoes">
    <label>Massa Padrão:</label>
    <input type="int" required>
    <label>Fator de equivalência:</label>
    <input type="int" required>
    <label>Volume de NaOH:</label>
    <input type="int" required>
</form>
"""

@app.route("/equacoes",  methods=["GET","POST"])
def equacoes(selected_eq, quantity_eq):
    if request.method == "POST":

        result = Exemplo
        for _ in range(int(quantity_eq) - 1):
            result += '</br>' + Exemplo
        print(result)

        return render_template('equacoes.html', result=result)
    
    else: return 
    
if __name__ == '__main__':
    app.run(debug=True)
