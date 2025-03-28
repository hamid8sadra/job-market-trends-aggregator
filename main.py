from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os

# Configure Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
driver_path = os.path.join(os.getcwd(), "chromedriver-win64", "chromedriver.exe")
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

def scrape_jobvision_page(url):
    """Scrape job listings from a given page URL."""
    driver.get(url)
    
    # Wait for job listings to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "job-card"))
        )
    except Exception as e:
        print(f"Error loading page {url}: {e}")
        return []

    # Extract job cards
    job_cards = driver.find_elements(By.TAG_NAME, "job-card")
    jobs = []

    for card in job_cards:
        try:
            title = card.find_element(By.CLASS_NAME, "job-card-title").text.strip()
            gender = "آقا" if "آقا" in title else "خانم" if "خانم" in title else "مشخص نشده"
            if gender != "مشخص نشده":
                title = title.replace(f" - {gender}", "").strip()

            company = card.find_element(By.XPATH, ".//a[contains(@href, '/companies')]").text.strip()
            location_salary_div = card.find_element(By.CLASS_NAME, "text-secondary")
            location_parts = location_salary_div.text.split(" ، ")
            region = location_parts[0] if location_parts else ""
            address_salary = location_parts[1].split(" | ") if len(location_parts) > 1 else [""]
            address = address_salary[0]
            salary = address_salary[1] if len(address_salary) > 1 else "نامشخص"

            time_posted = card.find_element(By.XPATH, ".//span[@style='color: #8E9CB2;']").text.strip()
            status = card.find_element(By.CLASS_NAME, "nudge").text.strip() if card.find_elements(By.CLASS_NAME, "nudge") else "نامشخص"
            urgent = "فوری" in card.text

            jobs.append({
                "title": title,
                "gender": gender,
                "company": company,
                "region": region,
                "address": address,
                "salary": salary,
                "time_posted": time_posted,
                "status": status,
                "urgent": urgent
            })
        except Exception as e:
            print(f"Error parsing job card: {e}")
            continue
    return jobs

def scrape_all_pages(base_url, max_pages=3):
    """Scrape all pages using URL parameters."""
    all_jobs = []
    page = 1

    while True:
        url = f"{base_url}?page={page}&sort=0"
        print(f"Scraping page {page}: {url}")
        jobs = scrape_jobvision_page(url)
        
        if not jobs:  # Stop if no jobs are found (end of pages)
            print("No more jobs found.")
            break
        
        all_jobs.extend(jobs)
        print(f"Page {page} scraped: {len(jobs)} jobs (Total: {len(all_jobs)})")
        
        page += 1
        if max_pages and page > max_pages:  # Respect max_pages limit
            print(f"Stopped at {max_pages} pages as per limit.")
            break
        
        time.sleep(1)  # Polite delay to avoid overwhelming the server

    return all_jobs

def main():
    base_url = "https://jobvision.ir/jobs"
    print("Scraping job listings from jobvision.ir...")
    job_listings = scrape_all_pages(base_url, max_pages=3)  # Limit to 3 pages for testing
    
    # Save to Pandas DataFrame and CSV
    df = pd.DataFrame(job_listings)
    df.to_csv("job_trends.csv", index=False, encoding="utf-8-sig")
    print(f"Saved {len(job_listings)} jobs to job_trends.csv")
    
    driver.quit()

if __name__ == "__main__":
    main()