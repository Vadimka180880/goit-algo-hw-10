import pulp

# Створюємо модель
model = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

# Оголошуємо змінні
x = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
y = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

# Цільова функція
model += x + y, "Total Drinks Produced"

# Обмеження
model += 2 * x + y <= 100, "Water Constraint"
model += x <= 50, "Sugar Constraint"
model += x <= 30, "LemonJuice Constraint"
model += 2 * y <= 40, "FruitPuree Constraint"

# Розв'язуємо задачу
model.solve()

# Виводимо результати
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade Produced: {pulp.value(x)} units")
print(f"Fruit Juice Produced: {pulp.value(y)} units")
print(f"Total Drinks Produced: {pulp.value(model.objective)} units")
