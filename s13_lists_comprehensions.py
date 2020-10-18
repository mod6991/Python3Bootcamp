numbers = [1,2,3,4,5]
squared_numbers = [num**2 for num in numbers] # --> [1, 4, 9, 16, 25]

# With conditional logic
even_numbers = [num for num in numbers if num % 2 == 0] # --> [2, 4]
odd_numbers = [num for num in numbers if num % 2 != 0] # --> [1, 3, 5]

new_numbers = [num * 2 if num % 2 == 0 else num / 2 for num in numbers] # --> [0.5, 4, 1.5, 8, 2.5]

# Nested

multi_dim = [[1,2,3], [4,5,6], [7,8,9]]
multi_dim_squared = [[num**2 for num in li] for li in multi_dim] # --> [[1, 4, 9], [16, 25, 36], [49, 64, 81]]