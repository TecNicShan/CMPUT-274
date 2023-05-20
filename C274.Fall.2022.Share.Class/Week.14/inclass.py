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


    # p( F_1 | C ) == p( "Dear" | Normal )
    norm1 = norm[ "Dear" ] / float(norm_words)
    # p( F_2 | C ) == p( "Fried" | Normal )
    norm2 = norm[ "Friend" ] / float(norm_words)
    norm1 = norm1 *  norm2
    print( "Likelihood: ", norm1)

    # TODO: answer_norm_prob = float(norm_msg/(norm_msg+spam_msg) )
    # p(n)
    p_N = norm_msg / float(norm_msg + spam_msg)
    print( "Prior: ", p_N)
    print( "Posterior: ", p_N * norm1)

    # p( F_1 | Spam ) == p( "Dear" | Spam )
    spam1 = spam[ "Dear" ] / float(spam_words)
    # p( F_2 | Spam ) == p( "Fried" | Normal )
    spam2 = spam[ "Friend" ] / float(spam_words)
    spam1 = spam1 *  spam2
    print( "Likelihood: ", spam1)

    # p(n)
    p_S = spam_msg / float(norm_msg + spam_msg)
    print( "Prior: ", p_S)
    print( "Posterior: ", p_S * spam1)

    # argmax C
    if (p_N * norm1) > (p_S * spam1):
        print( "Normal")
    else:
        print( "Spam")

if __name__ == "__main__":
    main()
