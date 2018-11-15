from django.db import models

# Create your models here.

class Address(models.Model):
    #데이터 베이스의 테이블 생성(클래스 상속)
    address = models.CharField(max_length=20)



    def __str__(self):
        return self.address




                 #문자열 : 케릭터필드. 썼기 떄문에 테이블에 보면 바 필드 생성.
                 #글자수 20까지.

#모델을 쓰면 자동으로 id생성.
#함수 재정의 : 오버라이딩


