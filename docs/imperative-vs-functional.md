# 명령형 vs 함수형

| 명령형 프로그래밍 | 함수형 프로그래밍 |
| ----------------- | ----------------- |
| 5 + 2 = 7         | 5 + 2 = 7         |
| 5 + 3 = **10**    | 5 + 3 = **8**     |
| 5 + 4 = **14**    | 5 + 4 = **9**     |

---

## 명령형 프로그래밍

[imperative.c](../src/imperative-vs-functional/imperative.c)

```c
int x = 5; // x = 5

x += 2;    // x + 2 = 7
x += 3;    // x + 3 = 10
x += 4;    // x + 4 = 14
```

- 변수의 상태가 변경된다.

---

## 함수형 프로그래밍

[functional.py](../src/imperative-vs-functional/functional.py)

```py
>>> def add(a, b):
...   return a + b
...
>>> a = 5
>>> add(a, 2)
7
>>> add(a, 3)
8
>>> add(a, 4)
9
```

- 같은 입력값을 넣으면 항상 똑같은 결과값이 나온다.
- **언제든지** 마음껏 **실행할 수 있다.**
- 테스트하기 쉽다.

---

## 디자인 패턴

![](../images/design.patterns.png)
- [Functional Design Patterns](https://youtu.be/srQt1NAHYC0) by Scott Wlaschin

객체지향 프로그래밍에서 자주 쓰던 **디자인 패턴은** 함수형 프로그래밍에서 **사라진다.**

디자인 패턴 → 고차 함수의 합성

---

## 추상화의 발전

- goto, for: [count.c](../src/imperative-vs-functional/count.c)
- map, filter, reduce: [count.py](../src/imperative-vs-functional/count.py)

<table>
<thead>
<tr>
<th>Goto</th>
<th>For</th>
<th>Map, Filter, Reduce</th>
</tr>
</thead>
<tbody>
<tr>
<td>

```c
int array[3] = {1, 2, 3};

int i = 0;

LOOP:
printf("%d", array[i]);
i++;
if (i < 3)
  goto LOOP;
```
</td>
<td>

```c
int array[3] = {1, 2, 3};

for (int i = 0; i < 3; i++)
{
  printf("%d", array[i]);
}
```

</td>
<td>

```py
array = [1, 2, 3]

map(print, array) # 1 2 3
filter(lambda x: x % 2 == 0, array) # [2]
reduce(add, array, 0) # 6
```

</td>
</tr>
</tbody>
</table>

- 코드의 추상화가 저수준에서 고수준으로 갈수록 **미리 결정된 행동만** 가능하다.
- 추상화가 높은 수준일 때, **비즈니스 문제에 더 집중**할 수 있다.
  - 예: 메모리 할당 관리 vs 가비지 컬렉터
- 미리 만들어진 다양한 함수들 중에서 **상황에 알맞은** 함수를 선택하면, 간단하게 개발할 수 있다.

하지만, **상황을 정확하게 판단**하고 알맞은 **도구를 활용하는 능력**을 갖춰야한다.  

---

## (참고) Data Oriented Design

- Book: [Data Oriented Design](https://www.dataorienteddesign.com/dodbook)
- [Data Oriented Design과 Cache Miss](http://rapapa.net/?p=2792)

데이터 지향 설계는
- 성능 지향의 설계이다.
- 객체지향 프로그래밍에서 성능 하락의 단점을 예로 든다.
- 객체마다 정의된 데이터들 보다 정리된 데이터들의 조합으로 최적의 성능을 이끌어낸다.
- 다른 패러다임과 함께 사용 가능하다.
- 함수형 프로그래밍과는 지향점이 다르다.
