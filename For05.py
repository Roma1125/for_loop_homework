def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    d=[]
    for i in range(A,B+1):
        d.append(i)

    return d[::-1]
print(main(2,7))