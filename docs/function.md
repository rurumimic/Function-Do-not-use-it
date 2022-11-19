# 함수

**함수는 이미 익숙하다**: 중학교 1학년 1학기 - IV. 좌표평면과 그래프

---

### 간단한 함수

| 수학 함수                                                       | 좌표 평면과 그래프                                                                 |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| ![f(x) = \frac{1}{\sqrt{x}}](../images/inverse-square-root.svg) | <img src="../images/inverse-square-root.png" style="max-width: 300px; width:100%"> |

```c
float y = 1 / sqrt(x);
```

### 미분 함수

|        | 함수                     |
| ------ | ------------------------ |
| 함수   | ![](../images/xr.svg)    |
| 도함수 | ![](../images/rxr-1.svg) |


```Matlab
syms x r
f = x .^ r

g = diff(f)
% ans = r * x .^ (r-1)

subs(g, [x, r], [3, 2])
% ans = 6
```

`도함수 = 미분함수(함수)`

---

## 함수의 합성: 분해와 조립

| 함수 합성                                                                                                                                                                                         | 새로운 함수                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="../images/funcmachine.png" alt="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Function_machine5.svg/1280px-Function_machine5.svg.png" style="max-width: 300px; width:100%"> | <img src="../images/composition.png" alt="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Example_for_a_composition_of_two_functions.svg/499px-Example_for_a_composition_of_two_functions.svg.png" style="max-width: 300px; width:100%"> |

```c
int f(int x) { return x * x; }
int g(int x) { return x + 1; }

g(f(3)); // 10
```
