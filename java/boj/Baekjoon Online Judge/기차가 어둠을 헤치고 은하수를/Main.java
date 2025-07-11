//  기차가 어둠을 헤치고 은하수를

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static Set<String> set = new HashSet<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] trains = new int[n];
        for (int i = 0; i < m; i++) {
            int command = sc.nextInt();

            if (command == 1) {
                int trainIdx = sc.nextInt() - 1;
                int seatIdx = sc.nextInt() - 1;
                trains[trainIdx] |= (1 << seatIdx);
            }
            else if (command == 2) {
                int trainIdx = sc.nextInt() - 1;
                int seatIdx = sc.nextInt() - 1;
                trains[trainIdx] &= ~(1 << seatIdx);
            }
            else if (command == 3) {
                int trainIdx = sc.nextInt() - 1;
                trains[trainIdx] <<= 1;
                trains[trainIdx] &= ~(1 << 20); // 21번째 비트 제거
            }
            else if (command == 4) {
                int trainIdx = sc.nextInt() - 1;
                trains[trainIdx] >>= 1;
            }
        }

        Set<Integer> uniqueTrains = new HashSet<>();
        for (int train : trains) {
            uniqueTrains.add(train);
        }

        System.out.println(uniqueTrains.size());
    }
    public static void pushTrain(int[] train) {
        for (int i = train.length-1; i > 0; i--) {
            train[i] = train[i-1];
        }
        train[0] = 0;
    }

    public static void pullTrain(int[] train) {
        for (int i = 0; i < train.length-1; i++) {
            train[i] = train[i+1];
        }
        train[train.length-1] = 0;
    }
}