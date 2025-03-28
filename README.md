# Job Market Trends Aggregator

A sophisticated Python-based tool designed to scrape, aggregate, and analyze job market trends from `jobvision.ir`. Built with `Selenium` and `Pandas`, this project showcases my advanced skills in web scraping, data processing, and analysis—tailored for real-world applications.

## Purpose
As a senior Python developer, I created this project to demonstrate my expertise in web scraping and data collection, skills vital for data-driven insights. The tool extracts job postings from `jobvision.ir`, processes Persian-language data, and generates actionable trends like top job titles and regional demand.

## Tech Stack
- **Python**: Core scripting and logic.
- **Selenium**: Dynamic web scraping with URL-based pagination.
- **Pandas**: Data manipulation and trend analysis.
- **Git**: Version control for collaboration and tracking.

## Features
- Scrapes job listings efficiently using URL parameters (`page={n}&sort=0`).
- Extracts fields: title, gender, company, region, address, salary, time posted, status, urgency.
- Saves raw data to `job_trends.csv`.
- Analyzes trends (e.g., top 5 job titles, regions, urgent jobs) and saves to `analysis.txt`.

## Setup
1. Clone the repository: `git clone https://github.com/hamid8sadra/job-market-trends-aggregator.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
4. Install dependencies: `pip install -r requirements.txt`
5. Download ChromeDriver matching your Chrome version and place it in `chromedriver-win64/chromedriver.exe` (or adjust `driver_path` in `main.py`).
6. Run the script: `python main.py`

## Implementation Highlights
- **Efficient Scraping:** Optimized with URL-based pagination, avoiding unnecessary UI interactions.
- **Robust Parsing:** Handles Persian text and missing data gracefully.
- **Insightful Analysis:** Uses `Pandas` to identify job market trends, saved in a readable format.

This project reflects my ability to design scalable, efficient solutions and deliver meaningful data outputs—skills honed through extensive Python experience.