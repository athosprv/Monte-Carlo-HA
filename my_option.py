'''
========
Problem:
========
Consider the following option on this stock. The option expires in 120 days.
The option pays you $1 if the stock's price at expiration is between $101 and
$105. The option pays $2 if the stock's price at expiration is greater than
$105. The option pays you $3 if the stock's price exceeds $105 within the
first 60 days.
-----------------------------------------------------------------------------
===================
Solution & Results:
===================
1)
Is this is a non path dependent option, a weakly path dependent,or a strongly
path dependent option?

This option is weak path dependent since there is a case where the option pays
you $3 if the stock's price exceeds $105 within the first 60 days.

2)
How long does it take to run the program with a precision of 16cents?
How long does it take to run the program with a precision of 8cents?
How long does it take to run the program with a precision of 4cents?
How long does it take to run the program with a precision of 2cents?

Run Time (in seconds) for
16 cents:  0.0249998569489
8 cents:  0.116000175476
4 cents:  0.332999944687
2 cents:  1.21199989319


3)
What is a fair price for the option (requires a target absolute precision of 8cents)?
$ 102.95027429

4)
What is the price if the yearly volatility is increased to 40%?
$ 104.445058211

5)
What is the price if the yearly volatility is decreased to 10%?
$ 101.524911838

=====
Code:
=====
'''
from math import *
import time
from storage import Storage
from mc import MCSimulator
from random import *
#from plots import *

class StockSimulator(MCSimulator):
    u = []  # Vector to hold all final prices at the end of each run of 120 days.
    def simulate_once(self):
        params=self.params
        mu = params.mu
        sigma=params.sigma
        dt = params.dt
        T = params.T
        F = params.F
        r_free = params.r_free
        t = 0.0
        S = params.S # price of the stock at time 0.
        history = [S]
        while True:
            t = t+dt
            #   Weiner Process takes place here.
            day_log_ret = gauss(mu*dt,sigma*sqrt(dt))            
            S = S*exp(day_log_ret)
            #print S 
            history.append(S)            
            if t>= T: break
        self.u.append(history[-1])  #   Each Price is appended.
        #print 'Price', history[-1]
        return params.option(history,params)*exp(-r_free*T) 

#   Our custom option for stock XXX.
def current_option(history,params):
    #   If within the 60 first days price has gone over $105 we return 3.
    for i in range(60):
        if(history[i]>105): return 3
    #   If the stock at expiration is between $101 and $105 we return 1.
    if 105>=history[-1]>=101: return 1
    #   If the stock at expiration is over $105 we return 2.
    elif history[-1]>105: return 2
    else: return 0

#   Variables are initialized here.
params=Storage()
params.mu = 0.03/300 # avg daily return.
params.sigma = 0.2/sqrt(300) # avg daily volatility.
params.S = 100.0 # today's stock price.
params.option=current_option
params.T = 120 # time to expiration.
params.r_free = 0.04/300 # avg daily risk free rate.

params.dt = 1.0 # simulation step.

#   StockSimulator Object is initialized.
s = StockSimulator(params)

# Plotting is disabled for the purpose of this program.
#plot(dict(data=[x for x in enumerate(r)]))

#  Simulating to get the price for different volatility values or absolute precision.
#   Run times for program are slightly faster when commented out.
print s.simulate_many(absolute_precision = 0.00, relative_precision=0.02, max_iterations=10000)
#print 'Price: $',sum(s.u)/len(s.u)

#    Simulating different values for relative precision.
precision = 0.32
print "Run Time (in seconds) for"
for i in range(4):
    t = time.time()
    precision = precision/2
    s.simulate_many(absolute_precision=0.0,
                         relative_precision=precision,
                         max_iterations=10000)
    print int(precision*100),'cents: ', time.time()-t

