from tqdm import trange

def my_solution(n):
    OPT = [0] * (n + 1)

    for i in range(2, n + 1):
        max_value = 0
        for k in range(1, i):
            max_value = max(max_value, max(OPT[i - k], i - k) * max(OPT[k], k))
        OPT[i] = max_value

    return OPT[n]


def other_solution(n):
    OPT = [0] * (n + 1)

    for i in range(2, n + 1):
        max_value = 0
        for k in range(1, i):
            max_value = max(max_value, k * max(i - k, OPT[i - k]))
        OPT[i] = max_value

    return OPT[n]


def compare_functions(max_n):
    for n in trange(2, max_n + 1):
        result1 = my_solution(n)
        result2 = other_solution(n)
        if result1 != result2:
            print(f"Difference found at n = {n}: my algorithm = {result1}, other algorithm = {result2}")
            return False
    print("Both functions give the same results for all values of n.")
    return True


compare_functions(1000)