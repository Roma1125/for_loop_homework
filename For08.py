def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    d=0
    for i in range(1,N+1):
       d+=1/i 

    return d
print(main(4))