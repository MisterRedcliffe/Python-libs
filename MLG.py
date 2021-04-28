# loop back to this point once code finishes
loop = 1
while(loop < 10):
    # All the questions that the program ask the user
    noun = input("Choose a noun: ")
    plural_noun = input("Choose a plural noun: ")
    noun_2 = input("Choose another noun: ")
    place = input("Name a place: ")
    adj = input("Choose an adjective or description word: ")
    noun_3 = input("Choose a third noun: ")
    # The story
    print("--------------------")
    print("Be kind to your", noun, "-footed", plural_noun)
    print("For a duck may be somebody's", noun_2, ",")
    print("Be kind to your", plural_noun, "in", place)
    print("Where the weather is always", adj, ".")
    print()
    print("You may think that is this the", noun_3, ",")
    print("Well it is.")
    print("--------------------")
    //loop back to "loop = 1"
    loop = loop + 1
