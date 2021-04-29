class CalculateExponentialGrowth():
    def __init__(self):
        pass

    def calculateExponentialGrowth(self, total_months, percentage_of_growth,
    initial_number):
        import matplotlib.pyplot
        import matplotlib.pyplot as plt

        total_months = int(total_months)
        percentage_of_growth = int (percentage_of_growth)
        initial_number = int (initial_number)
        all_values = []
        all_months = []
        counter = 1

        while (counter <= total_months):
            all_values.append(initial_number)
            initial_number = ( initial_number + ((initial_number/100) * percentage_of_growth))
            all_months.append(counter)
            counter += 1
        
        print(all_months)
        print(all_values)
        matplotlib.pyplot.plot(all_months, all_values)
        matplotlib.pyplot.show()



