import numpy as np
from scipy.stats import norm
#Try integrating Partial Derivatives into code

r=float(input("enter r value here: \n"))  #risk free rate
S=float(input("enter S value here: \n"))    #current value of stock
K=float(input("enter K value here: \n"))  #Strike Price/Excerise price
T_num=int(input("enter T value (Numerator) here: \n"))  
#T_sum=int(input("enter T value (Denomenator) here: \n"))
#time to maturity in years
#sigma=float(input("Enter Sigma Value Here: \n"))  #volatilty of dividents of stock
expected_price=float(input("enter Current option price here:\n"))
Type=input("Is it a Call or a Put?  \n")
sigma=0
T=T_num/365
i=0

def sigma_scholes(r,S,K,T,Type):
    price=0
    for i in range(1,10000000):
        if (expected_price<=price):
            break
        else:
            sigma=i/10000
            #print(sigma)
            Derivative=(np.log(S/K) + (r+sigma**2/2)*T)/(sigma*np.sqrt(T))
            Derivative2=Derivative-sigma*np.sqrt(T)
            try:
                if Type=="Call":
                    price= S*norm.cdf(Derivative,0,1) - K*np.exp(-r*T) * norm.cdf(Derivative2,0,1)
                    
                elif Type=="Put":
                    price=K*np.exp(-r*T)*norm.cdf(-Derivative2,0,1)-S*norm.cdf(-Derivative,0,1)
            except:
                print("Type Parameter is wrong")
    
    return sigma
    

print("Implied Volatility is: {}%".format(round(sigma_scholes(r,S,K,T,Type),4)*100))
            
