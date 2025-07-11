//  NBA 농구

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    static class Team {
        int id;
        int score;
        int win_time;

        public Team(int id, int score) {
            this.id = id;
            this.score = score;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Team team1 = new Team(1, 0);
        Team team2 = new Team(2, 0);
        int currentTime = 0;

        for (int i = 0; i < n; i++) {
            String a = sc.next(); // "1"
            String b = sc.next(); // "01:10"

            if (team1.score > team2.score) {
                team1.win_time += parseTime(b) - currentTime;
            }
            else if (team2.score > team1.score) {
                team2.win_time += parseTime(b) - currentTime;
            }

            if (a.equals("1")) {
                team1.score++;
            }
            else {
                team2.score++;
            }
            currentTime = parseTime(b);
        }

        if (team1.score > team2.score) {
            team1.win_time += parseTime("48:00") - currentTime;
        }
        else if (team2.score > team1.score) {
            team2.win_time += parseTime("48:00") - currentTime;
        }

        System.out.println(timeToMinutes(team1.win_time));
        System.out.println(timeToMinutes(team2.win_time));

    }
    public static int parseTime(String time) {
        String[] parts = time.split(":");
        int hours = Integer.parseInt(parts[0]);
        int minutes = Integer.parseInt(parts[1]);
        return hours * 60 + minutes; // Convert to total minutes
    }

    public static String timeToMinutes(int n) {
        int hours = n / 60;
        int minutes = n % 60;
        return String.format("%02d:%02d", hours, minutes); // Format as "HH:MM"


    }
}