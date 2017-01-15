import java.util.*;
import java.io.*;


public class PieProgress {
	public static void main(String[] args) throws IOException {
		Scanner scanner = new Scanner(new FileInputStream("pie_progress.txt"));
		
		try {
			int tests = scanner.nextInt();
			
			for (int test=1; test<=tests; test++) {
				int n =  scanner.nextInt();
				int m = scanner.nextInt();
				long[][] costs = new long[n][m+1];
				
				for (int i=0; i<n; i++) {
					for (int j=1; j<=m; j++) {
						costs[i][j] = scanner.nextInt();
					}
					Arrays.sort(costs[i], 1, costs[i].length);
					for (int j=1; j<=m; j++) {
						costs[i][j] += costs[i][j-1];
					}
					for (int j=1; j<=m; j++) {
						costs[i][j] += j*j;
					}
				}
				long[][] dp = new long[n+1][];
				
				for (int i=0; i<=n; i++) {
					dp[i] = new long[1+Math.min(i*m, n)];
				}
				for (int i=1; i<=n; i++) {
					for (int j=i; j<dp[i].length; j++) {
						dp[i][j] = Long.MAX_VALUE;
						for (int k=Math.max(0, j-dp[i-1].length+1); k<=j-i+1 && k<=m && k<=j; k++) {
							dp[i][j] = Math.min(dp[i][j], dp[i-1][j-k]+costs[i-1][k]);
						}
					}
				}
				System.out.println("Case #"+test+": "+dp[n][n]);
			}
		} finally {
			scanner.close();
		}
	}
}
