//  히스토그램

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(); // 첫 줄: 막대 개수

        for (int i = 0; i < n; i++) {
            int heights = sc.nextInt(); // 막대 높이 입력
            System.out.println("=".repeat(heights));
        }


    }
}