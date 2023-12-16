def rotate_array(arr, k):
    k = k % len(arr)  # handle cases where k is larger than the array length
    return arr[-k:] + arr[:-k]

# Example usage
my_array = [1, 2, 3, 4, 5]
rotated_array = rotate_array(my_array, 2)
print(rotated_array)
