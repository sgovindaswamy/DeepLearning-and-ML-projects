# Amazon Stock Price Prediction

This project explores time-series forecasting for Amazon stock prices using several classical and deep-learning approaches. The notebook compares statistical models such as ARIMA, SARIMA, and Exponential Smoothing with a recurrent neural network based on LSTM (Long Short-Term Memory), with the goal of understanding which strategy performs best for financial forecasting.

## Overview

Stock price prediction is a challenging problem because financial time series are noisy, non-stationary, and influenced by many hidden factors. In this project, the analysis focuses on the adjusted closing price (`Adj Close`), which is often preferred in time series forecasting because it accounts for corporate actions such as stock splits and dividends.

The notebook follows a practical workflow:

- Load and clean the AMZN historical price data
- Perform exploratory data analysis (EDA)
- Analyze stationarity and autocorrelation
- Train baseline statistical models
- Build and train an LSTM model
- Compare predictions using evaluation metrics
- Interpret the strengths and weaknesses of each method

---

## Dataset

The dataset used in this project is the historical stock price data for Amazon (ticker `AMZN`) stored in `AMZN.csv`.

### Source and Time Range

- Time range: 1997-05-15 to 2023-04-05
- Number of rows: 6,516
- Number of features: 7

### Columns

| Column | Description |
| --- | --- |
| Date | Trading day |
| Open | Opening price of the stock for the day |
| High | Highest price reached during the day |
| Low | Lowest price reached during the day |
| Close | Closing price for the day |
| Adj Close | Adjusted closing price after accounting for splits/dividends |
| Volume | Total number of shares traded |

### Why this data is interesting

This data is a classic time-series dataset with temporal structure, trend, nonlinearity, and volatility. These properties make it suitable for comparing:

- Traditional forecasting models such as ARIMA and SARIMA
- Smoothing-based models like Exponential Smoothing
- Deep learning models like LSTM

The project also tracks daily returns, which helps visualize how the price changes over time and assess volatility.

---

## Exploratory Data Analysis

The notebook begins by converting the `Date` column to a datetime format and plotting the adjusted close price over time. The resulting chart shows the long-term growth of Amazon stock, along with periods of volatility and trend shifts.

Additional analyses include:

- Daily return plotting to inspect short-term movement
- Correlation heatmap between OHLCV variables
- Volume distribution analysis

These analyses help identify patterns in the market behavior and confirm that the data exhibits temporal dependence, which makes sequence-based models relevant.

---

## Statistical Forecasting Models

### ARIMA

ARIMA (AutoRegressive Integrated Moving Average) is a classical time-series model that uses past observations to predict future values. It captures:

- autoregression (`p`): dependence on past values
- differencing (`d`): transformation to make the series stationary
- moving average (`q`): dependence on previous forecast errors

The notebook checks stationarity using the Augmented Dickey-Fuller (ADF) test.

### SARIMA

SARIMA extends ARIMA by incorporating seasonal effects. This is useful for data with recurring patterns over time. In this notebook, SARIMA is applied to the differenced adjusted close series to see whether seasonal structure improves performance.

### Exponential Smoothing

Exponential Smoothing assigns more weight to recent observations and progressively less weight to older values. It is a useful benchmark for time-series forecasting because it can model level and trend components efficiently.

---

## LSTM Model Architecture

The notebook ultimately focuses on a deep-learning approach using an LSTM network. LSTMs are well-suited for sequential data because they can retain information over long time intervals and learn temporal dependencies that standard regression models struggle to capture.

The implemented architecture is:

- Input shape: `(samples, 1, features)`
- LSTM layer: 32 units
- Activation: `relu`
- Output layer: `Dense(1)`
- Optimizer: `Adam`
- Loss function: `mean_squared_error`
- Training epochs: `100`
- Batch size: `8`
- Shuffle: `False` (important for preserving time order)

This architecture uses the available features as input and predicts the future adjusted close value. The model is trained with a time-series split strategy rather than random shuffling to preserve the chronological order of the stock data.

### Why TimeSeriesSplit was used

A standard random train/test split would leak future information into the past. To avoid this, the notebook uses `TimeSeriesSplit`, which keeps the sequence order intact and evaluates the model in a realistic forecasting setting.

---

## Preprocessing and Training Setup

The notebook prepares the dataset for the LSTM model as follows:

- Uses `Adj Close` as the target variable
- Selects `Open`, `High`, `Low`, and `Volume` as historical features
- Scales or reshapes the data for LSTM compatibility
- Uses a sliding-window representation suited for sequence learning

The model is trained on a historical segment and evaluated on a later unseen portion of the series, which better reflects how the model would perform in real financial forecasting.

---

## Evaluation Metrics and Results

The notebook evaluates the statistical models using Mean Squared Error (MSE), which measures the average squared difference between actual and predicted values.

### ARIMA Result

The notebook reports the following ARIMA result:

- Mean Squared Error (MSE): `3467.3244840077746`

This result indicates that the ARIMA model was not highly accurate on this stock dataset.

### Interpretation

The project notes that the stock data is non-stationary and contains strong temporal structure that is difficult for standard ARIMA-type models to capture without careful differencing and tuning. Financial series often show trends, volatility, and regime shifts, which limit the predictive power of linear statistical models when used alone.

The notebook concludes that the LSTM model is better suited for this type of data because it can learn nonlinear temporal dependencies directly from the sequence.

---

## Key Findings

1. Traditional models such as ARIMA and SARIMA struggle with the non-stationary nature of stock prices.
2. Exponential Smoothing provides a simple baseline but is limited for highly nonlinear stock behavior.
3. LSTM captures temporal dependencies more effectively than the classical statistical models in this project.
4. Time-aware splitting is essential for fair evaluation in time-series forecasting.

---

## Project Structure

- `AMZN.csv`: Raw Amazon stock price dataset
- `Amazon_stock_price_prediction.ipynb`: Full notebook with preprocessing, exploration, model training, and visualization

---

## Conclusion

This project demonstrates that stock price prediction is a difficult but tractable time-series problem. While classical statistical models are useful as baselines, deep learning methods such as LSTM are often more effective when the goal is to model long-term dependencies in sequential financial data.

The notebook provides a good introduction to both traditional forecasting and deep learning techniques, making it a useful study for stock time-series analysis.

---

## Suggested Next Steps

- Add more features such as moving averages, RSI, or MACD
- Tune the LSTM architecture and hyperparameters
- Compare with GRU, BiLSTM, or Transformer-based models
- Experiment with longer prediction horizons
- Evaluate using MAE, RMSE, and R² in addition to MSE

This project is a strong starting point for learning how time-series forecasting works in real-world financial data and how neural networks can improve predictive performance over classical baselines.

