
def bubble_sort(arr):
    """Sorts a list using the bubble sort algorithm."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def is_palindrome(s):
    """Checks if a string is a palindrome."""
    return s == s[::-1]

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Returns the factorial of a number."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    """Returns the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Returns the least common multiple of a and b."""
    return abs(a * b) // gcd(a, b)

def is_armstrong(n):
    """Checks if a number is an Armstrong number."""
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))

def is_even(n):
    """Checks if a number is even."""
    return n % 2 == 0

def is_odd(n):
    """Checks if a number is odd."""
    return n % 2 != 0

def reverse_string(s):
    """Reverses a string."""
    return s[::-1]

def count_vowels(s):
    """Counts the number of vowels in a string."""
    return sum(1 for char in s.lower() if char in 'aeiou')

def is_anagram(s1, s2):
    """Checks if two strings are anagrams."""
    return sorted(s1) == sorted(s2)

def power(base, exponent):
    """Calculates base raised to the power of exponent."""
    return base ** exponent

def sum_of_digits(n):
    """Returns the sum of digits of a number."""
    return sum(int(digit) for digit in str(n))

def binary_search(arr, target):
    """Performs binary search on a sorted array."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def selection_sort(arr):
    """Sorts a list using the selection sort algorithm."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """Sorts a list using the insertion sort algorithm."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quicksort(arr):
    """Sorts a list using the quicksort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def merge_sort(arr):
    """Sorts a list using the merge sort algorithm."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """Helper function for merge sort."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def max_in_list(lst):
    """Returns the maximum value in a list."""
    return max(lst)

def min_in_list(lst):
    """Returns the minimum value in a list."""
    return min(lst)

def average(lst):
    """Returns the average of a list of numbers."""
    return sum(lst) / len(lst)

def median(lst):
    """Returns the median of a list of numbers."""
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def mode(lst):
    """Returns the mode of a list of numbers."""
    from collections import Counter
    counts = Counter(lst)
    max_count = max(counts.values())
    return [key for key, count in counts.items() if count == max_count]

def is_perfect_square(n):
    """Checks if a number is a perfect square."""
    return int(n**0.5)**2 == n

def gcd_list(numbers):
    """Finds the GCD of a list of numbers."""
    from functools import reduce
    return reduce(gcd, numbers)

def square(n):
    """Returns the square of a number."""
    return n * n

def cube(n):
    """Returns the cube of a number."""
    return n * n * n
