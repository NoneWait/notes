## 一个HMM tagger的组件

一个HMM主要有两种组件，分别是$A$和$B$概率。

- $A$矩阵表示了tag的转移(transition)概率$P(t_i|t_{i-1})$,表示了在给定前一个tag的时候，当前tag的发生概率
- $B$矩阵表示了发射(emisiion)概率（observation likelihoods）$P(w_i|t_i)$，表示给定一个tag，它和给定单词的关联概率

<img src=".\figures\image-20200917103436056.png" alt="ad" style="zoom:67%;" />

## HMM tagging解码

### HMM的解码

给定输入：一个HMM $\lambda=(A,B)$,一个观测序列$O = o_1, o_2,...,o_T$

目标：找到一个可能性最大的状态序列：$Q=q_1q_2q_3,...,q_T$

### POS任务

我们的目标就是给定观测到的单词序列，选择一个最大概率的tag序列
$$
\hat{t}^{n}_{1} = argmax(P(t_1^n|w_1^n))
$$
接着，使用贝叶斯规则
$$
\hat{t}^{n}_{1} = argmax(\frac{P(w_1^n|t_1^n)P(t_1^n)}{p(w_1^n)})
$$
为了方便，可以去除分母$p(w_1^n)$

HMM tagger使用了两个用于简化的假设，

- 一个词发生的概率仅和自己的tag的相关，独立与其他相邻的词和tags：
  $$
  P(w_1^n|t_1^n)\approx \prod^{n}_{i=1}P(w_i|t_i)
  $$
  

- 一元假设，一个tag的概率只依赖前一个tag
  $$
  P(t_1^n)\approx \prod^{n}_{i=1}P(t_i|t_{i-1})
  $$

 所以，最终结果为：

![image-20200917110342945](.\figures\image-20200917110342945.png)

可以看出两项分别是$A$和$B$。



## 维特比算法

