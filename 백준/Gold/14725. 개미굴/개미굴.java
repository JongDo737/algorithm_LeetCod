import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static class Node {
        Map<String,Node> child;

        private Node() {
            child = new HashMap<>();
        }
    }
    public static void main(String[] args) throws IOException {
//        SolutionFivo sol = new SolutionFivo();

//        3
//        2 B A
//        4 A B C D
//        2 A C
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Node root = new Node();

        for (int i=0; i< n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int num = Integer.parseInt(st.nextToken());

            Node cur = root;
            while(st.hasMoreTokens()) {
                String s = st.nextToken();
                // 키가 없을 경우 추가
                if(!cur.child.containsKey(s)) {
                    cur.child.put(s, new Node());
                }
                cur = cur.child.get(s);
            }
        }

        print(root, "");
    }
    static void print(Node cur, String s) {
        // 정렬 값 부터
        List<String> list = new ArrayList<>(cur.child.keySet());
        Collections.sort(list);

        for(String str: list) {
            System.out.println(s+str);
            // 재귀로 node 끝까지
            print(cur.child.get(str), s+"--");
        }

    }
}