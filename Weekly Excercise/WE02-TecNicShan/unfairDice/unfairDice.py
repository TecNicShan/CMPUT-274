import random

def biased_rolls(prob_list, s, n): 
    rolls = []
    random.seed(s)
    zero_to_one_list = [0]
    for x in prob_list:
        if len(zero_to_one_list) == 1:
            zero_to_one_list.append(x)
        else:
            zero_to_one_list.append(float(x+zero_to_one_list[-1]))
    
    for iterations in range(n):
        dice = random.random()
        for check in range(len(zero_to_one_list)-1):
            if zero_to_one_list[check+1]> dice >= zero_to_one_list[check]:
                rolls.append(check+1)
    return rolls


def draw_histogram(m, rolls, width):
    hist = []
    final_hist = []
    for x in range(m):
        hist.append(0)

    for r in rolls:
        hist[r-1] = hist[r-1] + 1
    scale = width/max(hist)
    scaled_list = []
    for num in hist:
        num = round(num * scale)
        scaled_list.append(num)
    
    for each in scaled_list:
        temp = []
        for x in range(each):
            temp.append("#")
        final_hist.append(temp)
    
    for dice in final_hist:
        if len(dice) != width:
            for z in range(width-len(dice)):
                dice.append("-")
    print("Frequency Histogram: "+str(m)+"-sided Die")
    for y in range(len(final_hist)):
        print(str(y+1)+"."+str("".join(final_hist[y])))


if __name__ == "__main__":

    rolls = biased_rolls([1/3, 1/3, 1/3], (2**32)-1, 1000)
    draw_histogram(3, rolls, 10)

    pass
