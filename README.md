# **🦠 COVID-19 Daily Cases Visualization and Analysis using Python**



## 📌 Problem Statement and Analysis

During the COVID-19 pandemic, analyzing daily case data was essential for understanding how the situation evolved over time. Large volumes of raw numerical data are difficult to interpret without proper visualization.

This project presents a Python-based system that processes COVID-19 daily case data and converts it into meaningful visual charts. The system applies Object-Oriented Programming (OOP) along with automation features such as decorators, lambda functions, and list comprehensions.

The final output includes:
	•	📈 Daily cases line chart
	•	📊 7-day moving average
	•	🔴 Highlighted peak case values

These features support clear and effective trend analysis.



## 🎯 Objectives

The main objectives of this project are:
	•	✅ Load and clean COVID-19 daily case data from a CSV file
	•	✅ Calculate a 7-day moving average to smooth fluctuations
	•	✅ Visualize daily cases using clear line charts
	•	✅ Identify and highlight peak case days
	•	✅ Apply OOP and advanced Python features in a real-world scenario



## 🏗️ System Overview

The project is divided into three main modules:
	•	📂 Data Module
Handles reading, cleaning, and processing COVID-19 data.
	•	📊 Visualization Module
Generates charts and highlights important trends.
	•	⚙️ Main Module
Controls program flow and connects all components.

📁 Input data is read from a CSV file, and output charts are stored in a separate folder for better organization.



## 🛠️ Tools and Technologies
	•	Python – Core programming language
	•	Pandas – Data handling and cleaning
	•	Matplotlib – Chart generation and visualization
	•	CSV Files – Data storage format
	•	Object-Oriented Programming (OOP) – Modular and maintainable design



## 📊 Data Processing and Analysis

The system begins by importing COVID-19 case data from a CSV file. Since real-world datasets often contain missing or invalid values, data cleaning is performed to ensure accuracy.

To better understand trends, a 7-day moving average is calculated. This reduces daily noise and highlights long-term patterns.
	•	Lambda functions simplify averaging calculations
	•	List comprehensions efficiently process data series

This approach keeps the code clean, efficient, and readable.



## 🧩 Object-Oriented Design

### 🧠 CovidData Class
	•	Loads the CSV dataset
	•	Cleans missing or invalid values
	•	Computes the 7-day moving average

### 🎨 ChartGenerator Class
	•	Plots daily COVID-19 case numbers
	•	Overlays the moving average line
	•	Highlights peak case days

This separation improves code readability and maintainability.



## ⚙️ Automation Features
	•	🧷 Decorators validate date ranges before plotting charts
	•	⚡ Lambda functions simplify mathematical operations
	•	🔁 List comprehensions reduce repetitive loops

These features reduce redundancy and improve code clarity.



## 📈 Visualization Output

The generated chart includes:
	•	📉 A line representing daily COVID-19 cases
	•	📊 A 7-day moving average line
	•	🔴 Markers highlighting peak case days

This makes trend identification faster and more intuitive than analyzing raw numbers.


# ✅ Results and Conclusion

The project successfully converts raw COVID-19 data into clear visual insights. Peaks, trends, and overall patterns become easy to identify using charts and moving averages.

This project demonstrates how Python can be effectively used for data analysis and visualization, while following good programming practices such as Object-Oriented Programming and automation. It serves as a practical example of solving real-world problems using Python.
