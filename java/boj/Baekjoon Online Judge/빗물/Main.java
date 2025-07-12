//  빗물

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 그냥 양옆이 막혀있으면 채우면 되는거 같은데
        int answer = 0;
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] block = new int[m];
        for (int i = 0; i < m; i++) {
            block[i] = sc.nextInt();
        }
        for (int i = 1; i <= n; i++) {
            boolean flag = false;
            int stack = 0;
            for (int j = 0; j < m; j++) {
                if (block[j] >= i && flag) {
                    answer += stack;
                    stack = 0;
                }
                else if (block[j] >= i) flag = true;
                else if (flag) stack++;
            }
        }
        System.out.println(answer);

    }
}
