# ETL-Query Lab: Data Processing with SQLite

This project focuses on the ETL (Extract, Transform, Load) process to handle datasets. The end goal is to extract a dataset from a URL, transform it for analysis, load it into an SQLite database, and then run SQL queries to retrieve insights from the processed data.

## Overview:

1. **Extraction (E):** Obtain a dataset from sources such as Kaggle or data.gov. Preferred formats are JSON or CSV.
2. **Transformation (T):** Clean, filter, and enrich the data to make it suitable for analysis.
3. **Loading (L):** Load the transformed data into an SQLite database table using Python's `sqlite3` module.
4. **Query (Q):** Perform SQL queries on the SQLite database to analyze the data and gain insights.

## Tasks:

- Fork the provided project and set it up to run.
- Optimize the query to ensure it doesn't merely print a massive output on the screen.
- Convert `main.py` into a command-line tool, allowing each ETL step to be executed independently.
- Select and process a new dataset of your choice, following the same ETL steps.
- Ensure your project adheres to coding standards and passes all lint/tests. Aim for a built badge for credibility.
- Document your project structure with an architectural diagram.

## Reflection:

Upon completing the lab, reflect on the following:

1. Challenges faced during the ETL process and the strategies you employed to overcome them.
2. Insights or knowledge gained from querying the SQLite database.
3. The efficiency of SQLite and SQL in data analysis, and their limitations.
4. Feedback on the AI assistant utilized and how it compares to others you've tried in terms of strengths and weaknesses.
5. Recommendations or improvements for this lab. What additional datasets might be interesting to analyze?

## Challenge Exercises (Optional):

1. Enhance the transformation phase by joining the data with another dataset, aggregating by specific categories, or normalizing columns.
2. Identify and display correlated fields in the data using SQL queries.
3. Create a secondary table in the SQLite database and demonstrate a join operation between the two tables.
4. Implement a Flask web application that executes queries upon request and showcases the results.
5. Containerize the application with Docker for better portability.

## Requirements:

- Python
- SQLite
- Recommended AI Assistant (other than those previously used, such as Anthropic's Claud, Bard, Copilot, CodeWhisperer, etc.)

## Getting Started:

To get started with this project:

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Navigate to the project directory and execute the desired operations using the command-line tool.

Happy Data Processing!
