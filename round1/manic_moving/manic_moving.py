import networkx as nx
INT_MAX = 2 ** 31 - 1

def moving(G, F):
    d = nx.floyd_warshall(G, weight='weight')
    # res[i - 1][0]: the result to unload ith item w/o carrying the (i + 1)th item
    # res[i - 1][1]: the result to unload ith item w carrying the (i + 1)th item
    res = [[]]
    try:
        res[0].append(d['1'][F[0][0]] + d[F[0][0]][F[0][1]])
        if len(F) == 1:
            return res[0][0]
        res[0].append(d['1'][F[0][0]] + d[F[0][0]][F[1][0]] + d[F[1][0]][F[0][1]])

        for i in range(1, len(F)):
            res.append([])
            res[i].append(min(res[i - 1][0] + d[F[i - 1][1]][F[i][0]] + d[F[i][0]][F[i][1]], res[i - 1][1] + d[F[i - 1][1]][F[i][1]]))
            if i == len(F) - 1:
                return res[i][0]
            res[i].append(min(res[i - 1][0] + d[F[i - 1][1]][F[i][0]] + d[F[i][0]][F[i + 1][0]] + d[F[i + 1][0]][F[i][1]], res[i - 1][1] + d[F[i - 1][1]][F[i + 1][0]] + d[F[i + 1][0]][F[i][1]]))
    except:
        return -1

def main():
    fin = open('manic_moving.txt')
    fout = open('manic_moving_output.txt', 'w')
    T = int(fin.readline())
    for i in range(T):
        data = fin.readline().split()
        # N = int(data[0]) # number of vertices
        M = int(data[1]) # number of edges
        K = int(data[2]) # number of families
        G = nx.Graph()
        for j in range(M):
            edge = fin.readline().split()
            G.add_edge(edge[0], edge[1], weight = int(edge[2]))

        F = []
        for j in range(K):
            F.append(fin.readline().split())

        x = moving(G, F)
        if x == float('Inf'):
            x = -1
        fout.write("Case #%d: %d\n" % (i + 1, x))
    fin.close()
    fout.close()

if __name__ == '__main__':
    main()
