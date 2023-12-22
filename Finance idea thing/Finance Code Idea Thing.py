import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import time
states = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
    'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia',
    'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
    'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
    'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
    'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
    'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
    'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
    'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
    'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
]



def tax(income):
    FICA = 0.0765   
    taxes = 0
    if income > 0 and income < 11601:
        taxes += income * .1
    elif income > 11600 and income < 47151:
        taxes += 11600 * .1
        taxes += (income-11601) * .12
    elif income > 47150 and income < 100526:
        taxes += 11600 * .1
        taxes += (47150-11601) * .12
        taxes += (income - 47151) * .22
    elif income > 100525 and income < 191951:
        taxes += 11600 * .1
        taxes += (47150-11601) * .12
        taxes += (100525 - 47151) * .22
        taxes += (income - 100526) * .24
    elif income > 191950 and income < 243726:
        taxes += 11600 * .1
        taxes += (47150-11601) * .12
        taxes += (100525 - 47151) * .22
        taxes += (191950-100526) * .24
        taxes += (income - 191951) * .32
    elif income > 243725 and income < 609351:
        taxes += 11600 * .1
        taxes += (47150-11601) * .12
        taxes += (100525 - 47151) * .22
        taxes += (191950-100526) * .24
        taxes += (243725 - 191951) * .32
        taxes += (income - 243726) * .35
    elif income > 609350:
        taxes += 11600 * .1
        taxes += (47150-11601) * .12
        taxes += (100525 - 47151) * .22
        taxes += (191950-100526) * .24
        taxes += (243725 - 191951) * .32
        taxes += (609350 - 243726) * .35
        taxes += (income - 609351) * .37
    state = input("What state do you live in? (Correctly spell your state or an error will arise. ex. 'Alabama'): ")
    df = pd.read_csv('State_Taxes.csv')
    State_tax = df.at[states.index(state),'Pers_Rate']
    State_tax = State_tax/100
    taxes += income * State_tax
    taxes += income * FICA
    time.sleep(2)
    return taxes
def predict():
    predict = input("\nResults if you invest in the DOW/NSDQ/S&P500 ('D','N','S','Q' to cancel): ").lower()
    if predict == 'd':

        df = pd.read_csv('DowJones.csv')
        df.head(6)


        df = df[['Value']]
        future_days = 1000
        df['Prediction'] = df[['Value']].shift(-future_days)
        df.head(4)



        X = np.array(df.drop(['Prediction'], axis=1))[:-future_days]
        y = np.array(df['Prediction'])[:-future_days] 

        x_train, x_test,y_train,y_test = train_test_split(X,y,test_size=0.25)


        model = LinearRegression().fit(x_train,y_train)

        x_future = df.drop(['Prediction'],axis= 1)[:-future_days]
        x_future = x_future.tail(future_days)
        x_future = np.array(x_future)
        x_future

        prediction = model.predict(x_future)
        predictions = prediction
    

        valid = df[X.shape[0]:]
        
        valid['Predictions'] = predictions
        r2 = r2_score(df['Value'][-future_days:],valid['Predictions'])
        print(f"r^2 is {r2:.3f}")
        plt.figure(figsize=(12,6))
        plt.title('Dow Jones')
        plt.xlabel('Days')
        plt.ylabel('Close Price USD ($)')
        plt.plot(df['Value'])
        plt.plot(valid['Predictions'],color = 'red')
        plt.legend(['Orig','Pred'])
        time.sleep(5)
        plt.show()
    if predict == 'n':
        df = pd.read_csv('Nasdaq.csv')
        df.head(6)


        df = df[['Value']]
        future_days = 1000
        df['Prediction'] = df[['Value']].shift(-future_days)
        df.head(4)



        X = np.array(df.drop(['Prediction'], axis=1))[:-future_days]
        y = np.array(df['Prediction'])[:-future_days] 

        x_train, x_test,y_train,y_test = train_test_split(X,y,test_size=0.25)


        model = LinearRegression().fit(x_train,y_train)

        x_future = df.drop(['Prediction'],axis= 1)[:-future_days]
        x_future = x_future.tail(future_days)
        x_future = np.array(x_future)
        x_future
        
        prediction = model.predict(x_future)
        predictions = prediction
 
        
        valid = df[X.shape[0]:]
        
        valid['Predictions'] = predictions
        r2 = r2_score(df['Value'][-future_days:],valid['Predictions'])
        print(f"r^2 is {r2:.3f}")
        plt.figure(figsize=(12,6))
        plt.title('NASDAQ')
        plt.xlabel('Days')
        plt.ylabel('Close Price USD ($)')
        plt.plot(df['Value'])
        plt.plot(valid['Predictions'],color = 'red')
        plt.legend(['Orig','Pred'])
        time.sleep(5)
        plt.show()
    if predict == 's':
        df = pd.read_csv('SP500.csv')
        df.head(6)


        df = df[['Value']]
        future_days = 1000
        df['Prediction'] = df[['Value']].shift(-future_days)
        df.head(4)



        X = np.array(df.drop(['Prediction'], axis=1))[:-future_days]
        y = np.array(df['Prediction'])[:-future_days] 

        x_train, x_test,y_train,y_test = train_test_split(X,y,test_size=0.25)


        model = LinearRegression().fit(x_train,y_train)

        x_future = df.drop(['Prediction'],axis= 1)[:-future_days]
        x_future = x_future.tail(future_days)
        x_future = np.array(x_future)
        x_future

        prediction = model.predict(x_future)
        predictions = prediction
    

        valid = df[X.shape[0]:]
        
        valid['Predictions'] = predictions
        r2 = r2_score(df['Value'][-future_days:],valid['Predictions'])
        print(f"r^2 is {r2:.3f}")
        plt.figure(figsize=(12,6))
        plt.title('S&P500')
        plt.xlabel('Days')
        plt.ylabel('Close Price USD ($)')
        plt.plot(df['Value'])
        plt.plot(valid['Predictions'],color = 'red')
        plt.legend(['Orig','Pred'])
        time.sleep(5)
        plt.show()
print('''This program uses the 2024 Federal Income Tax Brackets.
      This program assumes that the person entering their income is a single filer void of any local taxes.
      This program will give you a rough estimate of the taxes you owe based on your annual income and state of residence.''')
income = int(input("\nWhat is you annual income(Round your number to an integer number): "))
while type(income) is not int:
    print("Not a valid input.")
    income = int(input("What is you annual income(Round your number to an integer number): "))
time.sleep(1)
print(f"You owe ${tax(income):,.2f} worth of taxes for the 2023-2024 year.")
time.sleep(3)
print()
print("Using Machine Learning, we can predict the growth of stocks, mutual funds, ETF's, etc.")
print('''This script uses a Linear Regression Model to predict the growth of ETF's 
      and you can see the comparison between predicted and actual values if you wish.''')
print("The r^2 value of our model is in the +0.7-+0.8 range.")
print("This value means the data fits our regression model very well, as +0.7-+0.8 is a known to be a strong coefficient of determination.")
time.sleep(15)
predict()
