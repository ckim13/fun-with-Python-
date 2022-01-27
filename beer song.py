#when executed  counts beer from 99 to 0 and displays the output.
word = "bottles"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("take one down.")
    print("pass it around.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottles"
        print(new_num, word, "of beer on the wall.")
    print()
