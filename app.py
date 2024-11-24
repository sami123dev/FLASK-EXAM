from flask import Flask, render_template, request

app = Flask(__name__)


def calcular_descuento(age):
    if age >= 18 and age <= 30:
        discount = 15
    elif age > 30:
        discount = 25
    else:
        discount = 0
    return discount

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['POST', 'GET'])
def ejercicio1():
    if request.method == 'POST':
        paint_value = 9000
        name = request.form['name']
        age = int(request.form['age'])
        paint_quantity = int(request.form['paint_cuantity'])
        total_to_pay = paint_quantity * paint_value
        discount = calcular_descuento(age=age)
        total_discount = total_to_pay * discount / 100
        total_with_discount = total_to_pay - total_discount
        form_ok = True
        return render_template('ejercicio1.html', name=name, total_to_pay=total_to_pay, total_discount=total_discount, total_with_discount=total_with_discount, form_ok=form_ok)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET','POST'])
def ejercicio2():
    loged_in = False
    welcome_message = ""
    user_list = [["juan", "admin", "admin"],["pepe", "user", "user"]] 
    if request.method == 'POST':
        username = request.form['name'].lower()
        password = request.form['pass']
        for i in user_list:
            if username == i[0] and password == i[1]:
                loged_in = True
                if i[1] == "admin":
                    welcome_message = f"Bienvenido Administrador {i[0]}"
                else:
                    welcome_message = f"Bienvenido Usuario {i[0]}"
            if not loged_in:
                welcome_message = "Usuario o contraseña incorrectos"
        return render_template('ejercicio2.html', loged_in=loged_in, welcome_message=welcome_message)
    return render_template('ejercicio2.html')


if (__name__) == ("__main__"):
    app.run(debug=True)