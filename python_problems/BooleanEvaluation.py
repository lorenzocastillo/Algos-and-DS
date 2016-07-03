def string_to_bool(s):
    if s == '1':
        return True
    else:
        return False


def count_eval(string, result):
    if not string:
        return 0
    elif len(string) == 1:
        return 1 if string_to_bool(string) == result else 0
    else:
        ways = 0
        # Scan through the numerals, starting at 1 and every other one after that
        for i in range(1,len(string),2):
            left = string[:i]
            right = string[i+1:]

            left_true = count_eval(left, True)
            left_false = count_eval(left, False)
            right_true = count_eval(right, True)
            right_false = count_eval(right, False)
            total = (left_true + left_false) * (right_true + right_false)

            total_true = 0
            if string[i] == '^':
                total_true = (left_true*right_false) + (left_false*right_true)
            elif string[i] == '&':
                total_true = left_true*right_true
            elif string[i] == '|':
                total_true = (left_true*right_true) + (left_true*right_false) + (left_false*right_true)
            else:
                print("ERROR")

            sub_ways = total_true if result else total - total_true
            ways += sub_ways

        return ways

print(count_eval('1^0|0|1', False))
print(count_eval('0&0&0&1^1|0', True))