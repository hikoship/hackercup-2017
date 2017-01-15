INT_MAX = 2 ** 31 - 1

def pie(price):
    res = [] # res[i][j]: have bought j pies by day i
    for i, p in enumerate(price):
        res.append([0]) # res[i][0] = 0
        if i == 0:
            for j in range(1, len(price) + 1):
                if j <= len(p):
                    res[0].append(sum(p[:j]) + j * j)
                else:
                    res[0].append(INT_MAX) # not so many pies
        else:
            for j in range(1, len(price) + 1):
                tmp = INT_MAX
                for k in range(j + 1):
                    # but k pies on day i
                    if k <= len(p):
                        tmp = min(tmp, res[i - 1][j - k] + sum(p[:k]) + k * k)
                res[i].append(tmp)
    return res[-1][-1]

def main():
    fin = open('pie_progress.txt')
    fout = open('pie_progress_output.txt', 'w')
    T = int(fin.readline())
    for i in range(T):
        N = int(fin.readline().split()[0])
        price = []
        for j in range(N):
            price.append(sorted([int(p) for p in fin.readline().split()]))
        fout.write("Case #%d: %d\n" % (i + 1, pie(price)))
    fin.close()
    fout.close()

if __name__ == '__main__':
    main()
