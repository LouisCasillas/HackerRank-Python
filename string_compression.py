def compress_string(original_string):
    original_length = len(original_string)

    compressed_string = ""

    char_count = 0
    previous_char = original_string[0]
    for c in original_string:
        if c == previous_char:
            char_count += 1
        else:
            compressed_string += previous_char + str(char_count)

            previous_char = c
            char_count = 1

    compressed_string += previous_char + str(char_count)

    if original_length <= len(compressed_string):
        print(original_string)
    else:
        print(compressed_string)


compress_string('aabcccccaaa')
compress_string('abca')
