class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 알파벳인 경우만, 소문자로 바꿔서 문장으로 변환
        sentence = ''
        for i in s:
            if i.isalnum():
                sentence += i.lower()
        # 뒤집어도 똑같은 문장인지 확인
        return sentence[::-1] == sentence