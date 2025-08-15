# Password Generator

## Overview
사용자로부터 원하는 **영문자, 특수문자, 숫자 개수**를 입력받아 비밀번호를 생성하는 프로그램.  
- **Easy Mode**: 입력 순서대로 문자 배치  
- **Hard Mode**: 문자 순서를 무작위로 섞어 보안성 향상

---

```text
Welcome to the PyPassword Generator!
How many letters would you like in your password?
4
How many symbols would you like?
2
How many numbers would you like?
2
here is your password: JduE&!91
here is your password: g^2jk8&P
```

---

## What I Learned

random.choices(list, k=n): 리스트에서 중복 허용하며 n개 무작위 선택

random.sample(list, n): 리스트에서 중복 없이 n개 무작위 선택

리스트 연결 후 for문으로 문자열로 변환

입력값을 int()로 변환해 숫자형으로 활용

---

## Next Steps

비밀번호 길이를 자동으로 계산 (len(password))

사용자가 총 길이만 입력하면 문자를 랜덤 비율로 섞어 생성

CLI 인자(argument)로 옵션 제공 (argparse 활용)

대소문자 강제 포함 옵션 추가