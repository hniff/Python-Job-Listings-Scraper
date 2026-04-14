import requests
import csv
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
job_listings = []
job_listings_card = soup.find_all("div", class_="card-content")

for job in job_listings_card:
    job_title = job.find("h2", class_="title is-5").text.strip()
    company_name = job.find("h3", class_="subtitle is-6 company").text.strip()
    location = job.find("p", class_="location").text.strip()
    details_url = job.find("a", href = (lambda h: h and h.startswith("https://realpython.github.io/fake-jobs/jobs")))["href"]
    job_listings.append({
        "title": job_title,
        "company": company_name,
        "location": location,
        "details_url": details_url
    })

filename = "job_listings.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["title", "company", "location", "details_url"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for job in job_listings:
        writer.writerow(job)