# STOCK PRICE PREDICTION
This is a kaggle dataset that contains the historical stock prices of Amazon from 1997 to 2024. The columns in the dataset are "Date" , "Open" , "High" , "Low" , "Close" , "Adj Close" and "Volume". This dataset could be used for implementing timeseries analysis.
# ARIMA / SARIMA
ARIMA : AutoRegressive Integrated Moving Average and SARIMA (Seasonal ARIMA) are two popular statistical models used to forecast future values in a time series based on past data. These models are widely used in finance, economics, and other fields to analyze and predict patterns in data. 
# Exponential Smoothing
ES assigns more weight to more recent observations, and less weight to older observations. The weight decreases exponentially as the observations get older. This is why it's called Exponential Smoothing.
# Long Short Term Memory
LSTM networks are an extension of RNN which are designed to handle long sequence of data patterns. LSTM's overcome the drawbacks suffered by RNN. A RNN network suffers from vanishing gradient problem. When the neural network back propagates, weights are being assigned to the gradients. As it proceeds to further timesteps, the gradients diminishes. LSTM's capture the temporal dependencies in the data and handles the vanishing gradients. 

# Closing thoughts 
ARIMA / SARIMA fails to make accurate predictions on the stock price dataset because the dataset is left-skewed and it is non-stationary ( no constant mean, variance observed over different time periods ). Even differentiating did not help in accurate predictions. But a simple LSTM model captures the temporal dependencies and makes accurate predictions on the test dataset. While training the LSTM, the dataset was split using timeseries split from scikit-learn. Unlike the conventional way of splitting the dataset after random shuffling, the timeseries split maintains the temporal ordering of the data since the sequence of data points matter !
