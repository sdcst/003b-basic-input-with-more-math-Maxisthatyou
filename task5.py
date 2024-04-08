#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days

pop = float(input("Please enter the current population> "))
rate = float(input("Please enter the grouth rate in percentage> "))
days = float(input("Please enter the number of days> "))

future = pop * ( 1 + (rate / 100) ) ** ( days / 365 )
future = round(future)
days = round(days)
print(f"There will be {future} people after {days} days.")

