//  달력

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {

    public static void main(String[] args) {
        class Work implements Comparable<Work>{
            int start;
            int end;
            int time;

            public Work(int start, int end) {
                this.start = start;
                this.end = end;
                this.time = end - start + 1;
            }

            @Override
            public int compareTo(Work other) {
                if (this.start != other.start) {
                    return Integer.compare(this.start, other.start);
                }
                else {
                    return Integer.compare(other.time, this.time);
                }
            }
        }

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] counts = new int[366];
        int answer = 0;
        for (int i = 0; i < n; i++) {
            int s = sc.nextInt();
            int e = sc.nextInt();
            for (int j = s; j <= e; j++) {
                counts[j]++;
            }
        }
        int stack = 0;
        int maxv = 0;
        for (int i = 0; i < counts.length; i++) {
            if (counts[i] == 0) {
                answer += stack * maxv;
                stack = 0;
                maxv = 0;
            }
            else {
                stack++;
                maxv = Math.max(maxv, counts[i]);
            }
        }
        answer += stack * maxv;
        System.out.println(answer);
        
    }
}