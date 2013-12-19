Monte-Carlo-HA
==============

Monte-Carlo-HA

You work for a small health insurance company which insure 10000 people. Each insured person pays a annual premium of $150/year. Each person has a 10% chance of submitting a claim during one year and the amount of a claim is a random log-normal distributed variable (in pythonrandom.lognormvariate(mu,sigma)) with parameters mu=5 andsigma=2.1 (you know this from historical data).
The premiums are collected at the beginning of the year, all claims are paid immediately as they occur, and all profit is distributed to shareholders at the end of the year. Ignore taxes and any other cost/expense. (You are not paid a salary, you work as an unpaid intern!)

Without performing any numerical computation, what is the average total annual profit?
-	The average total annual profit is around $150,000

Perform a Monte Carlo computation to confirm the result of problem 1, using a relative target precision of 10%.

There is a probability that at the end of the year the expenses (total claims) exceed the income (total premiums).
Produce a plot showing profit as function of the simulated scenario (sorted by profit). What is the probability that this happens (use at last 100 simulated scenarios)? Explain your answer and the code to compute it.

You want to protect your company against this possibility of default by buying an option that will pay the difference between total expenses due to claims and total income from premiums, in case expenses exceed income.
What should be the cost of such option? Explain your answer and the code to compute it.

