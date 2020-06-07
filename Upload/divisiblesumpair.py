from itertools import combinations

def divisibleSumPairs(n, k, ar):
    sum_lst = list()
    res = list()
    comb_list = (list(combinations(ar, 2)))
    for i in comb_list:
        sum_lst.append(i[0] + i[1])
        print(sum_lst)
    for i in sum_lst:
        if (i % k) == 0:
            res.append(i)
    return (len(res))
                



if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)
