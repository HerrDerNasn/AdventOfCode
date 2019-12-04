interval = [245318, 765747]


def smaller(bottom, top):
    for x in range(0, len(bottom)):
        if bottom[x] < top[x]:
            return True
        if bottom[x] > top[x]:
            return False
    return True


def get_digits(number):
    str_number = str(number)
    digits = []
    for ch in str_number:
        digits.append(int(ch))
    return digits


def is_valid(digits):
    one_double = False
    curr_double = (-1, -1)
    for x in range(len(digits) - 1, 0, -1):
        if digits[x] < digits[x - 1]:
            return False
        if digits[x] == digits[x - 1]:
            if one_double:
                if curr_double[0] == x and curr_double[1] == digits[x - 1]:
                    one_double = False
            else:
                if curr_double == (-1, -1) or (not x == curr_double[0] and not digits[x] == curr_double[1]):
                    one_double = True
                    curr_double = (x - 1, digits[x - 1])
                else:
                    curr_double = (x - 1, digits[x - 1])
    return one_double


def increment_digits(digits):
    curr_ind = len(digits) - 1
    while curr_ind > -1:
        if digits[curr_ind] < 9:
            digits[curr_ind] += 1
            curr_ind = -1
        else:
            next_ind = curr_ind - 1
            while next_ind > -1:
                if not digits[next_ind] == 9:
                    digits[curr_ind] = digits[next_ind] + 1
                    next_ind = -1
                else:
                    next_ind -= 1
            curr_ind -= 1
    return digits


def count_valid_passwords():
    bottom_digits = get_digits(interval[0])
    target_digits = get_digits(interval[1])
    count = 0
    valid = []
    while smaller(bottom_digits, target_digits):
        if is_valid(bottom_digits):
            count += 1
            valid.append(bottom_digits.copy())
        bottom_digits = increment_digits(bottom_digits)
    print(valid)
    return count


def main():
    print(count_valid_passwords())


if __name__ == "__main__":
    main()
