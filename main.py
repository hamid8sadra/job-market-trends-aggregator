from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os

# Configure Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in background
# Use relative path for portability
driver_path = os.path.join(os.getcwd(), "chromedriver-win64", "chromedriver.exe")
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

def set_sorting_to_newest():
    """Set the sorting dropdown to 'جدیدترین‌' (Newest)."""
    try:
        sort_select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sort-select"))
        )
        select = Select(sort_select)
        select.select_by_value("0")  # '0' corresponds to 'جدیدترین‌'
        time.sleep(2)  # Wait for page to reload with new sorting
    except Exception as e:
        print(f"Error setting sorting: {e}")

def scrape_jobvision_page(url):
    """Scrape job listings from a single page of jobvision.ir."""
    driver.get(url)
    set_sorting_to_newest()  # Apply sorting preference
    
    # Wait for job listings to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "job-card"))
        )
    except Exception as e:
        print(f"Error loading page: {e}")
        driver.quit()
        return []

    # Extract job cards
    job_cards = driver.find_elements(By.TAG_NAME, "job-card")
    jobs = []

    for card in job_cards:
        try:
            # Job title (may include gender like "آقا")
            title = card.find_element(By.CLASS_NAME, "job-card-title").text.strip()
            gender = "آقا" if "آقا" in title else "خانم" if "خانم" in title else "مشخص نشده"
            if gender != "مشخص نشده":
                title = title.replace(f" - {gender}", "").strip()  # Clean title

            # Company name
            company = card.find_element(By.XPATH, ".//a[contains(@href, '/companies')]").text.strip()

            # Location (region and address) and salary
            location_salary_div = card.find_element(By.CLASS_NAME, "text-secondary")
            location_parts = location_salary_div.text.split(" ، ")
            region = location_parts[0] if location_parts else ""
            address_salary = location_parts[1].split(" | ") if len(location_parts) > 1 else [""]
            address = address_salary[0]
            salary = address_salary[1] if len(address_salary) > 1 else "نامشخص"

            # Posting time
            time_posted = card.find_element(By.XPATH, ".//span[@style='color: #8E9CB2;']").text.strip()

            # Status
            status = card.find_element(By.CLASS_NAME, "nudge").text.strip() if card.find_elements(By.CLASS_NAME, "nudge") else "نامشخص"

            # Urgency
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

def main():
    url = "https://jobvision.ir/jobs"
    print("Scraping job listings from jobvision.ir...")
    job_listings = scrape_jobvision_page(url)
    
    # Print results for now
    for job in job_listings:
        print(f"Title: {job['title']}, Gender: {job['gender']}, Company: {job['company']}, "
              f"Region: {job['region']}, Address: {job['address']}, Salary: {job['salary']}, "
              f"Time: {job['time_posted']}, Status: {job['status']}, Urgent: {job['urgent']}")
    
    driver.quit()

if __name__ == "__main__":
    main()