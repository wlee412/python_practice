# Caesar Cipher 🔐

이 프로젝트는 **시저 암호(Caesar Cipher)** 방식을 Python으로 구현한 간단한 암호화/복호화 프로그램입니다.  
사용자가 메시지와 시프트(shift) 값을 입력하면, 알파벳 문자를 해당 값만큼 이동시켜 암호화하거나 복호화합니다.  

---

## 📜 기능
- **암호화 / 복호화**  
  - `encode` → 오른쪽으로 시프트  
  - `decode` → 왼쪽으로 시프트 (shift 값에 `-1`을 곱해 반대 방향 이동)
- **예외 처리**: 알파벳이 아닌 문자(숫자, 기호, 공백 등)는 변경하지 않고 그대로 유지
- **무한 반복 실행**: 사용자가 `yes`를 입력하면 계속 실행, `no`를 입력하면 종료
- **art.py**의 로고 출력

---

## 🖥 코드 예시
```python
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
restart = "yes"

while restart == "yes":
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no': ").strip().lower()
    if restart == "no":
        print("Goodbye")
        break 
```

---

## 📚 배운 점
- **`index()` 함수 활용**  
  리스트에서 특정 값의 위치를 찾는 방법을 익힘.
- **방향 전환 구현**  
  `shift` 값에 `-1`을 곱해 암호화 ↔ 복호화 방향을 전환하는 방법 학습.
- **Python `for`문 활용 능력 향상**  
  문자열을 한 글자씩 순회하며 처리하는 로직에 익숙해짐.
- **`modulo (%)` 연산 활용**  
  - 알파벳 범위를 초과했을 때 인덱스를 순환시키는 방법 이해.  
  - 알파벳에 없는 문자(숫자, 기호, 공백 등)를 수정하지 않고 그대로 유지하는 예외 처리 방법 학습.

---

## 🚀 실행 예시

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world!
Type the shift number:
5
Here is the encoded result: mjqqt btwqi!
```