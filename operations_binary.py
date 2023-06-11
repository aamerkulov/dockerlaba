import os

test_value = os.getenv("test_env")
test_value = int(test_value)
print(f"Значение: {test_value}")
print(f"Сумма: {test_value+test_value}")
print(f"Квадрат: {test_value*test_value}")
print(f"Куб - {test_value*test_value*test_value}")