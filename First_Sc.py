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
def First_scholes(r,S,K,T,sigma):
    
   
    Derivative=(np.log(S/K) + (r+(sigma**2/2))*T)/(sigma*np.sqrt(T))
    
    Vega=(S*np.sqrt(T)*norm.pdf(Derivative))
    #problem was  derivative of distribution
    return Vega
 #try to integrate gamma spot   
print("Vega is: {} or {}".format(round(First_scholes(r,S,K,T,sigma),4),(round(First_scholes(r,S,K,T,sigma),4)*.01)))