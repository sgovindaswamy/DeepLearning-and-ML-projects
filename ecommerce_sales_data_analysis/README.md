# Ecommerce Sales Data Analysis

This project analyzes an e-commerce sales dataset to understand buying patterns, category performance, pricing effects, and customer satisfaction. The goal is to answer business-facing questions using exploratory data analysis (EDA) and a simple statistical regression model.

## Overview

The notebook processes a retail dataset containing product information, price, review score, review count, and monthly sales values across 12 months. It combines feature engineering, visualization, and regression analysis to uncover relationships such as:

- which product category has the strongest sales performance
- whether price is associated with review score or total sales
- how revenue varies by category
- how customer satisfaction changes across product groups

---

## Dataset

The dataset is stored in `ecommerce_sales_analysis.csv`.

### Columns

| Column | Description |
| --- | --- |
| product_id | Unique product identifier |
| product_name | Product name |
| category | Product category |
| price | Selling price of the product |
| review_score | Average customer rating |
| review_count | Number of reviews |
| sales_month_1 to sales_month_12 | Monthly sales values for each month |

### Feature Engineering

The notebook creates two derived variables to simplify business analysis:

- `Total sales` = sum of sales across all 12 months
- `Total revenue` = `Total sales * price`

This makes it easier to compare products and categories based on total volume and monetary contribution.

---

## Business Questions Addressed

The analysis focuses on the following questions:

1. Which product categories generate the highest and lowest sales?
2. Is there a relationship between product price and customer review score?
3. How do monthly sales patterns differ by category?
4. Which categories have the strongest average review performance?
5. Are review scores associated with sales or revenue?

---

## Exploratory Data Analysis

The notebook performs EDA using pandas and matplotlib/seaborn to understand the structure of the data and reveal patterns.

### 1) Sales by Category

The dataset is grouped by category, and total sales are aggregated to identify which product segments are performing best. The visualizations include a pie chart and category-wise sales comparisons.

This helps answer questions such as:

- which category contributes the largest share of overall sales
- which categories underperform relative to others

### 2) Price vs Sales and Review Behavior

The notebook visualizes the relationship between `price` and:

- `Total sales`
- `review_score`

This helps determine whether premium pricing is aligned with stronger customer satisfaction or whether higher-priced products simply make different sales contributions.

### 3) Monthly Sales Trends

Monthly sales are grouped by category and plotted over the 12-month period. This reveals trends such as seasonal spikes, category-specific demand patterns, and product lifecycle cycles.

### 4) Customer Satisfaction Analysis

The notebook computes the average review score by category and compares them visually. This gives a simple view of which categories are most appreciated by customers.

---

## Statistical Modeling and Architecture

The project uses a lightweight statistical workflow rather than a deep learning model. The analytical pipeline is as follows:

1. Import dataset and preprocess values
2. Create aggregated business metrics (`Total sales`, `Total revenue`)
3. Explore correlations and trends
4. Apply regression analysis to quantify the relationship between price and review score
5. Visualize category performance and customer sentiment

### Regression Model

The notebook uses `statsmodels` OLS (Ordinary Least Squares) regression to model the relationship between price and review score.

The structure is conceptually:

- Dependent variable: `review_score`
- Independent variable: `price`
- Model: `sm.OLS(Y, X).fit()`

This allows the analysis to estimate how much of the variation in review score can be explained by product price.

---

## Evaluation Metrics and Results

### Regression Performance

The model summary reports:

- R-squared (uncentered): 0.657
- Adjusted R-squared (uncentered): 0.657

This means that approximately 65.7% of the variation in the dependent variable is explained by the model in this uncentered setup. While this is a moderate explanatory signal, it also shows that pricing alone does not fully determine customer review behavior.

### Correlation Analysis

The notebook computes a correlation matrix for:

- `review_score`
- `Total sales`
- `Total revenue`

The reported correlations are:

- `review_score` vs `Total sales`: -0.018186
- `review_score` vs `Total revenue`: 0.027932
- `Total sales` vs `Total revenue`: 0.256792

These values indicate that there is little or no meaningful linear relationship between review score and sales/revenue. In other words, customer ratings do not appear to strongly predict either total sales volume or total revenue in this dataset.

The project explicitly concludes that:

> The correlation coefficients and the graphs indicate that there is no relationship between review score, total sales, and total revenue.

---

## Key Insights

1. Category-level sales analysis identifies the strongest and weakest performers.
2. Price is not strongly tied to review score in this dataset.
3. Customer satisfaction metrics do not appear to drive sales or revenue strongly.
4. Sales trends across months can reveal seasonal demand patterns.
5. The dataset is more suitable for business intelligence and exploratory product analysis than for a high-accuracy predictive model.

---

## Project Structure

- `ecommerce_sales_analysis.csv`: retail sales dataset
- `ecommerce_sales_analysis.ipynb`: notebook containing data analysis, feature engineering, visualizations, and regression modeling

---

## Conclusion

This project demonstrates how business-oriented EDA can turn raw transactional data into useful insights. Instead of focusing only on a single predictive algorithm, it combines category analysis, price evaluation, trend analysis, and regression metrics to tell a practical story about e-commerce performance.

The main takeaway is that category sales and monthly patterns provide more actionable business information than price alone, and that review score is not strongly correlated with either sales volume or total revenue in this dataset.

---

## Potential Next Steps

- Add more advanced predictive models such as linear regression with multiple features
- Use customer segmentation or clustering
- Build a sales forecasting model for monthly demand
- Incorporate category-level seasonality analysis
- Explore whether discounting or promotions affect conversion and revenue

This project is a strong example of data-driven retail analysis that combines descriptive analytics and statistical evaluation for decision-making.

