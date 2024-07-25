---
title: Linear Programming - Interior-Point Methods
date: 2024-07-10 00:34:53
cover: https://quantum-computing.lehigh.edu/wp-content/uploads/2020/02/Screenshot-2020-02-24-10.43.24.png
single_column: true
categories: math
tags: math
---

### Problem 1
**Assume the linear model:**
$$ Y = X \beta + \epsilon$$ 
where $X'X=I$ and $\epsilon \sim N(0,\sigma^2I)$  
**Find the numerical solution for the elastic net in the form:**
$$\hat{\beta_{en}} = argmin_b \frac{1}{2} \|Y-Xb\|_2^2 + \lambda\biggl(\frac{1}{2}(1-\alpha)\|b\|_2^2 + \alpha\sum\limits_{i=1}^p|b_i| \biggr)$$  
$$\hat{\beta_{en}} = argmin_b \frac{1}{2} \|Y-Xb\|_2^2 + \lambda\biggl(\frac{1}{2}(1-\alpha)\|b\|_2^2 + \alpha\sum\limits_{i=1}^p|b_i| \biggr)$$
- **What would be the value of the elastic net estimator with $\lambda = 1$ and $\alpha = 0.5$ if  $\hat{\beta}_{OLS} = 3?$**
- **How does the number of discoveries depend on the parameter $\alpha$**
- **Provide the numerical value for the expected number of false discoveries when $n = p = 1000$, $p_0 = 950$, $\sigma = 1$, and $\lambda = 2$ , and the power of detection of $X_1$ when $\beta_1 = 3$**

