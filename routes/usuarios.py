from conexion import *

@app.route("/login", methods=['POST'])
def login():
    id = request.form['id']
    pas = request.form['pas']
    return render_template("principal.html")

    