def main():
    fin = open('lazy_loading.txt')
    fout = open('lazy_loading_output.txt', 'w')
    t = int(fin.readline())
    for i in range(t):
        n = int(fin.readline())
        res = 0
        items = []
        for _ in range(n):
            items.append(int(fin.readline()))

        items.sort()
        left = 0
        right = len(items) - 1
        while left <= right:
            left += 49 / items[right] # not 50, because 50 / 25 = 2, but we only need 1 from left
            right -= 1
            res += 1
        if left - right > 1:
            res -= 1 # in fact there are not so many items
        fout.write("Case #%d: %d\n" % (i + 1, res))
    fin.close()
    fout.close()

if __name__ == '__main__':
    main()
