import java.util.*;
import java.io.*;


public class ManicMoving {
	public static void main(String[] args) throws IOException {
		Scanner scanner = new Scanner(new FileInputStream("manic_moving.txt"));
		
		try {
			int tests = scanner.nextInt();
			
			for (int test=1; test<=tests; test++) {
				int n =  scanner.nextInt();
				int m = scanner.nextInt();
				int K = scanner.nextInt();
				int[][] dists = new int[n][n];
				int[][] moves = new int[K][2];
				
				for (int i=0; i<n; i++) {
					Arrays.fill(dists[i], Integer.MAX_VALUE);
					dists[i][i] = 0;
				}
				for (int i=0; i<m; i++) {
					int j = scanner.nextInt()-1;
					int k = scanner.nextInt()-1;
					
					dists[j][k] = dists[k][j] = Math.min(dists[k][j], scanner.nextInt());
				}
				for (int k=0; k<n; k++) {
					for (int i=0; i<n; i++) {
						for (int j=i+1; j<n; j++) {
							dists[i][j] = dists[j][i] = (int)Math.min(dists[i][j], 0L+dists[i][k]+dists[k][j]);
						}
					}
				}
				boolean flag = true;
				
				for (int i=0; i<K; i++) {
					moves[i][0] = scanner.nextInt()-1;
					moves[i][1] = scanner.nextInt()-1;
					if (dists[moves[i][0]][moves[i][1]] == Integer.MAX_VALUE ||
							(i > 0 && dists[moves[i-1][1]][moves[i][0]] == Integer.MAX_VALUE) ||
							(i == 0 && dists[0][moves[0][0]] == Integer.MAX_VALUE)) {
						flag = false;
					}
				}
				if (!flag) {
					System.out.println("Case #"+test+": -1");
				} else if (0 == K) {
					System.out.println("Case #"+test+": 0");
				} else if (1 == K) {
					System.out.println("Case #"+test+": "+(dists[0][moves[0][0]]+dists[moves[0][0]][moves[0][1]]));
				} else {
					long[][] dp = new long[K][2];
					
					dp[0][0] = 0L+dists[0][moves[0][0]]+dists[moves[0][0]][moves[0][1]];
					dp[0][1] = 0L+dists[0][moves[0][0]]+dists[moves[0][0]][moves[1][0]]+dists[moves[1][0]][moves[0][1]];
					for (int i=1; i<K; i++) {
						dp[i][0] = Math.min(dp[i-1][0]+dists[moves[i-1][1]][moves[i][0]]+dists[moves[i][0]][moves[i][1]], 
								dp[i-1][1]+dists[moves[i-1][1]][moves[i][1]]);
						if (i < K-1) {
							dp[i][1] = Math.min(dp[i-1][0]+dists[moves[i-1][1]][moves[i][0]]+
									dists[moves[i][0]][moves[i+1][0]]+dists[moves[i+1][0]][moves[i][1]],
									dp[i-1][1]+dists[moves[i-1][1]][moves[i+1][0]]+dists[moves[i+1][0]][moves[i][1]]);
						}
					}
					System.out.println("Case #"+test+": "+dp[K-1][0]);
				}
			}
		} finally {
			scanner.close();
		}
	}
}
