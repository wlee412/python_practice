# 🐍 Python Practice — Dictionary & 조건문 학습

이번 실습은 **학생 점수를 기준으로 성적 등급을 부여하는 프로그램**을 작성하면서  
Python에서의 **조건문 범위 표현**과 **Dictionary(자바의 Map과 유사)** 개념을 복습했습니다.  

---

## 📘 배운 점
- Python에서는 **범위 조건**을 `and` 대신 **체인 연산**으로 표현할 수 있음  
  ```python
  if 81 <= score <= 90:
      ...

---

## 📚 추가 학습 메모

조건문 작성: Python은 들여쓰기 기반, 중괄호 {}가 필요 없음

자료구조 비교:

Python list ↔ Java ArrayList

Python dict ↔ Java HashMap

Python set ↔ Java HashSet

코드 스타일: Python은 자바보다 간결하게 범위 조건과 자료구조를 표현할 수 있음

오류 경험: 처음에 {key, "value"}로 작성해서 set으로 인식 →
'set' object is not subscriptable 오류 발생 → :을 써야 dict라는 점을 학습

---

## ✅ 느낀 점

자바에 익숙하다 보니 Python의 문법이 처음엔 낯설었지만,
조건문 범위 표현이 훨씬 간단하고 직관적이라는 장점이 있음.
또한 dict는 자바의 Map과 동일한 개념이라 금방 익숙해질 수 있다고 느낌.