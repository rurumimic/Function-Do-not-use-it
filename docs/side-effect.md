# 부수 효과 Side Effect

## Calculation: 순수 함수

```ruby
def add(total, x) # 명시적인 입력
  return total + x # 명시적인 출력
end
```

`add` 함수의 주요 기능:
- 입력값 `total`, `x`의 합을 반환한다.

## Action: 부수 효과가 있는 순수하지 않은 함수

```ruby
$total = 5 # 전역변수

def add(x)
  puts "#{$total} += #{x}" # 콘솔 화면에 출력한다.
  $total += x # 함수 바깥의 전역 변수의 값을 변경한다.
  return $total
end
```

`add` 함수에서 일어나는 부수 효과:
- `add` 함수 안에서 **전역변수** `$total`을 읽고 쓴다.
- `add` 함수 안에서 `puts` 함수로 **콘솔 화면에 출력**한다.

---

## 하스켈 부수 효과

- 함수의 정의만으로도 어떻게 코드가 짜여졌을지 예측할 수 있다.
- 다음 함수는 데이터베이스 IO 작업이 동작될 것이라는 것이 쉽게 예상된다.

```hs
getPerson :: String -> Database Person
```

- 자바: 직접 코드를 뜯어봐야한다.

```java
public Person getPerson(String name) {..}
```

- 부수 효과는 잠재적으로 복잡한 코드가 숨어있다는 뜻이다.
- 숨어있는 복잡한 코드에서 버그가 발생할 가능성이 많아진다.
- 부수 효과를 **줄인다면** 안정성을 높일 수 있다. → **Calcuation**
- 부수 효과를 **표면적으로 드러내는 방법**으로도 안정성을 높일 수 있다. → 명시적인 함수 정의 / 타입 시스템 활용
