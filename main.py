from flask import Flask, render_template

app = Flask("MyJobs")


@app.route("/")
def home():
    return render_template("home.html")

# print(len(total_jobs()))
