intput_data = input()

unique_counter = sum([1 for char in intput_data if intput_data.count(char) == 1])

if unique_counter > 10:
    print(True)
else:
    print(False)
