v = int(input("Выручка фирмы: "))
i = int(input("Издержки фирмы: "))

if v>i:
    print("Фирма получает прибыль")
    print(f"Рентабельность выручки: {v/i:.2f}")
    ch = int(input("Введите численность сотрудников: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника: {v/i/ch:.2f}")
else:
    print("Фирма работает в убыток")

