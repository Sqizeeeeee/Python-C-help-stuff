from random import choice
def quick_sort(m:list):
    if len(m) <= 1:
        return m
    else:
        x = choice(m)
        R = []
        L = []
        M = []
        for i in m:
            if i > x:
                R.append(i)
            elif i < x:
                L.append(i)
            else:
                M.append(i)
        return (quick_sort(L) + M + quick_sort(R))



if __name__ == '__main__':
    s = [1,2,3,5,4,3,2,1,22,3,4,55,6,56,76]
    print(quick_sort(s))