from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == "POST":
        selected_eq = request.form.get('eq_select').strip()
        quantity_eq = request.form.get('eq_quantity').strip()



@app.route("/calculus",  methods=["GET","POST"])
def equacoes(selected_eq, quantity_eq):
    if request.method == "GET":
        return
    
    return render_template('equacoes.html')


if __name__ == '__main__':
    app.run(debug=True)
