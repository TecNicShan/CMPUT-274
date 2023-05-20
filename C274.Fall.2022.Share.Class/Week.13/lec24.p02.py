# https://www.youtube.com/watch?v=O2L2Uv9pdDA

def epsilon(x, y, e=0.01):
    if abs(float(x)-float(y)) < e:
        return True
    else:
        return False


def main():
    norm = {}
    norm_words = 17
    norm_msg = 8

    norm[ "Dear" ] = 8
    norm[ "Friend" ] = 5
    norm[ "Lunch" ] = 3 
    norm[ "Money" ] = 1
    assert( norm_words == sum(norm.values()) ), "Does not add up"
    for w in norm.keys():
        print( "p( %s | N ) = %f" % (w, norm[w] / float(norm_words)) )


    print()

    spam = {}
    spam_words = 7
    spam_msg = 4

    spam[ "Dear" ] = 2
    spam[ "Friend" ] = 1
    spam[ "Lunch" ] = 0
    spam[ "Money" ] = 4
    assert( spam_words == sum(spam.values()) ), "Does not add up"
    for w in spam.keys():
        print( "p( %s | S ) = %f" % (w, spam[w] / float(spam_words)) )


if __name__ == "__main__":
    main()
