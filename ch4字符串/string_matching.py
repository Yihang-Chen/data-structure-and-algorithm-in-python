# 字符串匹配算法


def naive_matching(t, p):
    # t 为目标串，p 为模式串
    m, n = len(p), len(t)
    i, j = 0, 0
    while i < m and j < n:
        if p[i] == t[j]:
            i, j = i + 1, j + 1
        else:
            i, j = 0, j - i + 1
    if i == m:
        return j - i
    return -1


#------------------------------------------
if __name__ == "__main__":

    print("Start testing.")

    # *************************
    # test naive_matching()
    # *************************
    print(naive_matching('', 'a'))
    print(naive_matching('aaa', 'a'))
    print(naive_matching('aaa', 'aaaa'))
    print(naive_matching('aaabbb', 'aaaa'))
    print(naive_matching('acgccatgcc', 'ccatg'))
    print(naive_matching('awefnon4f879*^^&&NFWhim', '9*'))


