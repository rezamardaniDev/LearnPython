def longest_str_in_list(list_of_strings):
    final_result = ''
    for string  in list_of_strings:
        if len(string) >= len(final_result):
            final_result = string

    return final_result, len(final_result)


print(longest_str_in_list(['developer', 'programmer', 'founder']))