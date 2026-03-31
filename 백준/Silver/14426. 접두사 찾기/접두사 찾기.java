import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static class Node {
        HashMap<String, Node> child;
        private Node() {
            child = new HashMap<>();
        }
    }
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
//        SolutionFivo sol = new SolutionFivo();
//5 10
//baekjoononlinejudge
//startlink
//codeplus
//sundaycoding
//codingsh
//baekjoon
//star
//start
        int answer = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine(), " ");

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Node root = new Node();

        for(int i=0; i<n; i++) {
            String nStr = br.readLine();
            Node cur = root;
            for(char c : nStr.toCharArray()) {
                if (!cur.child.containsKey(String.valueOf(c))) {
                    cur.child.put(String.valueOf(c), new Node());
                }
                cur = cur.child.get(String.valueOf(c));
            }
        }
        for (int i=0; i<m; i++) {
            String mStr = br.readLine();
            boolean isCheck = true; // 접두사 아닐 때
            Node checkCur = root;


            for(char c: mStr.toCharArray()) {
                // 글자별로 접두사에 포함되는지 확인
                if (checkCur.child.containsKey(String.valueOf(c))) {

                    checkCur = checkCur.child.get(String.valueOf(c));
                }else {
//                    System.out.println(checkCur.child.keySet()+" : "+c);
                    isCheck = false;
                    break;
                }
            }
//            System.out.println(mStr+" : "+isCheck);
            if (isCheck) {
                answer ++;
            }

        }
        System.out.println(answer);

    }
}
