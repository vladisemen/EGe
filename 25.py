count = 2
count_max = 2
for i in range(586132, 586431):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            count += 1
        max_del = j
    if count > count_max:
        count_max = count
        Max_del_by_min_num = max_del
    elif count == count_max:
        Max_del_by_max_num = max_del
    count = 2
print(count_max, Max_del_by_min_num)
print(count_max, Max_del_by_max_num)
