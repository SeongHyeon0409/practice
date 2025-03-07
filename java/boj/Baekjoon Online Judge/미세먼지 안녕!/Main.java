//  미세먼지 안녕!
import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    static int R, C, T;
    static int[] cleaner;
    static int[][] map;
    static int[][] copyMap;
    static int[] dy = {0, -1, 0, 1};
    static int[] dx = {1, 0, -1, 0};
    static int[] dy2 = {0, 1, 0, -1};
    static int[] dx2 = {1, 0, -1, 0};

    public static void printmap(int[][] map) {
        Arrays.stream(map)
                .map(row -> Arrays.toString(row))
                .forEach(System.out::println);
    }
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] s = br.readLine().split(" ");
        R = Integer.parseInt(s[0]);
        C = Integer.parseInt(s[1]);
        T = Integer.parseInt(s[2]);

        map = new int[R][C];
        int num = 0;
        for (int i = 0; i < R; i++) {
            String[] s1 = br.readLine().split(" ");
            for (int j = 0; j < C; j++) {
                map[i][j] = Integer.parseInt(s1[j]);
                if (map[i][j] == -1) {
                    cleaner = new int[] {i, j};
                }
            }
        }
        for (int i = 0; i < T; i++) {
            copyMap = getCopyMap();

            expand();
            map = copyMap;

            copyMap = getCopyMap();

            workCleaner(cleaner[0] - 1, cleaner[1], dy, dx, copyMap);
            workCleaner(cleaner[0], cleaner[1], dy2, dx2, copyMap);
            map = copyMap;
        }

        int count = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] != -1) {
                    count += map[i][j];
                }
            }
        }

        System.out.println(count);
    }



    private static void workCleaner(int y, int x, int[] dy, int[] dx, int[][] copyMap) {
        for (int i = 0 ; i < 4; i++) {
            while (true) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if (ny < 0 || nx < 0 || ny >= R || nx >= C) break;
                if (map[ny][nx] == -1) break;
                if (map[y][x] == -1) {
                    copyMap[ny][nx] = 0;
                }
                else {
                    copyMap[ny][nx] = map[y][x];
                }
                y = ny;
                x = nx;
            }
        }
    }

    private static int[][] getCopyMap() {
        int[][] copyMap = Arrays.copyOf(map, map.length);
        for (int i = 0; i < map.length; i++) {
            copyMap[i] = Arrays.copyOf(map[i], map[i].length);
        }
        return copyMap;
    }

    private static void expand() {
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] >= 0) {
                    int count = 0;
                    for (int k = 0; k < 4; k++) {
                        int nx = j + dx[k];
                        int ny = i + dy[k];
                        if (nx < 0 || ny < 0 || ny >= R || nx >= C ) continue;
                        if (map[ny][nx] == -1) continue;
                        copyMap[ny][nx] += map[i][j] / 5;
                        count++;
                    }
                    copyMap[i][j] -= (map[i][j] / 5) * count;
                }
            }
        }
    }
}