import random
import logging

logging.basicConfig(level=logging.INFO)

def generate_random_list(length):
    return [random.randint(1, 100) for _ in range(length)]

def find_max(numbers):
    # TODO: Implement this function to find and return the maximum number in the list
    # Use print statements to debug your implementation
    pass

def sort_list(numbers):
    # TODO: Implement this function to sort the list in ascending order
    # Use logging to output the number of comparisons and swaps
    pass

def calculate_average(numbers):
    # TODO: Implement this function to calculate and return the average of the numbers
    # Use print statements to debug your implementation
    pass

def main():
    numbers = generate_random_list(10)
    print("Original list:", numbers)

    max_num = find_max(numbers)
    print("Maximum number:", max_num)

    sorted_numbers = sort_list(numbers.copy())
    print("Sorted list:", sorted_numbers)

    average = calculate_average(numbers)
    print("Average:", average)

if __name__ == "__main__":
    main()
