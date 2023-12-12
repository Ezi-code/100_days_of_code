def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    missing_number = total_sum - actual_sum
    return missing_number

# Example usage
array = [1, 2, 3, 5, 6]
missing_number = find_missing_number(array)
print("Missing number:", missing_number)
