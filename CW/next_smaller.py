def next_smaller(n):
    digits = list(str(n))
    length = len(digits)

    pivot_idx = -1
    for i in range(length - 2, -1, -1):
        if digits[i] > digits[i+1]:
            pivot_idx = i
            break

    if pivot_idx == -1:
        return -1

    pivot = digits[pivot_idx]

    swap_idx = -1
    for i in range(length - 1, pivot_idx, -1):
        if digits[i] < pivot:
            swap_idx = i
            break

    digits[pivot_idx], digits[swap_idx] = digits[swap_idx], digits[pivot_idx]

    digits[pivot_idx+1:] = sorted(digits[pivot_idx+1:], reverse=True)

    if digits[0] == '0':
        return -1

    return int(''.join(digits))


print(next_smaller(907))  # 790
print(next_smaller(531))  # 513
print(next_smaller(135))  # -1 (no smaller number)
print(next_smaller(2071))  # 2017
print(next_smaller(414))  # 144
print(next_smaller(123456798))  # 123456789
