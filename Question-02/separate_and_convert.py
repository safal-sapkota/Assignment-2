def separate_and_convert(s):
    num_str = ''.join(c for c in s if c.isdigit())
    letter_str = ''.join(c for c in s if c.isalpha())

    # Even numbers to ASCII decimal values
    even_numbers = [int(c) for c in num_str if int(c) % 2 == 0]
    ascii_values = [ord(str(num)) for num in even_numbers]

    # Uppercase letters to ASCII decimal values
    upper_case_letters = [c for c in letter_str if c.isupper()]
    upper_case_ascii = [ord(c) for c in upper_case_letters]

    print(f"Number substring: {num_str}")
    print(f"Letter substring: {letter_str}")
    print(f"Even numbers: {even_numbers}")
    print(f"Even numbers ASCII Codes: {ascii_values}")
    print(f"Uppercase letters: {upper_case_letters}")
    print(f"Uppercase letters ASCII Codes: {upper_case_ascii}")

# Example usage
s = '56aAww1984sktr235270aYmn145ss785fsq31D0'
separate_and_convert(s)