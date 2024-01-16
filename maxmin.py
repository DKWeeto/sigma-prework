def min_max(num_list):
    min = num_list[0]
    max = num_list[0]
    for i in num_list:
        if i > max:
            max = i
        if i < min:
            min = i
    return [min, max]

print(min_max(eval(input("List: "))))