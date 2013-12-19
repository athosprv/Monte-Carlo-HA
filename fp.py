from math import *
import time
from storage import Storage
from mc import MCSimulator
from random import *
from plots import *

class HealthInsuranceSim(MCSimulator):
    
    num_claims = 0
    u = []    
    def simulate_once(self):
        
        params=self.params
        drivers = params.num_drivers
        balance = params.total_balance        
        mu = params.mu
        sigma=params.sigma
        dt = params.dt
        T = params.T
        t = 0.0
        v = []


        # Simulate a year
        while True:
            t = t+dt
            if t> T: break
            drivers_claimed = 0
            # Simulate a day
            for i in range(drivers):
                claim_chance = randint(1,3650)                
                if claim_chance==1:                
                    balance -= lognormvariate(mu,sigma)
                    self.num_claims+=1
                    drivers_claimed+=1
            drivers-=drivers_claimed
        
        #print total_balance
        #self.num_claims = 0
        self.u.append(balance);
       
        return balance

params=Storage()
params.mu = 5
params.sigma = 2.1
params.T = 365 # time to expiration.
params.dt = 1.0 # simulation step.
params.num_drivers = 10000 # Number of total drivers.
params.total_balance = params.num_drivers*150 # Value of the total Premiums.


h = HealthInsuranceSim(params)

print 'Problem 1: Average Total Annual profit', 1500000 - exp(5.0 + ((2.1)*(2.1))/2)*1000
print 'Problem 2:', h.simulate_many(absolute_precision = 0.1 , max_iterations= 2)
print 'Claims: ', h.num_claims

print 'Problem X: Better Average Total Annual profit', 1500000*2 - exp(5.0 + ((2.1)*(2.1))/2)*h.num_claims

#print (75000000 - 47318* exp(5.0 + ((2.1)*(2.1))/2))/50 # 226062.512079
#print (75000000 - 50000* exp(5.0 + ((2.1)*(2.1))/2))/50 # 226062.512079

h.u.sort()
print 'Problem 3:',plot(dict(data=[x for x in enumerate(self.u)]))





