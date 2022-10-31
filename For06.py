def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    d=0
    for i in range(A,B):
       d+=i 

    return d
print(main(3,6))