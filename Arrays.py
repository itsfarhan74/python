# Create an array of integers
# import array
# arr = array.array('i', [1, 2, 3, 4, 5])
# print(arr)

# print(arr[0])
# print(arr[3])
# print(arr[1])

# import array

# arr = array.array('i',[3,4,5,6])
# print(arr)
# arr[1]=10
# print(arr)
# print(arr[2])
# print(arr[3])


# import array

# arr = array.array('i',[1,2,3,4,5])
# print(arr)

# arr.append(6)

# print(arr)

# arr.extend([7,8,9])

# print(arr)

# import array

# arr = array.array('i',[1,2,3,4,5])

# print(arr)

# arr.pop()

# print(arr)

# # arr.remove(1)

# # print(arr)

# import array

# arr = array.array('i',[1,2,3,4,5])

# print(arr)

# arr.pop()

# print(arr)

# arr.remove(1)

# print(arr)

# print(len(arr))

# import array

# arr = array.array('i',[1,2,3,4,5])

# for element in arr:
#     print(element)

#     arr.reverse()

#     print()
# import array
# arr = array.array('i', [5, 3, 8, 1, 2])
# arr = array.array('i', sorted(arr))  # Sort using sorted()
# print(arr)

# arr.sort()  # Sort using sort()
# print(arr)


# import array

# # Create an array
# arr = array.array('i', [5, 3, 8, 1, 2])

# # Find maximum and minimum values
# max_value = max(arr)
# min_value = min(arr)

# print("Maximum value:", max_value)
# print("Minimum value:", min_value)

# import array

# arr = array.array('i', [1, 2, 3, 4, 5])
# arr.reverse()

# print("Reversed array:", arr)

# import array

# def rotate_array(arr, k):
#     k = k % len(arr)
#     return arr[-k:] + arr[:-k]

# arr = array.array('i', [1, 2, 3, 4, 5])
# k = 2
# rotated_arr = rotate_array(arr, k)

# print("Rotated array:", rotated_arr)

# import array

# arr = array.array('i', [5, 3, 8, 1, 2])
# sorted_arr = sorted(arr, reverse=True)
# second_largest = sorted_arr[0]

# print("Second largest element:", second_largest)

# import array

# arr = array.array('i',[6,4,2,8,7])

# sortedArray=sorted(arr,reverse=True)

# second_largest=sortedArray[1]

# print("second largest element in array is:",second_largest)

# import array

# def is_sorted(arr):
#     for i in range(len(arr) - 1):
#         if arr[i] > arr[i + 1]:
#             return False
#     return True

# arr = array.array('i', [1, 2, 3, 4, 5])
# print("Is sorted:", is_sorted(arr))

# def rotate_array (arr,steps):
#     steps %= len(arr)
#     return arr[-steps:] + arr[:-steps]
#     print(rotate_array([1,2,3,4,5,6,7,8,9], 2 ))

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number
#         self.__balance = balance

#     def get_account_number(self):
#         return self.__account_number

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self, balance):
#         self.__balance = balance

# account = BankAccount(12345, 10000)
# print("Account Number:", account.get_account_number())
# print("Balance:", account.get_balance())


from datetime import datetime

date1 = datetime.strptime("2025-01-01", "%Y-%m-%d")
date2 = datetime.strptime("2025-01-15", "%Y-%m-%d")
delta = date2 - date1
print("Difference:", delta.days, "days")

import json

data = {"name": "Alice", "age": 20, "grade": "A"}
json_data = json.dumps(data)
python_data = json.loads(json_data)
print("Name:", python_data["name"])
print("Age:", python_data["age"])
print("Grade:", python_data["grade"])