def hypotenuse(a,o):
    # h^2 = a^2 + o^2
    h = ((float(a)**2) + float(o)**2) ** 0.5
    return(h)

def pythago(a=-1,o=-1,h=-1):
    # h^2 = a^2 + o^2
    if a == -1:
        a = (h**2 - o**2) ** 0.5
        return(a)
    if o == -1:
        o = (h**2 - a**2) ** 0.5
        return(o)
    if h == -1:
        h = (a**2 + o**2) ** 0.5
        return(h)

    pass

if __name__ == "__main__":
    print(hypotenuse(3,4))
    print(pythago(h=5,o=4))
