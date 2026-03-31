import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static class Node {
        Map<String, Node> child;

        private Node() {
            child = new HashMap<>();
        }
    }

    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
//        SolutionFivo sol = new SolutionFivo();

//        3
//        2 B A
//        4 A B C D
//        2 A C
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine(), " ");

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int answer = 0;

        Node root = new Node();

        for(int i =0; i< n;i ++) {
            String nString = br.readLine();

            if(! root.child.containsKey(nString)) {
                root.child.put(nString, new Node());
            }
        }


        for(int i=0; i<m; i++) {
            String mString = br.readLine();

            if(root.child.containsKey(mString)) {
                answer += 1;
            }
        }
        System.out.print(answer);


    }
}