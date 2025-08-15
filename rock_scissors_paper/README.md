# Rock-Paper-Scissors Game

## Overview
간단한 **가위바위보 게임** 구현.  
- 사용자가 0(바위), 1(보), 2(가위)를 입력
- 컴퓨터는 0~2 중 무작위 선택
- ASCII 아트를 사용해 각 선택을 시각적으로 표시
- 승패를 판정하여 결과 출력

---

## Features

 ASCII 아트로 바위, 보, 가위 표시

 random.randint()로 컴퓨터 선택 구현

 잘못된 입력(0, 1, 2 외) 처리

 승패 판정 로직

 사용자가 계속 플레이할 수 있는 반복 기능

 점수 집계 기능

 입력값을 숫자 대신 문자열("rock", "paper", "scissors")로도 지원

---

## Example

```text

What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors. 0
conputer_choice:     
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

user choose: 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

result is:
You lose!

```

---

## What I Learned

random.randint(a, b)로 정수 범위 내 무작위 값 생성

리스트 인덱스를 이용해 선택한 ASCII 아트 출력

집합 {}을 사용해 입력값 검증 (if user_choice in {"0","1","2"})

조건문으로 게임 승패 판정 로직 구현

---

## Next Steps

게임 반복 기능(while 루프) 추가

승리/패배 횟수 누적

대소문자 구분 없는 문자열 입력 처리

결과를 좀 더 직관적으로 표시 (예: "Rock beats Scissors → You Win!")