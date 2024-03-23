import requests
from bs4 import BeautifulSoup
from common import limit_text_length

BASE_URL = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

sch_jobs = []


def scraper(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    if response.status_code == 200:
        try:
            job_group1 = soup.find(id="category-2").findAll("li")
            job_group2 = soup.find(id="category-18").findAll("li")
            job_group1.pop()
            job_group2.pop()
            jobs = job_group1 + job_group2
            jobs = jobs[:5]
            job_info(jobs)
        except AttributeError:
            return print("AttributeError")
    else:
        print(response.status_code)


def scraper_detail(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    description = soup.find(id="job-listing-show-container").find("div").text.strip()
    max_desc = f"{limit_text_length(description)}..."
    return max_desc


def job_info(jobs):
    for job in jobs:
        company = job.find(class_="company").text
        position = job.find(class_="title").text
        get_link = job.find(class_="title").find_parent("a")["href"]
        link = f"https://weworkremotely.com{get_link}"
        description = scraper_detail(link)
        job_data = {
            "company": company,
            "position": position,
            "description": description,
            "link": link,
            "source": "weworkremotely.com",
        }
        sch_jobs.append(job_data)


def search_jobs_wwr(key):
    sch_jobs.clear()
    url = f"{BASE_URL}{key}"
    scraper(url)
    return sch_jobs
