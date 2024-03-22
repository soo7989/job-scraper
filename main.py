from flask import Flask, render_template, request
from scraping_berlinstartupjobs import search_jobs_keyword
from scraping_web3 import search_jobs_keyword

app = Flask("Find Jobs")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results")
def result():
    key = request.args.get("keyword")
    job_list = search_jobs_keyword(key)
    return render_template(
        "results.html",
        key=key,
        num_results=len(job_list),
        job_list=job_list,
    )


app.run()
