from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        name = request.form.get('name')
        bmi = weight / height ** 2
        result = 25   # temporary value to check if it's working just OK 
        return render_template('index.html', result=bmi, name=name)
    return render_template('index.html')

    
app.run(host='0.0.0.0', port=8080)