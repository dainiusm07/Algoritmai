public class B11 {
	static int n = 5;//matricos dydis
	static int N = 99999999;// nera kelio

	static void FloydWarshall(int W[][]) {
		int[][] dist = new int[n][n];// arciausias kelias nuo - iki
		int i, j, k;
		dist=W;

		for (k = 0; k < n; k++)
			for (j = 0; j < n; j++)
				for (i = 0; i < n; i++)
					// jeigu einant per k taska atstumas mazesnis tai keiciam
					if (dist[i][k] + dist[k][j] < dist[i][j]) {
						dist[i][j] = dist[i][k] + dist[k][j];
					}
		
		printMatrix(dist);
	}

	public static void main(String[] args) {	

		int graph[][] = { 
				{ 0, 3, 8, N, -4 },
				{ N, 0, N, 1, 7 }, 
				{ N, 4, 0, N, N }, 
				{ 2, N, -5, 0, N },
				{ N, N, N, 6, 0 } 
				};
		FloydWarshall(graph);
	}
	static void printMatrix(int dist[][]) {
		System.out.println("New matrix: ");
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (dist[i][j] == N)
					System.out.print("N   \t");
				else
					System.out.print(dist[i][j] + "   \t");
			}
			System.out.println();
		}
	}	
}
