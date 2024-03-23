import requests
from bs4 import BeautifulSoup

BASE_URL = "https://berlinstartupjobs.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

sch_jobs = []


def scraper(url):
    """구인정보 추출"""
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    if response.status_code == 200:
        try:
            jobs = soup.find("ul", class_="jobs-list-items").findAll(
                "li", class_="bjs-jlid"
            )[0:5]
            job_info(jobs)
        except AttributeError:
            return print("AttributeError")

    else:
        print(response.status_code)


def job_info(jobs):
    """구인정보 편집"""
    for job in jobs:
        company = job.find("a", class_="bjs-jlid__b").text
        position = job.find("h4", class_="bjs-jlid__h").find("a").text
        description = job.find("div", class_="bjs-jlid__description").text
        link = job.find("h4", class_="bjs-jlid__h").find("a")["href"]
        job_data = {
            "company": company,
            "position": position,
            "description": description,
            "link": link,
            "source": "berlinstartupjobs.com",
        }
        sch_jobs.append(job_data)


def search_jobs_berlinstartupjobs(key):
    """구인정보 내보내기"""
    sch_jobs.clear()
    url = f"{BASE_URL}/skill-areas/{key}/"
    scraper(url)
    return sch_jobs
