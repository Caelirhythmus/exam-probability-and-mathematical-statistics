## 题目
设 $X_1,X_2,\ldots,X_n$ 为来自总体 $X$ 的样本，总体 $X$ 的概率密度函数为

$$
f(x)=
\begin{cases}
\theta^2 x e^{-\theta x}, & x>0,\\
0, & \text{其他},
\end{cases}
\quad (\theta>0)
$$

试求：
(1) 未知参数 $\theta$ 的矩估计量 $\hat{\theta}_1$；
(2) 未知参数 $\theta$ 的最大似然估计量 $\hat{\theta}_2$；
(3) 判断 $\hat{\theta}_1$ 是否为 $\theta$ 的无偏估计，并说明理由。

## 步骤
**（1）矩估计**  
计算总体均值 $E(X)$（该分布为 $\text{Gamma}(2,\theta)$），令 $E(X)=\overline{X}$ 解出 $\theta$。

**（2）最大似然估计**  
写出似然函数 $L(\theta)=\prod f(x_i)$，取对数求导，令导数为零解出 $\theta$。

**（3）无偏性判断**  
计算 $E(\hat{\theta}_1)$，若 $E(\hat{\theta}_1)=\theta$ 则为无偏估计，否则为有偏。

## 题解
**（1）矩估计量**

总体 $X$ 服从伽马分布 $\text{Gamma}(2,\theta)$，其期望为：

$E(X)=\displaystyle\int_0^{+\infty} x\cdot\theta^2 x e^{-\theta x}\,\mathrm{d}x
=\theta^2\int_0^{+\infty} x^2 e^{-\theta x}\,\mathrm{d}x
=\theta^2\cdot\frac{\Gamma(3)}{\theta^3}
=\frac{2}{\theta}$

令 $E(X)=\overline{X}$ 得：

$\displaystyle\frac{2}{\theta}=\overline{X}\quad\Rightarrow\quad\hat{\theta}_1=\frac{2}{\overline{X}}$

**（2）最大似然估计量**

似然函数：

$\displaystyle L(\theta)=\prod_{i=1}^{n} \theta^2 x_i e^{-\theta x_i}
= \theta^{2n}\!\left(\prod_{i=1}^{n} x_i\right) e^{-\theta\sum_{i=1}^{n} x_i}$

对数似然：

$\displaystyle\ln L(\theta)=2n\ln\theta+\sum_{i=1}^{n}\ln x_i-\theta\sum_{i=1}^{n} x_i$

求导：

$\displaystyle\frac{\mathrm{d}\ln L}{\mathrm{d}\theta}
= \frac{2n}{\theta}-\sum_{i=1}^{n} x_i$

令其为零：

$\displaystyle\frac{2n}{\theta}-\sum_{i=1}^{n} x_i = 0
\quad\Rightarrow\quad
\hat{\theta}_2 = \frac{2n}{\sum_{i=1}^{n} X_i} = \frac{2}{\overline{X}}$

所以矩估计量与最大似然估计量相同：$\hat{\theta}_1=\hat{\theta}_2=\dfrac{2}{\overline{X}}$。

**（3）无偏性判断**

$Y=\sum_{i=1}^{n} X_i$ 服从 $\text{Gamma}(2n,\theta)$，其密度为 $f_Y(y)=\dfrac{\theta^{2n}}{\Gamma(2n)}y^{2n-1}e^{-\theta y}$。

$\displaystyle E\!\left(\frac{1}{Y}\right)=\int_0^{+\infty}\frac{1}{y}\cdot\frac{\theta^{2n}}{\Gamma(2n)}y^{2n-1}e^{-\theta y}\,\mathrm{d}y
= \frac{\theta^{2n}}{\Gamma(2n)}\int_0^{+\infty} y^{2n-2}e^{-\theta y}\,\mathrm{d}y$

$\displaystyle =\frac{\theta^{2n}}{\Gamma(2n)}\cdot\frac{\Gamma(2n-1)}{\theta^{2n-1}}
= \frac{\theta\Gamma(2n-1)}{\Gamma(2n)}
= \frac{\theta}{2n-1}$

因此

$E(\hat{\theta}_1)=E\!\left(\frac{2}{\overline{X}}\right)
= 2n\,E\!\left(\frac{1}{Y}\right)
= 2n\cdot\frac{\theta}{2n-1}
= \frac{2n}{2n-1}\,\theta \neq \theta$

由于 $E(\hat{\theta}_1)\neq\theta$，$\hat{\theta}_1$ **不是** $\theta$ 的无偏估计（存在正偏）。但当 $n\to\infty$ 时，$\dfrac{2n}{2n-1}\to 1$，故 $\hat{\theta}_1$ 是渐近无偏估计。
