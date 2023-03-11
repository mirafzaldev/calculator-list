# # Bissmilahi Rohmani Rohim



from functools import reduce
import random
def generate_random_list(length):
    return [random.randint(0, 100) for _ in range(length)]

def sum_list(numbers):
    return reduce(lambda x, y: x + y, numbers)

def product_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

def average_list(numbers):
    return sum_list(numbers) / len(numbers)

def min_list(numbers):
    return reduce(lambda x, y: x if x < y else y, numbers)

def max_list(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)

# Foydalanuvchidan raqamlar royxatini kiritish yoki tasodifiy royxat yaratishni sorash
choice = input("Do you want to enter a list of numbers (Y/N)? ")
if choice.lower() == "y":
    numbers = list(map(int, input("Enter the list of numbers separated by space: ").split()))
else:
    length = int(input("Enter the length of the list: "))
    numbers = generate_random_list(length)

#Foydalanuvchidan royxatda bajariladigan operatsiyani tanlashini sorang

print("Choose the operation to perform:")
print("1. Sum of the list")
print("2. Product of the list")
print("3. Average of the list")
print("4. Minimum value in the list")
print("5. Maximum value in the list")

choice = int(input("Enter your choice: "))

# Foydalanuvchidan royxatda bajariladigan operatsiyani tanlashini sorash
if choice == 1:
    result = sum_list(numbers)
    print("Sum of the list:", result)
elif choice == 2:
    result = product_list(numbers)
    print("Product of the list:", result)
elif choice == 3:
    result = average_list(numbers)
    print("Average of the list:", result)
elif choice == 4:
    result = min_list(numbers)
    print("Minimum value in the list:", result)
elif choice == 5:
    result = max_list(numbers)
    print("Maximum value in the list:", result)
else:
    print("Invalid choice!")

