class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment
    
    def salary(self):
        return self.hours * self.hourly_payment
    
# Проверка

print("Тест 1: Обычное создание сотрудника")
emp1 = EmployeeSalary("Анна", 35, 2, "anna@test.com")
print(f"Имя: {emp1.name}")
print(f"Часы: {emp1.hours}")
print(f"Выходные: {emp1.rest_days}")
print(f"Email: {emp1.email}")
print(f"Зарплата: {emp1.salary()} руб.")
print()

print("Тест 2: Создание через get_hours (часы неизвестны)")
emp2 = EmployeeSalary.get_hours("Иван", 2, "ivan@test.com")
print(f"Имя: {emp2.name}")
print(f"Рассчитанные часы: {emp2.hours}")
print(f"Выходные: {emp2.rest_days}")
print(f"Email: {emp2.email}")
print(f"Зарплата: {emp2.salary()} руб.")
print()

print("Тест 3: Создание через get_email (email неизвестен)")
emp3 = EmployeeSalary.get_email("Мария", 38, 1)
print(f"Имя: {emp3.name}")
print(f"Часы: {emp3.hours}")
print(f"Выходные: {emp3.rest_days}")
print(f"Сгенерированный email: {emp3.email}")
print(f"Зарплата: {emp3.salary()} руб.")
print()

print("Тест 4: Изменение почасовой оплаты")
print(f"Старая ставка: {EmployeeSalary.hourly_payment}")
EmployeeSalary.set_hourly_payment(500)
print(f"Новая ставка: {EmployeeSalary.hourly_payment}")
print(f"Зарплата Анны (35ч): {emp1.salary()} руб.")
print(f"Зарплата Ивана (40ч): {emp2.salary()} руб.")
print()