from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def home_page():
    return render_template('index.html') 

@app.route("/books")
def books_store(): 
	return render_template('books.html')