//  배부른 마라토너

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap <String, Integer> runners = new HashMap<>();
        int n = sc.nextInt();

        for (int i = 0; i < n*2-1; i++) {
            String name = sc.next().trim();
            runners.put(name, runners.getOrDefault(name, -1) + 1);
            if (runners.get(name) == 2) {
                runners.put(name, 0);
            }
        }
        for (String name : runners.keySet()) {
            if (runners.get(name) == 0) {
                System.out.println(name);
                break;
            }
        }
    }
}