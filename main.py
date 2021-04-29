'''
   insert here the class after construct her
'''


from calculate_exponential_growth import *

total_months = input('Enter the number of months for which the calculation will be applied: ')

percentage_of_growth = input('Enter the percentage of growth: ')

initial_number = input ('Enter the initial number (The number of day one)')


calculate = CalculateExponentialGrowth()

calculate.calculateExponentialGrowth(total_months, percentage_of_growth,
initial_number)

