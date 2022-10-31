

def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    d=[]
    for s in range(n):
        d.append(str(s))


        
    
    
    return ','.join(d)
print( (main(45)))