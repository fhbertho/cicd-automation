from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Py-CICD-Automation! (V1.0)'

if __name__ == '__main__':
    app.run(host='o.o.o.o', port=5000)