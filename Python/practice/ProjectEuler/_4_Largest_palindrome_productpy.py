def is_loop(n):
    str_n = str(n)
    for i in range(0, len(str_n)//2):
        if str_n[i] != str_n[len(str_n)-i-1]:
            return False
    return True


max_for_each = {}
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        if is_loop(i*j):
            #print(i*j)
            max_for_each[i*j] = "{0} * {1} = {2}".format(i, j, i*j)
            #max_for_each.append(i*j)
            break

max_key = max(max_for_each.keys(), key=int)
print(max_for_each[max_key])