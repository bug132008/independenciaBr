from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home/index.html')
@app.route('/<any>')
def ani(any):
	return f"A página {any} não foi encontrada"
if __name__ == "__main__":
	app.run(debug=True, port=8080)
