//  나무 자르기

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] raises = new int[n];
        Long answer = 0L;
        for (int i = 0; i < n; i++) {
            answer += sc.nextLong();
        }
        for (int i = 0; i < n; i++) {
            raises[i] = sc.nextInt();
        }
        Arrays.sort(raises);
        for (int i = 0; i < n; i++) {
            answer += raises[i] * i;
        }

        System.out.println(answer);

    }
}