def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    d=[]
    for i in range(1,11):
        d.append(i*price)


    return d
print(main(2.25))