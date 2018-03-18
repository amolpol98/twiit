def can_break(input_string, list_of_strings):
    """Returns None if the input string cannot be created from the given list of strings else returns possible words."""

    given_string_length = len(input_string)

    DP = [[-1 for _ in range(given_string_length)] for _ in range(given_string_length)]

    for substring_length in range(1, given_string_length + 1):
        for start in range(0, given_string_length - substring_length + 1):
            end = start + substring_length - 1
            substring = input_string[start: end + 1]
            if substring in list_of_strings:
                DP[start][end] = start
                continue

            for split in range(start + 1, end + 1):
                if DP[start][split - 1] != -1 and DP[split][end] != -1:
                    DP[start][end] = split
                    break

    if DP[0][-1] == -1:
        return None

    words = []
    start_index = 0
    end_index = given_string_length - 1
    while start_index < given_string_length:
        split_index = DP[start_index][end_index]
        if start_index == split_index:
            words.append(input_string[start_index: end_index + 1])
            break
        else:
            words.append(input_string[start_index: split_index])
        start_index = split_index

    return " ".join(words)


def unit_testcases(input_string, list_of_strings):
    assert True == bool(can_break(input_string, list_of_strings))

if __name__ == '__main__':

    list_of_strings = ['back', 'end', 'front', 'tree']
    print('List of strings - %s\n' % list_of_strings)

    for input_string in ['backend', 'frontyard', 'frontend']:
        print('Input string - %s' % input_string)
        print('Creating the string from the list is%spossible\n' % (' ' if can_break(input_string, list_of_strings) else ' not '))

    # unit_testcases("treeend", list_of_strings)
