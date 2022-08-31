from distutils.log import debug
from unicodedata import name
from flask import Flask, render_template

app =  Flask(__name__)

todos = {
    2:  {"task": "Read Book", "compeleted": True},
    3:  {"task": "Attend python training by 4:30pm", "compeleted": False},
    1:  {"task" : "Study DSA", "compeleted": False},
}

@app.route("/")

# def home_page():
#     return render_template("file.html", stu_names = name)

@app.route("/todos")
def todo_list():
    return render_template("todo.html", todo_lists = todos)

app.run(debug=True, host = "0.0.0.0")


