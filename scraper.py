import requests
from bs4 import BeautifulSoup


BASE_URL = "https://berlinstartupjobs.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
skills = ["python", "typescript", "javascript", "rust"]
all_jobs = []
sch_jobs = []


# 페이지네이션 인덱스 카운트
def get_page_numbers():
    response = requests.get(
        url=f"{BASE_URL}/engineering",
        headers=headers,
    )
    soup = BeautifulSoup(response.content, "html.parser")
    return len(soup.find("ul", class_="bsj-nav").findAll("a"))


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


# def total_jobs(key):
#     for i in range(get_page_numbers()):
#         url = f"{BASE_URL}/engineering/page/{i+1}/"
#         scraper(url)
#
#     for skill in skills:
#         url = f"{BASE_URL}/skill-areas/{skill}/"
#         scraper(url)
#
#     url = f"{BASE_URL}/skill-areas/{key}/"
#     scraper(url)
#
#     return all_jobs


def search_jobs_keyword(key):
    url = f"{BASE_URL}/skill-areas/{key}/"
    scraper(url)
