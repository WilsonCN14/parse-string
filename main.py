def turn_into_csv(string):
    list_of_values = string.split(',')
    final_list = []

    for value in list_of_values:
        value = value.replace('\t', '')
        final_list.append(value)

    print(final_list)


if __name__ == '__main__':
    # CONCATENATE(TRANSPOSE(A1: A2) & ",")
    turn_into_csv('11-157720,	11-157789')