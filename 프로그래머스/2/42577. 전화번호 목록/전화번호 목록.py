def solution(phone_book):
    phone_book.sort()
    # index 번의 전화번호가 다른 전화번호의 접두사 인지 확인. 슬라이싱을 활용해보자
    for i in range(0, len(phone_book) -1): # index
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True