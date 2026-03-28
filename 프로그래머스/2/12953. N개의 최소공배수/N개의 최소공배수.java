class Solution {
    public int solution(int[] arr) {
        int answer = 1;
        int a_index = 0;
        int b_index = 1;
        
        int a = arr[a_index];
        
        while(b_index < arr.length) {
            int b = arr[b_index];
            int startA = a;
            int startB = b;
            while(true) {
                // a, b
                // (b, a%b)
                
                // (a > b)
                if(a <= b) {
                    int temp = b;
                    b = a;
                    a = temp;
                }
                // System.out.println(a+":"+b);
                if(b == 0) {
                    break;
                }
                int temp = b;
                
                b = a % temp;
                a = temp;
                
            }
            // System.out.println("-----");
            // System.out.println("최대공약수 = "+a);
            // System.out.println("-----");
            // 최대공약수
            a = startA * startB/ a;
            b_index += 1;
        }
        
        
        
        return a;
    }
}