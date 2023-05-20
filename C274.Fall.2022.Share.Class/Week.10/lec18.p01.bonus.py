# ins = input().strip()
ins = "She sells seashells by the seashore"

print("len: ", len(ins))
ll = list(ins)
print(ll)

huffman = dict()
huffman[' '] = "000"
huffman['e'] = "001"

huffman['S'] = "01000"
huffman['y'] = "01001"

huffman['o'] = "01010"
huffman['r'] = "01011"

huffman['l'] = "01011"

huffman['a'] = "1000"
huffman['b'] = "10010"
huffman['t'] = "10011"

huffman['h'] = "101"
huffman['s'] = "11"

# print("start")
code = ""
for c in ll:
    print(c)
    print(huffman[c])
    code += huffman[c]
# print("done")
print("%d bits, %d bytes" % (len(code),  len(code)/ 8.0 ) )
print(len(code), " bits: ", code)
