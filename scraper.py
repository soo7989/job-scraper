import requests
from bs4 import BeautifulSoup

skills = [
    "python",
    # "typescript",
    # "javascript",
    # "rust"
]
all_jobs = []


def scraper(url):
    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    )
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find(
        "ul", class_="jobs-list-items").findAll("li", class_="bjs-jlid")
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
        all_jobs.append(job_data)


def get_page_numbers():
    response = requests.get(
        "https://berlinstartupjobs.com/engineering/",
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    )
    soup = BeautifulSoup(response.content, "html.parser")
    return len(soup.find("ul", class_="bsj-nav").findAll("a"))


# 모두 모으기
def total_jobs():
    for i in range(get_page_numbers()):
        url = f"https://berlinstartupjobs.com/engineering/page/{i + 1}/"
        scraper(url)

    for skill in skills:
        url = f"https://berlinstartupjobs.com/skill-areas/{skill}/"
        scraper(url)

    return all_jobs



