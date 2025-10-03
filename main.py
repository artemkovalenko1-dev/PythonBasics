import random  # Import the random module to generate random numbers

# Generate a list of 100 random integers between 0 and 1000
random_numbers = [random.randint(0, 1000) for _ in range(100)]

# Function to sort a list in ascending order using selection sort
def selection_sort(lst):
    # Loop through each element in the list
    for i in range(len(lst)):
        min_idx = i  # Assume the current position has the minimum value
        # Find the index of the smallest element in the remaining unsorted portion
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        # Swap the found minimum element with the current element
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

# Sort the list using the custom selection_sort function
sorted_numbers = selection_sort(random_numbers.copy())

# Separate the sorted numbers into even and odd lists
even_numbers = [num for num in sorted_numbers if num % 2 == 0]
odd_numbers = [num for num in sorted_numbers if num % 2 != 0]

# Calculate the average of even numbers if the list isn't empty
if even_numbers:
    even_average = sum(even_numbers) / len(even_numbers)
else:
    even_average = 0  # Avoid division by zero

# Calculate the average of odd numbers if the list isn't empty
if odd_numbers:
    odd_average = sum(odd_numbers) / len(odd_numbers)
else:
    odd_average = 0  # Avoid division by zero

# Print the calculated averages to the console
print(f"Average of even numbers: {even_average}")
print(f"Average of odd numbers: {odd_average}")