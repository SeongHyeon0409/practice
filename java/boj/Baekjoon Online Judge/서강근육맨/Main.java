//  서강근육맨

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] health = new long[n];
        for (int i = 0; i < n; i++) {
            health[i] = sc.nextLong();
        }

        Arrays.sort(health);
        long answer = 0;
        int start = 0;
        int end = n % 2 == 0 ? n - 1 : n - 2;
        while (start < end)
        {
            answer = Math.max(answer, health[start++] + health[end--]);
        }
        if (n%2==1)
        {
            answer = Math.max(answer, health[n - 1]);
        }
        System.out.println(answer);
    }
}