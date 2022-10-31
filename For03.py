def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    g=[]
    for d in range(n):
        g.append(k)

    return g
print(main(10,10))