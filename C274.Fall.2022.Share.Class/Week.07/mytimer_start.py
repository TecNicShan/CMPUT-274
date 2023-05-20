import time
import random

class TimeObj():
    def __init__(self, msg=""):
    # Code here

    def tick(self,print_clock=False):
    # Code here

    def tock(self,print_clock=False):
    # Code here

    def __str__(self):
    # Code here


# Not the cleverest way to do this
def rand_list_ints(l,num):
    for i in range(num):
        l.append(random.randint(0,10000000))


def test_main():
    a = TimeObj("All:")

    b = TimeObj("Create:")
    my_list = []
    rand_list_ints(my_list,1000000)
    b.tock(True)

    c = TimeObj("Sort:")
    c.tick()
    my_list.sort()
    c.tock()

    print("Sorting:",c)

    a.tock(True)

if __name__ == "__main__":
    test_main()
