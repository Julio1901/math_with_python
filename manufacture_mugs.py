'''Ex crescimento exponencial. Um artesão se propõe durante 16 dias a dobrar
a sua produção de canecas sempre tendo como base o número de canecas produzidas
no dia anterior, considerando que ele começará no dia 0 produzindo uma única
caneca e que, irá se propor a fazer isso durante 16 dias irei demonstrar 2
eventos: 

1- A curva de crescimento exponencial
2- o número total de canecas produzidas ao final dos 16 dias
'''
import matplotlib.pyplot

total_number_of_mugs = 0
total_number_days = 16
actual_day = 1

list_of_days_with_mugs_production = []

while (actual_day <= 16):
    if total_number_of_mugs == 0:
        total_number_of_mugs += 1
        list_of_days_with_mugs_production.append(f'{actual_day} : {total_number_of_mugs}')
        actual_day+= 1
    else:
        total_number_of_mugs = (total_number_of_mugs * 2)
        #codigo duplicado aqui, eliminar
        list_of_days_with_mugs_production.append(f'{actual_day}:{total_number_of_mugs}')
        actual_day+=1

print(list_of_days_with_mugs_production)
total_registers = len(list_of_days_with_mugs_production)

total_days_list = []
total_numbers_mugs_ordened = []

counter = 0
for x in list_of_days_with_mugs_production:
    actual_register = list_of_days_with_mugs_production[counter].split(":")
    actual_day = actual_register[0]
    actual_production = actual_register[1]

    total_days_list.append(actual_day)
    actual_production = int(actual_production)
    total_numbers_mugs_ordened.append(actual_production)
    
    counter += 1

print(total_days_list)



print('Demonstrando em um gráfico')
matplotlib.pyplot.plot(total_days_list, total_numbers_mugs_ordened )

matplotlib.pyplot.show()

