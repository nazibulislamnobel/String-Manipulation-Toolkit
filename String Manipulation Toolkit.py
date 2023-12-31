def countDigits(s):
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count

def replaceLetters(s):
    result = ''
    for i in range(len(s)):
        if i % 2 == 0 and i + 1 < len(s):
            result += s[i + 1]
        elif i % 2 == 1:
            result += s[i - 1]
        else:
            result += s[i]
    return result

def main():
  for _ in range(2):
    user_input = input("\nEnter a string: ")
    digit_count = countDigits(user_input)
    print(f"The number of digits in '{user_input}' is {digit_count}")

    user_input_again = input("\nEnter a string: ")
    replaced_string = replaceLetters(user_input_again)
    print(f"The replaced string is {replaced_string}")

if __name__ == "__main__":
    main()

