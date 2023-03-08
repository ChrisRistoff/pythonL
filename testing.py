def gap(g, m, n):
    all_num = [0]
    for num in range(m, n):
        if num % 2 != 0:
            all_num.append(num)
    for i in range(len(all_num) - 1):
        if all_num[i + 1] - all_num[i] == g:
            return [all_num[i], all_num[i + 1]]
    return None


print(gap(4, 130, 200))
