def reverse_list(input_list):
    """
    Reverse the provided list.

    Parameters:
    - input_list (list): The input list to be reversed.

    Returns:
    - list: The reversed list.
    """
    return input_list[::-1]

# Example usage:
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)

print("Original List:", original_list)
print("Reversed List:", reversed_list)
