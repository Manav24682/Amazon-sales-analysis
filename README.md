# Amazon Sales Analysis

## 📌 Project Overview

This project analyzes Amazon sales data using Python to understand sales performance, customer ordering patterns, product categories, geographical performance, and monthly sales trends.

The project covers the complete data analysis process, including data cleaning, exploratory data analysis (EDA), data visualization, KPI analysis, and dashboard creation.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Analyze overall Amazon sales performance.
- Identify the top-performing states and cities.
- Find the best-performing product categories.
- Analyze monthly sales trends.
- Understand sales by size, sales channel, and fulfillment method.
- Compare B2B and Non-B2B sales.
- Analyze order and quantity patterns.
- Create meaningful visualizations.
- Build an interactive-style sales analysis dashboard.
- Generate useful business insights and recommendations.

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- VS Code
- GitHub

---

## 📂 Dataset

The project uses an Amazon Sales Report dataset containing information about:

- Order ID
- Date
- Product Category
- Size
- Quantity
- Amount
- Sales Channel
- Fulfillment
- Courier Status
- Shipping City
- Shipping State
- B2B information
- Order Status

The original CSV dataset is not included in this repository because of its file size.

---

## 🧹 Data Cleaning & Preprocessing

The following preprocessing steps were performed:

- Checked missing values.
- Checked duplicate records.
- Removed duplicate rows.
- Removed rows with missing shipping location information.
- Removed columns containing entirely missing values.
- Removed the `fulfilled-by` column.
- Filled missing currency values using the mode.
- Filled missing sales amount values using the mean.
- Converted the `Date` column into datetime format.
- Extracted the month from the date for monthly analysis.

---

## 🔎 Exploratory Data Analysis (EDA)

Several questions were analyzed using Pandas `groupby()`, aggregation, sorting, and filtering.

### Key EDA areas:

- Top 10 states by sales amount.
- Top 10 cities by sales amount.
- Sales by product category.
- Sales by size.
- Sales by sales channel.
- Sales by fulfillment method.
- Orders by order status.
- Courier status analysis.
- Monthly sales analysis.
- Quantity sold by category.
- Quantity sold by state and city.
- B2B vs Non-B2B sales.
- Average sales amount by category.
- Average order value by state.
- Orders by category, state, and city.
- Monthly order and quantity analysis.

---

## 📊 Data Visualization

The project uses Matplotlib and Seaborn to visualize important findings.

### Visualizations include:

- Monthly Sales Trend
- Sales by Product Category
- Top 10 States by Sales
- Top 10 Cities by Sales
- Sales by Size
- Sales by Fulfillment
- Sales by Sales Channel
- B2B vs Non-B2B Sales
- Sales Distribution
- Correlation Analysis

---

## 📈 Key Performance Indicators (KPIs)

The dashboard includes four major KPIs:

### 💰 Total Sales

Shows the total sales amount generated from the dataset.

### 📦 Total Quantity

Shows the total number of products sold.

### 🛒 Total Orders

Shows the number of unique orders.

### 💵 Average Order Value

Shows the average sales value per order.

---

## 📊 Dashboard

A final Amazon Sales Analysis dashboard was created by combining the most important KPIs and visualizations.

### Dashboard Components

- Total Sales
- Total Quantity
- Total Orders
- Average Order Value
- Monthly Sales Trend
- Top 5 Categories by Sales
- Top 10 States by Sales
- Top 10 Cities by Sales

---

## 💡 Key Business Insights

Business insights will be added after reviewing the final analysis results.

The insights will focus on:

- Strongest-performing states.
- Strongest-performing cities.
- Highest-performing product categories.
- Highest-sales months.
- Customer/order behavior.
- B2B vs Non-B2B contribution.
- Areas with potential business improvement.

---

## 🎯 Business Recommendations

Based on the final analysis, recommendations will focus on:

- Improving performance in high-potential regions.
- Maintaining inventory for high-demand categories.
- Focusing marketing efforts on strong-performing markets.
- Understanding monthly sales patterns.
- Exploring opportunities to increase weaker sales segments.
- Using customer and order trends to improve business decisions.

---

## 🚀 How to Run the Project

### 1. Clone the repository

'''bash
git clone
<>

```bash
git clone <your-github-repository-link>
