import requests
from bs4 import BeautifulSoup
from common import limit_text_length

BASE_URL = "https://web3.career"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

sch_jobs = []


def scraper(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    if response.status_code == 200:
        try:
            jobs = (
                soup.find(class_="row-cols-2")
                .find("table")
                .find("tbody")
                .findAll("tr", attrs={"data-jobid": True})[0:5]
            )
            job_info(jobs)
        except AttributeError:
            return print("AttributeError")
    else:
        print(response.status_code)


def scraper_detail(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    description = soup.find(attrs={"style": "word-wrap: break-word;"}).text.strip()

    max_desc = f"{limit_text_length(description)}..."
    return max_desc


def job_info(jobs):
    for job in jobs:
        jobid = job.get("data-jobid")
        company = job.findAll("td")[1].text.strip()
        position = job.findAll("td")[0].text.strip()
        link = transform_string(position, jobid)
        description = scraper_detail(link)
        job_data = {
            "company": company,
            "position": position,
            "description": description,
            "link": link,
            "source": "web3.career",
        }
        sch_jobs.append(job_data)


def transform_string(position, jobid):
    lowercased_string = position.lower()
    hyphenated_string = lowercased_string.replace(" ", "-")
    dotted_string = hyphenated_string.replace(".", "-")
    final_string = f"{BASE_URL}/{dotted_string}/{jobid}"
    return final_string


def search_jobs_web3(key):
    sch_jobs.clear()
    url = f"{BASE_URL}/{key}-jobs"
    scraper(url)
    return sch_jobs
