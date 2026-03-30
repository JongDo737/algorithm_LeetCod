import java.util.*;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        // 셋째 날, 넷째 날, 다섯째 날부터 각각 열흘은 원하는 제품과 수량이 일치하기 때문에 셋 중 하루에 회원가입을 하려 합니다.

        // Map에 원하는 상품과 가격을 먼저 입력하고
        Map<String, Integer> wantMap = new HashMap<>();

        for(int i=0; i<want.length; i++) {
            wantMap.put(want[i], number[i]);
        }

        // discount 10일 적용해서 리스트 모두가 < 0 일 경우 answer += 1

        for (int i = 0; i < 10; i++) {
            if(wantMap.containsKey(discount[i])) {
                wantMap.put(discount[i], wantMap.get(discount[i]) -1);
            }
        }

        int index = 0;
        int index_max = 10;
        while(index < discount.length) {
            boolean isClear = true;
//            System.out.println(wantMap.values());
            for(Integer count : wantMap.values()) {
                if(count > 0) { // 상품이 다 못사는 날일 때
                    isClear = false;
                    break;

                }
            }

            // 모두 구매했을 경우
            if(isClear) {
                answer ++;
            }

            // 첫 날 할인상품 다시 추가

            if(wantMap.containsKey(discount[index])) {
//                System.out.println("1: "+discount[index]);
                wantMap.put(discount[index], wantMap.get(discount[index])+1);
            }



            // 마지막날 할인 상품 제거
            if(index_max < discount.length && wantMap.containsKey(discount[index_max])) {
//                System.out.println("2: "+discount[index_max]);
                wantMap.put(discount[index_max], wantMap.get(discount[index_max])-1);
            }
            index ++;
            if (index_max < discount.length) {
                index_max ++;
            }

        }

        return answer;
    }
}