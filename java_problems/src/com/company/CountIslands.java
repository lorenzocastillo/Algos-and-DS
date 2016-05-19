/**
 * @author Raj, Lorenzo
 *
 */
public class CountIslands {

    final int MOVES[][] = {{1, 1}, {-1, 1}, {1, -1}, {-1, -1}, {1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    /**
     * @param args
     */
    public static void main(String[] args) {
        CountIslands obj = new CountIslands();
        int result, result2 = -1;
        int a[][] = { { 1, 1, 0, 0, 0 }, { 0, 1, 0, 0, 1 }, { 1, 0, 0, 1, 1 }, { 0, 0, 0, 0, 0 }, { 1, 0, 1, 0, 1 } };

        // Time :O(rows*cols), Space : O(rows*cols)
        result = obj.countIslands(a, a.length, a[0].length);

        // Time :O(rows*cols), Space : O(1), if original array is mutable
        // not including recursive call space
        result2 = obj.countIslands2(a, a.length, a[0].length);

        assert result == result2;

        System.out.println(obj.countIslands2(a, a.length, a[0].length));
        System.out.println(result);

    }

    public void dfs(int[][] a , int rows, int cols, int row, int col, int count){
        a[row][col] = count;
        for (int i = 0; i < MOVES.length; i++) {
            int r1 = row + MOVES[i][0];
            int c1 = col + MOVES[i][1];
            if (isSafe(a, rows, cols, r1, c1)) {
                dfs(a, rows, cols, r1, c1, count);
            }
        }
    }

    public int countIslands2(int[][] a, int rows, int cols) {
        int count = 1;

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (a[row][col] == 1) {
                    count++;
                    dfs(a, rows, cols, row, col, count);
                }
            }
        }
        return count - 1;
    }


    public int countIslands(int[][] a, int m, int n) {
        boolean visited[][] = new boolean[m][n];
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (a[i][j] == 1 && visited[i][j] == false) {
                    count++;
                    visited[i][j] = true;
                    dfsForNeighbours(a, m, n, visited, i, j);
                }
            }
        }
        return count;
    }

    public void dfsForNeighbours(int[][] a, int m, int n, boolean[][] visited, int x, int y) {
        visited[x][y] = true;
        for (int i = 0; i < MOVES.length; i++) {
            int x1 = x + MOVES[i][0];
            int y1 = y + MOVES[i][1];
            if (isSafe(a, m, n, x1, y1) && visited[x1][y1] == false) {
                dfsForNeighbours(a, m, n, visited, x1, y1);
            }
        }
    }

    public boolean isSafe(int[][] a, int m, int n, int x, int y) {
        return x >= 0 && x < m && y >= 0 && y < n && a[x][y] == 1;
    }

}
