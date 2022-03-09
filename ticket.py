ticket = int(input('Какое кол-во билетов Вы хотите приобрести?'))
price = []
for i in range(1, ticket + 1):
    age = int(input(f"Возраст {1} участника "))
    if age < 18:
        price.append(0)
    elif 18 < age < 25:
        price.append(990)
    elif age > 25:
        price.append(1390)
print(price)
if ticket > 3:
    a = int(sum(price) - sum(price)/10)
    print("Сумма Вашей покупки составляет: " , a)
else:
    a = sum(price)
    print ("Сумма Вашей покупки составляет: ", a)
print(price)