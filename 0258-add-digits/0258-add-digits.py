class Solution:
    def addDigits(self, num: int) -> int:
        t1=0
        t2=0
        t3=0
        while num!=0:
            digit1=num%10
            t1=digit1+t1
            num//=10
        while t1!=0:
            digit2=t1%10
            t2=digit2+t2
            t1//=10
        while t2!=0:
            digit3=t2%10
            t3=digit3+t3
            t2//=10
        return t3
        