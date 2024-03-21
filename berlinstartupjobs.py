import requests
from bs4 import BeautifulSoup

BASE_URL = "https://berlinstartupjobs.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

sch_jobs = []


# 구인정보 추출
def job_info(jobs):
    for job in jobs:
        company = job.find("a", "bjs-jlid__b").text
        position = job.find("h4", "bjs-jlid__h").find("a").text
        description = job.find("div", "bjs-jlid__description").text
        link = job.find("h4", "bjs-jlid__h").find("a")["href"]
        job_data = {
            "company": company,
            "position": position,
            "description": description,
            "link": link,
        }
        sch_jobs.append(job_data)


# 구인정보
def scraper(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("ul", class_="jobs-list-items").findAll("li", class_="bjs-jlid")
    if response.status_code == 200:
        job_info(jobs)
    else:
        print(f"Error: {response.status_code}")


def search_jobs_keyword(key):
    sch_jobs.clear()
    url = f"{BASE_URL}/skill-areas/{key}/"
    scraper(url)
    return sch_jobs
