# Gold Stock Price Predictor and Regression Analysis

## Overview
This project leverages three powerful regression models—Linear Regression, Ridge Regression, and Lasso Regression—to predict the stock prices of Gold (GC=F). The analysis encompasses data visualization, model training, and evaluation.
- [Yahoo Finance](https://finance.yahoo.com/quote/GC=F/history?p=GC=F)
- [Scikit-Learn] (https://scikit-learn.org/stable/)

## Key Steps and Findings

### 1. Data Loading and Visualization
- Utilized historical monthly data of Gold stock prices.
- Visualized the Adjusted Closing Price and implemented a rolling mean for trend analysis.

### 2. Prediction Modelling and Training
- Forecasted stock prices for the next 12 months.
- Prepared data for training and testing with an 80/20 split.

### 3. Regression Models
- Trained Linear, Ridge, and Lasso Regression models on the dataset.
- Evaluated each model's performance using the test data.

### 4. Visualization of Results
- Plotted the original Adjusted Closing Price and Moving Average.
- Overlaid predictions from Linear, Ridge, and Lasso Regression models for a comprehensive comparison.

## Results and Conclusion
- Lasso Regression emerged as the best performer, achieving a score of 86.07%.
- The visualizations provide valuable insights into the effectiveness of each regression model.
- This project offers a robust framework for predicting Gold stock prices, aiding investors and analysts in decision-making.
