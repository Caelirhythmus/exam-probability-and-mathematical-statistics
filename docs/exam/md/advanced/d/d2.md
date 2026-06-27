## 题目
设连续型随机变量 $X$ 的概率密度函数为

$$
f(x)=
\begin{cases}
a x^2 + b x + c, & 0\le x\le 1,\\
0, & \text{其他}
\end{cases}
$$

其中 $a,b,c$ 为未知常数。已知 $E(X)=0.5$，$E(X^2)=0.4$，试求：
(1) 常数 $a,b,c$ 的值；
(2) $X$ 的方差 $D(X)$。

## 步骤
密度函数满足归一化 $\displaystyle\int_{-\infty}^{+\infty}f(x)\,\mathrm{d}x = 1$，结合已知的一、二阶矩，列方程组解 $a,b,c$。

$D(X) = E(X^2) - [E(X)]^2$。

## 题解
**（1）常数 $a,b,c$**

由密度函数归一化：

$\displaystyle\int_{0}^{1} (ax^2+bx+c)\,\mathrm{d}x
= \left[\frac{a}{3}x^3 + \frac{b}{2}x^2 + cx\right]_{0}^{1}
= \frac{a}{3} + \frac{b}{2} + c = 1$
<span style="display:block; text-align:right">①</span>

由 $E(X)=0.5$：

$\displaystyle\int_{0}^{1} x(ax^2+bx+c)\,\mathrm{d}x
= \int_{0}^{1} (ax^3+bx^2+cx)\,\mathrm{d}x$
$\displaystyle = \left[\frac{a}{4}x^4 + \frac{b}{3}x^3 + \frac{c}{2}x^2\right]_{0}^{1}
= \frac{a}{4} + \frac{b}{3} + \frac{c}{2} = 0.5$
<span style="display:block; text-align:right">②</span>

由 $E(X^2)=0.4$：

$\displaystyle\int_{0}^{1} x^2(ax^2+bx+c)\,\mathrm{d}x
= \int_{0}^{1} (ax^4+bx^3+cx^2)\,\mathrm{d}x$
$\displaystyle = \left[\frac{a}{5}x^5 + \frac{b}{4}x^4 + \frac{c}{3}x^3\right]_{0}^{1}
= \frac{a}{5} + \frac{b}{4} + \frac{c}{3} = 0.4$
<span style="display:block; text-align:right">③</span>

解方程组 ① ② ③ 得：

$a = 12,\qquad b = -12,\qquad c = 3$

因此

$$
f(x)=
\begin{cases}
12x^2 - 12x + 3, & 0\le x\le 1,\\
0, & \text{其他}.
\end{cases}
$$

**（2）方差**

$D(X) = E(X^2) - [E(X)]^2 = 0.4 - 0.5^2 = 0.15$
