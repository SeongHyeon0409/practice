//  별 찍기 - 11

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    static char[][] stars;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        stars = new char[N][2 * N - 1];
        for (int i = 0; i < N; i++) {
            Arrays.fill(stars[i], ' ');
        }

        drawStars(0, N-1, N);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < stars.length; i++) {
            for (int j = 0; j < stars[i].length; j++) {
                sb.append(stars[i][j]);
            }
            sb.append("\n");
        }

        System.out.println(sb);

    }

    public static void drawStars(int r, int c, int N) {
        if (N == 3) {
            stars[r][c] = '*';
            stars[r+1][c-1] = stars[r+1][c+1] = '*';
            stars[r+2][c-2] = stars[r+2][c-1] = stars[r+2][c] = stars[r+2][c+1] = stars[r+2][c+2] = '*';
            return;
        }
        else {
            int cut = N / 2;
            drawStars(r, c, cut);
            drawStars(r + cut, c - cut, cut);
            drawStars(r + cut, c + cut, cut);

        }
    }
}