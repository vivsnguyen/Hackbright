def get_produce_info(day, file):
    """hello"""

    print("Day ",day)
    the_file = open(file)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')
    #    print(words)

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()
    return 


get_produce_info(1, "um-deliveries-20140519.txt")
get_produce_info(2, "um-deliveries-20140520.txt")
get_produce_info(3, "um-deliveries-20140521.txt")