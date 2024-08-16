import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf

def get_data(stocks, start, end): # data imported from yahoo finance
    stockData = yf.download(stocks, start, end)
    stockData = stockData['Close']
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    if len(stocks) > 1:
        covMatrix = returns.cov()
    else:
        covMatrix = returns.var() 
    return meanReturns, covMatrix

stockList = ['TSLA', 'ENVX', 'CLPT', 'EOSE', 'VOO', 'PGY']
stocks = [stock for stock in stockList]
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)

meanReturns, covMatrix = get_data(stocks, startDate, endDate)

#print(meanReturns)

if isinstance(meanReturns, np.float64):  # Single stock case
    weights = np.array([1.0])  
    meanReturns = np.array([meanReturns])  # Convert meanReturns to an array
else:  # Multiple stocks case
    weights = np.random.random(len(meanReturns))
    weights /= np.sum(weights)  # Normalize weights 

#print(weights)

mc_sims = 10000
time = 365

meanMatrix = np.full(shape=(time, len(weights)), fill_value=meanReturns)
meanMatrix = meanMatrix.T

portfolio_sims = np.full(shape=(time, mc_sims), fill_value=0.0)

initialValue = 10000

mean = []

for m in range(0, mc_sims):
    Z = np.random.normal(size=(time, len(weights)))  # Random normal values for simulation
    if len(weights) > 1:
        L = np.linalg.cholesky(covMatrix)  # Cholesky decomposition for covariance matrix
        dailyReturns = meanMatrix + np.inner(L, Z)
        portfolio_sims[:, m] = np.cumprod(np.inner(weights, dailyReturns.T) + 1) * initialValue
    else:
        # For a single stock, handle the shapes directly
        dailyReturns = meanMatrix.flatten() + Z.flatten() * np.sqrt(covMatrix)
        portfolio_sims[:, m] = np.cumprod(dailyReturns + 1) * initialValue
    mean = [portfolio_sims[time-1]]

mean = np.mean(mean)
plt.plot(portfolio_sims)
plt.ylabel("Portfolio Value ($)")
plt.xlabel('Days')
plt.title("MC Simulation")

print(f'Your projected portfolio value in {time} days is ${mean:.2f}')
if mean >= initialValue:
    print(f'This is a {(mean-initialValue)/initialValue*100:.2f}% increase from the initial investment')
else:
    print(f'This is a {(mean-initialValue)/initialValue*100:.2f}% decrease from the initial investment')
plt.show()