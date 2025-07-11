import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] board = new int[19][19];
    // →, ↓, ↘, ↙
    static int[] dx = {1, 0, 1, -1};
    static int[] dy = {0, 1, 1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        // 입력
        for (int i = 0; i < 19; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < 19; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 탐색
        for (int y = 0; y < 19; y++) {
            for (int x = 0; x < 19; x++) {
                int color = board[y][x];
                if (color == 0) continue;

                for (int dir = 0; dir < 4; dir++) {
                    // 이전 칸에 같은 돌이 있으면 스킵 (중복·6목 방지)
                    int py = y - dy[dir], px = x - dx[dir];
                    if (inBounds(py, px) && board[py][px] == color)
                        continue;

                    // 정확히 5개 연속인지
                    boolean ok = true;
                    int ny = y, nx = x;
                    for (int k = 1; k < 5; k++) {
                        ny += dy[dir];
                        nx += dx[dir];
                        if (!inBounds(ny, nx) || board[ny][nx] != color) {
                            ok = false;
                            break;
                        }
                    }
                    if (!ok) continue;

                    // 다음 칸 검사 (6목 방지)
                    int iy = y + dy[dir] * 5;
                    int ix = x + dx[dir] * 5;
                    if (inBounds(iy, ix) && board[iy][ix] == color)
                        continue;

                    // **출력 좌표 분기**
                    int outY = y, outX = x;
                    if (dir == 3) {
                        // ↙ 방향일 땐 가장 왼쪽 돌이 다섯 번째이므로
                        outY = y + dy[dir] * 4;  // y + 4
                        outX = x + dx[dir] * 4;  // x - 4
                    }

                    System.out.println(color);
                    System.out.println((outY + 1) + " " + (outX + 1));
                    return;
                }
            }
        }

        System.out.println(0);
    }

    private static boolean inBounds(int y, int x) {
        return y >= 0 && y < 19 && x >= 0 && x < 19;
    }
}
