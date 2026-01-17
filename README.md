**Video Game Sales Data Analysis**

Project Overview

This project analyzes global video game sales data to uncover trends across **genres**, **platforms**, and **release years**. Using Python and common data analysis libraries, the project demonstrates how raw data can be cleaned, explored, visualized, and transformed into meaningful insights.

This project is designed to showcase **foundational data analysis skills** suitable for internships and entry-level roles in data analytics, technology, and software development.

---

Tools & Technologies

* **Python**
* **Pandas** – data loading, cleaning, and aggregation
* **NumPy** – numerical operations
* **Matplotlib** – data visualization

---

Dataset

* **Source:** Video Game Sales Dataset (vgsales.csv)
* **Contents:**

  * Game title
  * Platform
  * Genre
  * Publisher
  * Release year
  * Regional sales (NA, EU, JP)
  * Global sales (in millions)

---

Key Objectives

* Clean and preprocess a real-world dataset
* Analyze total sales by genre and platform
* Identify trends in video game sales over time
* Visualize categorical and time-series data using multi-plot dashboards
* Extract insights to support data-driven conclusions

---

Analysis Performed

Data Cleaning

* Removed rows with missing values
* Converted data types (e.g., year column)

Genre Analysis

* Aggregated global sales by genre
* Identified top-performing video game genres

Platform Analysis

* Aggregated global sales by platform
* Visualized the top 10 platforms by total sales

Sales Over Time

* Grouped global sales by release year
* Analyzed trends in video game sales across time

---

Visualizations

The project includes a single dashboard containing:

* Global sales by genre (bar chart)
* Top 10 platforms by global sales (bar chart)
* Global video game sales over time (line chart)

These visualizations allow for easy comparison of categorical and temporal trends.

---

Key Insights

* Certain genres (such as Action and Sports) dominate global sales
* A small number of platforms account for the majority of total sales
* Video game sales peak during major console generations and decline between cycles

---

How to Run the Project

1. Clone or download this repository
2. Ensure `vgsales.csv` is in the project directory
3. Install required libraries:

   ```bash
   pip install pandas numpy matplotlib
   ```
4. Run the analysis script:

   ```bash
   python game_sales_analysis.py
   ```

---

Future Improvements

* Add regional sales comparisons (NA vs EU vs JP)
* Export visualizations as image files
* Introduce interactive dashboards
* Apply basic machine learning models for trend prediction

---

Author

**Coriawn Griffin**
Computer Science & Information Systems Student
Aspiring Data Analyst / Software Engineer

---

License

This project is for educational and portfolio purposes.

