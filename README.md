# Monte Carlo Portfolio Simulation

This project performs a Monte Carlo simulation to estimate the future value of an investment portfolio composed of a single stock or multiple stocks. The simulation utilizes historical stock data to model potential future returns and assesses the likelihood of various outcomes.

## Project Description

This project fetches historical stock data for a given set of stocks from Yahoo Finance to estimate the portfolio's mean returns and covariance matrix. The Monte Carlo simulation is then run to project the portfolio's value over a specified period, providing insight into the range of possible outcomes based on historical data.

### Technologies Used:
- **Python**: The core programming language used for the project.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Matplotlib**: For plotting the simulation results.
- **yfinance**: For fetching historical stock data from Yahoo Finance.


### Some Possible Future Enhancements:
- **User Interface**: Adding a graphical user interface to allow users to input stock symbols and adjust parameters without editing the code.
- **Advanced Analytics**: Implementing additional risk metrics like Value at Risk or Conditional Value at Risk.

## How to Install and Run the Project

To install and run this project locally, follow these steps:

1. **Clone the Repository:**


   ```bash
   git clone https://github.com/evangruhlkey/MC_Simulation.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd MC_Simulation
   ```
3. **Run the Project:**
   ```bash
   python Monte_Carlo_Simulation.py
   ```

## How to Use the Project
**Input Stock Symbols:**

  - In the stockList variable within the script, input the stock symbols you wish to simulate.
    
    ![image](https://github.com/user-attachments/assets/a881e46b-e7e4-478e-8f46-efe49d521f5b)

  
**Adjust Simulation Parameters:**

- Modify the mc_sims variable to change the number of Monte Carlo simulations.
- Modify the time variable to change the number of days for the simulation.
  
  ![image](https://github.com/user-attachments/assets/55588d26-8166-4e39-86cb-51cea912f6bc)


**View Results:**

- The script will output the projected portfolio value after the simulation period and display a plot of the simulated portfolio paths.

  ![MC Simulation](https://github.com/user-attachments/assets/3236126c-6cdd-47c2-8a41-0940636e9980)

  ![image](https://github.com/user-attachments/assets/6d8b22e0-ea7a-469e-9a8a-9228f3999498)

   

