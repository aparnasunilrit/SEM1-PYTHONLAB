



numbers = [-10, 15, -3, 7, -25, 18, 0]
positive_numbers = [num for num in numbers if num > 0]
print("Positive numbers:", positive_numbers)

N = 5
squares = [num ** 2 for num in range(1, N + 1)]
print("Squares of first N numbers:", squares)

word = "comprehension"
vowels = [char for char in word if char in 'aeiou']
print("Vowels in the word:", vowels)

word = "ABCD"
ordinal_values = [ord(char) for char in word]
print("Ordinal values of each character:", ordinal_values)
