from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        result = 25   # temporary value to check if it's working just OK 
        return render_template('index.html', result=result)
    return render_template('index.html')

    
app.run(host='0.0.0.0', port=8080)