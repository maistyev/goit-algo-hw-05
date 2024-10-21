def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # Якщо елемент не знайдено, повертаємо верхню межу
    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]
    
    return iterations, upper_bound

# Тестуємо функцію
arr = [0.1, 0.3, 0.5, 0.7, 1.1, 1.3, 1.6, 1.9]

# Тест 1: Шукаємо існуюче значення
target = 1.1
iterations, result = binary_search(arr, target)
print(f"Шукаємо {target}:")
print(f"Кількість ітерацій: {iterations}")
print(f"Результат: {result}")

# Тест 2: Шукаємо неіснуюче значення
target = 1.0
iterations, result = binary_search(arr, target)
print(f"\nШукаємо {target}:")
print(f"Кількість ітерацій: {iterations}")
print(f"Верхня межа: {result}")

# Тест 3: Шукаємо значення більше за максимальне в масиві
target = 2.0
iterations, result = binary_search(arr, target)
print(f"\nШукаємо {target}:")
print(f"Кількість ітерацій: {iterations}")
print(f"Верхня межа: {result}")