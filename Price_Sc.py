import numpy as np
from scipy.stats import norm

# cannot calculate Implied Volitility well because it is based on input factors

r=float(input("enter r value here: \n"))  #risk free rate
S=int(input("enter S value here: \n"))    #current value of stock
K=int(input("enter K value here: \n"))  #Strike Price/Excerise price
T_num=int(input("enter T value (Numerator) here: \n"))  
T_sum=int(input("enter T value (Denomenator) here: \n"))
#time to maturity in years
sigma=float(input("Enter Sigma Value Here: \n"))  #volatilty of dividents of stock
Type=input("Is it a Call or a Put?  \n")

T=T_num/T_sum

def scholes(r,S,K,T,sigma,Type):
    #Price of Call or Put
    Derivative=(np.log(S/K) + (r+sigma**2/2)*T)/(sigma*np.sqrt(T))
    Derivative2=Derivative-sigma*np.sqrt(T)
    if Type=="Call":
        price= S*norm.cdf(Derivative,0,1) - K*np.exp(-r*T) * norm.cdf(Derivative2,0,1)
    elif Type=="Put":
        price=K*np.exp(-r*T)*norm.cdf(-Derivative2,0,1)-S*norm.cdf(-Derivative,0,1)
    return price
    
        
print("Option price is",round(scholes(r,S,K,T,sigma,Type),2))





