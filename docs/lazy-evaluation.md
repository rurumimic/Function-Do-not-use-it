# 느긋한 계산 Lazy Evaluation

## 함수형 프로그래밍의 구성 요소

### 데이터

- 값, 결과물

```clojure
(range) ;; => (0 1 2 3 4 5 6 7 8 9 10 11 ...)
'("peter" "steve" "tony") ;; => ("peter" "steve" "tony")
```

### 계산

- 순수 함수 pure function
- 같은 입력값을 넣으면 항상 똑같은 결과값이 나온다: [절차형 vs 함수형](imperative-vs-functional.md)
- **언제든지** 마음껏 실행할 수 있다.: **느긋한 계산**
- 테스트하기 쉽다.

```clojure
(map inc)      ;; => (1 2 3 4 5 6 7 8 9 ...)
(filter even?) ;; => (2 4 6 8 10 ...)
(take 5)       ;; => (1 2 3 4 5)
```

### 액션

- [부수 효과 side-effect](side-effect.md)가 있는 *순수하지 않은 함수 impure function*
- **상황에 따라 실행 결과가 달라진다.**
- 다루기 어렵다. (테스트가 어렵다.)

```clojure
(->> '("peter" "steve" "tony")
     (getPerson))
;; => (Spider-Man Captain-America Iron-Man)

(->> '("peter" "steve" "tony")
     (getPerson))
;; => Execution error (SQLException) at java.sql.DriverManager/getConnection
```

---

## 느긋한 프로그램

### 함수형 프로그래밍 언어에서 모듈화

1. 모든 함수가 Lazy Evaluation을 지원한다.
2. 모듈도 **일관적으로** Lazy Evaluation을 지원한다.
3. Lazy Evaluation을 지원하는 프로그램을 만들 수 있다.
4. Lazy Evalutaion을 지원하는 프로그램들을 서로 연결하여, 강력한 시스템을 구성한다.

따라서 **시스템은 CPU와 메모리를 효율적**으로 사용할 수 있다.

### 명령형 프로그래밍 언어에서 모듈화

1. Lazy Evaluation을 사용하겠다고 함수에 명시한다.
2. 하지만, 프로그래머는 직접적인 통제를 할 수 있다는 **명령형 프로그래밍의 장점을 잃어버린다.**
3. 기존 코드를 Lazy Evaluation과 함께 사용하기 어려워진다.
