# Backendtask
Project Overview
This tool fetches research papers from PubMed based on a user query and identifies papers with at least one author affiliated with a pharmaceutical or biotech company. The results are saved in a CSV file for easy analysis.



1. How the Code is Organized
The project is structured as follows:

📂 pubmed_fetcher/ (Main package)

📄 fetch.py → Handles API requests to fetch research papers.

📄 filter.py → Identifies industry-affiliated authors using heuristics.

📄 export.py → Saves the filtered data to a CSV file.

📄 utils.py → Helper functions (e.g., API error handling, logging).

📂 cli/ (Command-line interface)

📄 main.py → Parses user input, calls fetch & filter functions, and manages output.

📂 tests/ (Test cases)

📄 test_fetch.py → Tests API data retrieval.

📄 test_filter.py → Tests author affiliation filtering.

📄 test_export.py → Tests CSV file creation.

📄 pyproject.toml → Defines dependencies (managed by Poetry).
📄 README.md → Instructions and project details.




2. Installing Dependencies & Running the Program
Install Dependencies
Use Poetry to install all required packages:

sh
Copy
Edit
poetry install
Run the Program
To fetch papers related to "cancer treatment" and display results:

sh
Copy
Edit
poetry run get-papers-list "cancer treatment"
To save the results in a CSV file:

sh
Copy
Edit
poetry run get-papers-list "COVID-19 vaccine" -f results.csv
To enable debug mode for troubleshooting:

sh
Copy
Edit
poetry run get-papers-list "gene therapy" -d



3. Tools & Libraries Used
Programming & APIs
Python – Core programming language

PubMed API – Fetches research papers

Libraries & Frameworks
Requests – Handles API requests

CSV Module – Saves results in structured format

Poetry – Manages dependencies

Pytest – Runs test cases

AI & LLMs Used in Development
ChatGPT – Assisted in debugging and optimizing code

PubMed E-utilities Docs – Reference for API integration

🔗 PubMed API Docs: https://www.ncbi.nlm.nih.gov/books/NBK25500/
🔗 Poetry Docs: https://python-poetry.org/docs/
