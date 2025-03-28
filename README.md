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