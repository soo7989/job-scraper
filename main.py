from flask import Flask, render_template, request, redirect
from scraping_berlinstartupjobs import search_jobs_berlinstartupjobs
from scraping_web3 import search_jobs_web3
from scraping_wwr import search_jobs_wwr

app = Flask("Find Jobs")
site1 = search_jobs_berlinstartupjobs
site2 = search_jobs_web3
site3 = search_jobs_wwr


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results")
def result():
    key = request.args.get("keyword")
    if key == None or key == "":
        return redirect("/")
    else:
        job_list = site1(key) + site2(key) + site3(key)
        return render_template(
            "results.html",
            key=key,
            num_results=len(job_list),
            job_list=job_list,
        )


app.run()
