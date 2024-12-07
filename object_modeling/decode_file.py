def decode(message_file):
    my_data = {}
    with open(message_file) as fh:
        for line in fh:
            num, word = line.split()
            if line == "":
                continue
            my_data[int(num)] = word

    sentence = ""
    i = 0
    count = 0
    print (my_data)
    while count < len(my_data):
        count = count + i + 1 # 1, 3, 3+2+1,
        sentence = sentence + " " + my_data[count]
        i += 1

    return sentence


message_file = 'coding_qual_input.txt' 
print(decode(message_file))