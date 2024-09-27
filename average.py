# Input from the user
numbers = input("Enter numbers separated by space: ").split()

# Convert input strings to float
numbers = [float(num) for num in numbers]

# Calculate the average
average = sum(numbers) / len(numbers)

# Find the largest and smallest numbers
largest = max(numbers)
smallest = min(numbers)

# Display the results
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
