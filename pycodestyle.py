def square_numbers(nums):
    """Calculate the square of each number in a list."""
    squares = []
    for num in nums:
        squares.append(num ** 2)
    return squares
