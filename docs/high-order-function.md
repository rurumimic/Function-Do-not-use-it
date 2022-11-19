# 고차 함수 Higher-order Function

- 함수를 입력받는 함수
- 함수를 출력하는 함수

|        | 함수                     |
| ------ | ------------------------ |
| 함수   | ![](../images/xr.svg)    |
| 도함수 | ![](../images/rxr-1.svg) |

---

### 일급 함수 first-class function

- 일급 함수는 프로그래밍 언어에서 변수와 동일하게 다루어진다.
  1. 함수의 입력값, 출력값에도 함수가 정의될 수 있을 때
  2. 데이터 구조에 함수를 저장할 수 있을 때
- 제네릭 프로그래밍 generic programming
  - 데이터 형식에 제약받지 않고 재사용성을 높이는 설계

#### Haskell

- [applyTwice.hs](../src/hof/applyTwice.hs)

```hs
applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

applyTwice (+3) 10 -- 16
applyTwice (++ " HAHA") "HEY" -- "HEY HAHA HAHA"
applyTwice (3:) [1] -- [3,3,1]
```

#### Python

```python
def apply_twice(f, x):
    return f(f(x))

apply_twice(lambda x: x + 3, 10) # 16
apply_twice(lambda x: x + " HAHA", "HEY") # 'HEY HAHA HAHA'
apply_twice(lambda x: [3] + x, [1]) # [3, 3, 1]
```

---

### 고차 함수의 합성

자주 사용하는 함수들을 결합하여 복잡한 계산 과정을 처리할 수 있다.

- map
- filter
- take / islice
- reduce
- 익명 함수 Anonymous function: lambda

#### clojure

- [example.clj](../src/hof/example.clj)

```clojure
(->> (range)
     (map inc)
     (filter even?)
     (take 5)
     (reduce +)) 
;; => 30
```

#### python

- [example.py](../src/hof/example.py)

```py
reduce(add, islice(filter(lambda x: x % 2 == 0, map(lambda x: x + 1, count())), 5))
# 30
```

---

### Currying

예제: [send_mail.py](../src/hof/send_mail.py)

- 입력: `func` 함수
- 출력: `inner(name)` 함수

```py
def make_mail(func):
    def inner(name):
        return func(name)
    return inner
```

실제 실행될 함수들:

```py
def hello(name):
    return "Hello, " + name

def goodbye(name):
    return "Goodbye, " + name
```

실행 결과:

```py
email_to = make_mail(hello)
email_to("Alice") # Hello, Alice
email_to("Charlie") # Hello, Charlie

make_mail(goodbye)("Alice") # Goodbye, Alice
make_mail(goodbye)("Charlie") # Goodbye, Charlie
```

---

## 요약

- OOP의 복잡한 디자인 패턴은 **일급**으로 다루어지는 **고차 함수들의 합성**으로 구현 가능하다.
- 익명 함수, 커링 등 다양한 개념이 적용되어 **재사용성**, **모듈화**, **사용 편이성** 수준이 높아진다.
