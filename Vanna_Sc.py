import numpy as np
from scipy.stats import norm

# cannot calculate Implied Volitility well because it is based on input factors

r=float(input("enter r value here: \n"))  #risk free rate
S=float(input("enter S value here: \n"))    #current value of stock
K=float(input("enter K value here: \n"))  #Strike Price/Excerise price
T_num=int(input("enter T value (Numerator) here: \n"))  # time to maturity in years
sigma=float(input("Enter Sigma Value Here: \n"))  #volatilty of dividents of stock(IV)

q=float(input("Enter Dividend rate Here: \n"))
T=T_num/365

#Call and put are same to to put call parity partial derivative
def Second_scholes(r,S,K,T,sigma):
     #difference between two is the introduction of q (dividend stock value)

     #integrate try statement into function for dividend stock

    #original function
    #Derivative=(np.log(S/K) + (r+(sigma**2/2))*T)/(sigma*np.sqrt(T))
    #Derivative2=Derivative-sigma*np.sqrt(T)
    #Vega=(S*np.sqrt(T)*norm.pdf(Derivative))
    #Vanna=Vega*((Derivative2)/(S*sigma))

    #functions with dividends
    Derivative=(np.log(S/K) + (r-q+(sigma**2/2))*T)/(sigma*np.sqrt(T))
    Derivative2=Derivative-sigma*np.sqrt(T)
    Vega=((np.exp(-q*T))*S*np.sqrt(T)*norm.pdf(Derivative))
    #Vanna=abs(Vega*((Derivative2)/(S*sigma)))
    Vanna=((-(np.exp(-q*T))*norm.pdf(Derivative))*Derivative2)/sigma
    return Vanna


print("Vanna is: {} or {}".format(round(Second_scholes(r,S,K,T,sigma),4),(round(Second_scholes(r,S,K,T,sigma),4)*.01)))
