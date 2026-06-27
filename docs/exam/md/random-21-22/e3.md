## 题目
设总体 $X$ 的概率分布为

$$
\begin{array}{c|ccc}
X & -1 & 0 & 2 \\
\hline
P & 2\theta & \theta & 1-3\theta
\end{array}
$$

其中 $\theta\ (0<\theta<\frac{1}{3})$ 是未知参数，又设 $X_{i}\ (i=1,\dots,n)$ 为来自于总体 $X$ 的简单随机样本。对抽得的一组样本 $x_{1}=-1$，$x_{2}=-1$，$x_{3}=0$，$x_{4}=2$，求 $\theta$ 的最大似然估计值。

## 步骤
对于离散型总体，样本的似然函数为各观测值概率的乘积：

$L(\theta) = \displaystyle\prod_{i=1}^{n} P(X=x_i)$

取对数得对数似然函数 $\ln L(\theta)$，求导并令其为零：

$\displaystyle\frac{\mathrm{d}\ln L(\theta)}{\mathrm{d}\theta} = 0$

解出的 $\theta$ 即为最大似然估计值 $\hat{\theta}$（需满足参数范围且二阶导数小于零以确认是极大值）。

## 题解
样本中 $x=-1$ 出现 2 次，$x=0$ 出现 1 次，$x=2$ 出现 1 次，故似然函数为：

$L(\theta) = (2\theta)^2 \cdot \theta \cdot (1-3\theta) = 4\theta^{3}(1-3\theta)$

取对数：

$\ln L(\theta) = \ln 4 + 3\ln\theta + \ln(1-3\theta)$

求导：

$\displaystyle\frac{\mathrm{d}\ln L(\theta)}{\mathrm{d}\theta} = \frac{3}{\theta} - \frac{3}{1-3\theta} = \frac{3(4\theta-1)}{\theta(1-3\theta)}$

令其为零：

$4\theta - 1 = 0 \quad\Rightarrow\quad \theta = \frac{1}{4}$

由于 $0 < \frac{1}{4} < \frac{1}{3}$，且二阶导数

$\displaystyle\frac{\mathrm{d}^{2}\ln L(\theta)}{\mathrm{d}\theta^{2}}\Big|_{\theta=1/4} = -192 < 0$

所以该点为极大值点。

因此 $\theta$ 的最大似然估计值为 $\hat{\theta} =$ **$\dfrac{1}{4}$**。
