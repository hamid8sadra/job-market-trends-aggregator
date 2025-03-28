# Job Market Trends Aggregator

A Python-based tool designed to scrape, aggregate, and analyze job market trends from online sources. Built with `BeautifulSoup`, `Selenium`, `Pandas`, and other libraries, this project showcases advanced web scraping, data processing, and analysis skills tailored for real-world applications.

## Purpose
As a Python developer, I created this project to demonstrate my web scraping and data collection—skills critical for data-driven decision-making. The tool extracts job postings from `jobvision.ir`, a Persian-language job board, processes multilingual data, and generates actionable insights, such as trending skills or regional demand.

## Tech Stack
- **Python**: Core language for scripting and logic.
- **BeautifulSoup**: For parsing static HTML content.
- **Selenium**: For handling dynamic, JavaScript-heavy websites.
- **Pandas**: For data manipulation and analysis.
- **Git**: Version control for collaboration and tracking.

## Setup
1. Clone the repository: `git clone <https://github.com/hamid8sadra/job-market-trends-aggregator.git>`
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
4. Install dependencies: `pip install -r requirements.txt`
5. Install a WebDriver (e.g., ChromeDriver) for Selenium—details in Step 2.

More features and implementation details to follow as the project evolves!

## Implementation: Step 2 - Core Scraper Finalized
After testing, I finalized the scraper to work with my local setup (Windows, ChromeDriver at `chromedriver-win64/chromedriver.exe`). The script now reliably extracts job data from `jobvision.ir/jobs`, handling cases where fields like salary are missing.

### Why This Approach?
- **Portability:** I used `os.path.join` for the ChromeDriver path, making the script adaptable across systems.
- **Real-World Testing:** The output (e.g., "کارشناس حسابداری مالی" from "شرکت درمان یاب پخش مهر آریا") confirms the scraper’s accuracy with live data.

### Setup Note
- Place `chromedriver-win64/chromedriver.exe` in the project folder or update the `driver_path` variable to your ChromeDriver location.

## Implementation: Step 3 - Simplified URL-Based Scraper
I discovered that `jobvision.ir/jobs?page={n}&sort=0` directly loads sorted pages, so I refactored the scraper to use URL parameters instead of UI interactions.

### Why This Approach?
- **Efficiency:** Leveraging URL patterns eliminates the need for button clicks or dropdowns, making the scraper faster and more reliable.
- **Simplicity:** Fewer `Selenium` interactions reduce complexity and potential points of failure, a senior-level optimization.
- **Scalability:** The script iterates through pages seamlessly, stopping when no more data is available.

### How It Works
1. Constructs URLs like `https://jobvision.ir/jobs?page=1&sort=0` for each page.
2. Scrapes job cards using existing logic.
3. Continues until no jobs are found or a `max_pages` limit is hit (default: 3).
4. Saves all data to `job_trends.csv` with `Pandas`, using UTF-8-SIG for Persian text.

This optimization highlights my ability to adapt and streamline solutions based on site behavior.

## Implementation: Step 4 - Data Analysis with Pandas
I added a data analysis layer using `Pandas` to extract insights from the scraped job listings, enhancing the project’s value.

### Why This Approach?
- **Insight Generation:** Analyzing trends (e.g., common job titles, regions) demonstrates my ability to turn raw data into actionable information—a critical skill for senior roles.
- **Professional Output:** Saving a summary file alongside the CSV provides a polished deliverable for stakeholders.

### How It Works
1. Scrapes jobs using the URL-based method (`page={n}&sort=0`).
2. Saves raw data to `job_trends.csv`.
3. Analyzes the DataFrame for:
   - Total job count.
   - Top 5 job titles and regions.
   - Salary availability stats.
   - Urgent job count.
4. Outputs results to console and `job_trends_summary.txt`.

This step showcases my proficiency in data manipulation and analysis, rounding out the project for a resume.