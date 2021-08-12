import numpy as np
from scipy.stats import norm
sigma=.3
up_state=0
down_state=0
r=float(input("enter r value here: \n"))  #risk free rate
S=int(input("enter S value here: \n"))    #current value of stock
K=int(input("enter K value here: \n"))  #Strike Price/Excerise price
T_num=int(input("enter T value (Numerator) here: \n"))  
T=T_num/365
n=5
#time to maturity in years
def binomialMethod(T,S,K,r,sigma,n):
    
    dt=T/n
    for n in range(1,4):
        up_state=S*np.exp(sigma*np.sqrt(dt))
        down_state=1/up_state
        #middle_state=(np.exp((r*T)/n)-down_state)/(up_state-down_state)
        Binomial_tree=np.zeros([n+1,n+1])

        for i in range(n+1):
            for j in range(i+1):
                Binomial_tree[i,j]=S*down_state**j*up_state**(i-j)
        return Binomial_tree
