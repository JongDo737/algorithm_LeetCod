class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];

        // 가로 *2 + 세로 *2 + 4 = brown
        // 가로* 세로 = yellow가 되야함
        // answer = [가로+2, 세로+2]

        int width = 0;
        int height = 0;

        while(true) {
            if (width*2 + height*2 + 4 == brown) {
                System.out.println("1: "+width+" : "+height);
                answer[0] = height+2;
                answer[1] = width+2;
                break;
            }
            do {
                width += 1;
                height = yellow / width;
                System.out.println("2: "+width+" : "+height);

            } while (width * height != yellow);
        }
        
        return answer;
    }
}