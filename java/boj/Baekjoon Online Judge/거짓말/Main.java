import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {

    static int[] par;
    static ArrayList<Integer> trues;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] str = bf.readLine().split(" ");

        int n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);
        // 사람 n명과 파티 m개
        par = new int[n + 1];
        // i번째 노드가 속한 파티의 루트노드

        trues = new ArrayList<>(); // 진실을 아는 사람들
        ArrayList<ArrayList<Integer>> party = new ArrayList<>();
        // 같은 파티에 참여하는 사람들
        int cnt = 0;
        // 과장 해도 되는 파티

        for(int i = 0; i <= m; i++) {
            party.add(new ArrayList<>());
        }

        for (int i = 0; i <= n; i++) {
            par[i] = i;
        } // 최초 루트노드는 자신

        str = bf.readLine().split(" ");

        int known = Integer.parseInt(str[0]);
        // 진실을 아는 사람의 수

        if(known == 0) { // 진실을 아는 사람이 없음
            System.out.println(m); // 모든 파티에서 가능
            System.exit(0);
        } else { // 아니면
            for (int i = 0; i < known; i++) {
                trues.add(Integer.parseInt(str[i + 1]));
            } // 진실을 아는 사람들을 리스트에 저장
        }


        for(int i = 1; i <= m; i++) {
            // 파티별 탐색
            str = bf.readLine().split(" ");

            int people = Integer.parseInt(str[0]);
            // 파티 참가인원
            int first = Integer.parseInt(str[1]);
            // 파티 참여하는 첫번째 사람
            // 참여인원은 1이상므로 무조건 있음
            party.get(i).add(first);
            // 파티에 저장

            for(int j = 1; j < people; j++) {
                int next = Integer.parseInt(str[j + 1]);

                union(first, next);
                // 첫번째 사람을 기준으로 union
                party.get(i).add(next);
            } // 참여인원들 파티에 저장

        }

        for(int i = 1; i <= m; i++) {
            boolean check = true;
            // 과장 가능한 파티인가?

            for(int next : party.get(i)) {
                if(trues.contains(find(par[next]))) {
                    // 파티에 진실을 아는 사람이 있음
                    // 루트노트가 진실을 아는 사람임
                    check = false;
                    // false로 변경
                    break; // 탐색 종료
                }
            }

            if(check) { // false가 되지 않았음
                cnt++; // 추가
            }
        }

        bw.write(cnt + "\n");

        bw.flush();
        bw.close();
    }

    public static int find(int x) {
        if(par[x] == x) return x;
        else return find(par[x]);
    } // 루트노드 찾기

    public static void union(int x, int y) {
        // 합치기
        int px = find(x);
        int py = find(y);
        // 두 사람이 참여한 파티의 루트노드

        if(trues.contains(py)) {
            int temp = px;
            px = py;
            py = temp;
        } // y쪽 루트 노드가 진실을 아는 사람임
        // 둘이 자리 바꾸기

        par[py] = px;
        // 루트노드 등록
    }

}