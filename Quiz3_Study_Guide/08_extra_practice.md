# 8. Extra Practice Problems (with hidden solutions)

[← Practice quiz solutions](07_practice_quiz_solutions.md) · [Index](README.md)

These mirror the question types on the practice quiz. Work each one on paper, then expand the solution.

---

## Problem 1: Standardization, ATE vs ATT, and confounding

100 people. $L\in\{\text{Young},\text{Old}\}$.

| Group | # people | # treated | Mean $Y$ (treated) | Mean $Y$ (untreated) |
|---|---|---|---|---|
| Young | 60 | 20 | 10 | 6 |
| Old | 40 | 30 | 20 | 12 |

(a) Compute the naive (unadjusted) difference in means.
(b) Compute the ATE by standardization.
(c) Compute the ATT.
(d) Why does (a) differ from (b)?

<details>
<summary><b>Solution</b></summary>

**(a)** Treated mean = $\frac{20(10)+30(20)}{50}=\frac{800}{50}=16$. Untreated mean = $\frac{40(6)+10(12)}{50}=\frac{360}{50}=7.2$. Naive difference = **8.8**.

**(b)** CATE: young $10-6=4$, old $20-12=8$. Population shares: young .6, old .4.
$\widehat{ATE}=4(.6)+8(.4)=\mathbf{5.6}$

**(c)** ATT weights by the **treated** group's mix: 20 young and 30 old among 50 treated, so .4 and .6.
$\widehat{ATT}=4(.4)+8(.6)=\mathbf{6.4}$

**(d)** Old people are more likely to be treated (75% vs 33%) **and** have higher outcomes regardless of treatment. Age confounds the naive comparison.
</details>

---

## Problem 2: IPW on the same data

(a) Find the propensity score for young and for old people.
(b) Give the IPW weight for each of the four groups.
(c) Compute $\hat E(Y^1)$, $\hat E(Y^0)$, and the ATE by IPW.

<details>
<summary><b>Solution</b></summary>

**(a)** $\pi_{\text{young}}=20/60=1/3$; $\pi_{\text{old}}=30/40=3/4$.

**(b)**
| Group | Weight |
|---|---|
| Young treated | $1/(1/3)=3$ |
| Young untreated | $1/(2/3)=1.5$ |
| Old treated | $1/(3/4)=4/3$ |
| Old untreated | $1/(1/4)=4$ |

**(c)** $\hat E(Y^1)=\frac{1}{100}[20\cdot3\cdot10+30\cdot\frac43\cdot20]=\frac{600+800}{100}=14$
$\hat E(Y^0)=\frac1{100}[40\cdot1.5\cdot6+10\cdot4\cdot12]=\frac{360+480}{100}=8.4$
$\widehat{ATE}=\mathbf{5.6}$, the same as standardization, as expected when the propensity is computed exactly.
</details>

---

## Problem 3: Parametric g-formula with and without an interaction

Four people with $L=0,1,2,3$. Persons with $L=2$ and $L=3$ are treated.

(a) The fitted model is $\hat E(Y\mid A,L)=5+3A+2L$. Find the ATE and ATT.
(b) The fitted model is $\hat E(Y\mid A,L)=5+3A+2L+1\cdot(A\times L)$. Find the ATE and ATT.

<details>
<summary><b>Solution</b></summary>

**(a)** Each person's predicted effect $=\hat E(Y\mid1,\ell)-\hat E(Y\mid0,\ell)=3$. So **ATE = ATT = 3** (the g-formula collapses to $\hat\beta$).

**(b)** Predicted effect for person $i$ $=3+\ell_i$:
| $L$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| effect | 3 | 4 | 5 | 6 |

ATE = average over all four = $(3+4+5+6)/4=\mathbf{4.5}$
ATT = average over the treated ($L=2,3$) = $(5+6)/2=\mathbf{5.5}$

The ATT is larger because the treated have higher $L$, and the effect grows with $L$.
</details>

---

## Problem 4: IPW from a table

| $i$ | $A_i$ | $Y_i$ | $\hat\pi_i$ |
|---|---|---|---|
| 1 | 1 | 12 | .6 |
| 2 | 1 | 8 | .4 |
| 3 | 0 | 5 | .5 |
| 4 | 0 | 9 | .25 |
| 5 | 1 | 10 | .8 |

(a) Compute the IPW estimate of the ATE.
(b) Which person gets the largest weight, and why?

<details>
<summary><b>Solution</b></summary>

**(a)** $N=5$.
Treated: $12/.6=20$, $8/.4=20$, $10/.8=12.5$, sum $=52.5$
Untreated: $5/(1-.5)=10$, $9/(1-.25)=12$, sum $=22$
$\widehat{ATE}=\frac{52.5-22}{5}=\frac{30.5}{5}=\mathbf{6.1}$

**(b)** Person 2: weight $1/.4=2.5$. They were treated even though people like them had only a 40% chance of treatment, so each such person "stands in" for 2.5 people in the all-treated world. (Person 4's weight is only $1/.75\approx1.33$ because, with $\pi=.25$, being untreated was likely for them.)
</details>

---

## Problem 5: One person's AIPW contribution

For person $i$: $\hat E(Y\mid A=1,\ell_i)=50$, $\hat\pi_i=.25$, $Y_i=62$.

(a) If $A_i=1$, what does person $i$ contribute (before dividing by $N$) to $\hat E(Y^1)$?
(b) If instead $A_i=0$?

<details>
<summary><b>Solution</b></summary>

**(a)** $50+\frac{1}{.25}(62-50)=50+4(12)=\mathbf{98}$

**(b)** $50+\frac{0}{.25}(\ldots)=\mathbf{50}$. Untreated people contribute only their outcome-model prediction to $\hat E(Y^1)$.
</details>

---

## Problem 6: Which method is reliable?

For each scenario, mark g-formula, IPW, AIPW as reliable or not. Assume $L$ is a sufficient adjustment set unless stated otherwise.

(a) True $E(Y\mid A,L)$ is highly nonlinear; you fit linear. True $P(A=1\mid L)$ is logistic in $L$; you fit logistic regression in $L$.
(b) Both models are fit with the correct functional form.
(c) You fit flexible ML for both, but there's an **unmeasured** confounder $U$.
(d) True outcome model is linear, fit linear. True propensity is complicated, fit linear.

<details>
<summary><b>Solution</b></summary>

| | g-formula | IPW | AIPW |
|---|---|---|---|
| (a) | ❌ | ✅ | ✅ |
| (b) | ✅ | ✅ | ✅ |
| (c) | ❌ | ❌ | ❌ (identification failure) |
| (d) | ✅ | ❌ | ✅ |
</details>

---

## Problem 7: Matching algorithms

Treated: T1 (age 30, $Y=50$), T2 (age 32, $Y=60$). Controls: C1 (age 31, $Y=45$), C2 (age 25, $Y=35$).

(a) 1:1 **greedy** matching without replacement, matching T1 first. What are the matches and the total distance?
(b) 1:1 **optimal** matching without replacement. What are the matches and the total distance?
(c) 1:1 matching **with replacement**: compute the ATT.

<details>
<summary><b>Solution</b></summary>

**(a)** T1 grabs its nearest, C1 (distance 1). C1 is used up, so T2 gets C2 (distance 7). **Total = 8.**

**(b)** Consider all pairings: {T1–C1, T2–C2} has total 1 + 7 = 8; {T1–C2, T2–C1} has total 5 + 1 = **6**. Optimal picks the second. *"Optimal is better, just computationally harder."*

**(c)** Both treated units match to C1 (distances 1 and 1, so better matches and lower bias).
$\widehat{ATT}=\frac{(50-45)+(60-45)}{2}=\frac{5+15}{2}=\mathbf{10}$
C1 is used twice and C2 not at all, so the estimate depends heavily on one control's outcome (higher variance).
</details>

---

## Problem 8: Distance metrics

Treated: (age 40, educ 12). Candidate A: (age 44, educ 14). Candidate B: (age 41, educ 17).

(a) Manhattan distance to each?
(b) Euclidean distance to each?
(c) Mahalanobis distance if SD(age) = 2, SD(educ) = 5, uncorrelated?

<details>
<summary><b>Solution</b></summary>

**(a)** A: $4+2=6$. B: $1+5=6$. A **tie**.

**(b)** A: $\sqrt{16+4}=\sqrt{20}\approx4.47$. B: $\sqrt{1+25}=\sqrt{26}\approx5.10$. Picks **A**.

**(c)** A: $\sqrt{(4/2)^2+(2/5)^2}=\sqrt{4+0.16}\approx2.04$. B: $\sqrt{(1/2)^2+(5/5)^2}=\sqrt{0.25+1}\approx1.12$. Picks **B**.

In this sample a 4-year age gap is large relative to the spread of ages (2 SDs), while a 5-year education gap is only 1 SD. Mahalanobis measures each difference in "SDs" rather than raw units.
</details>

---

## Problem 9: True or false

1. Matching on $L$ removes bias from an unmeasured confounder $U$.
2. With OLS and no interactions, the g-formula ATE equals the coefficient on $A$.
3. The IPW estimator of $E(Y^1)$ divides by the number of treated people.
4. A treated person with $\hat\pi=0.1$ gets weight 10.
5. Caliper matching estimates the ATE.
6. Matching with replacement tends to lower bias.
7. Propensity score matching guarantees every matched pair has identical covariates.
8. An empty cell in a finite sample is exactly the same as a positivity violation.
9. AIPW is consistent if both the outcome and propensity models are wrong.
10. 5:1 matching has lower variance than 1:1 matching.
11. A more complex model always gives a better causal estimate.
12. Coarsened exact matching is very transparent and directly targets balance in $L$.

<details>
<summary><b>Solution</b></summary>

1. **F**. Matching is estimation, not identification.
2. **T**. $\frac1n\sum(\hat\alpha+\hat\gamma\ell_i+\hat\beta)-\frac1n\sum(\hat\alpha+\hat\gamma\ell_i)=\hat\beta$.
3. **F**. It divides by $N$, the total sample size.
4. **T**. $1/0.1=10$.
5. **F**. It estimates the **FSATT** (feasible sample ATT).
6. **T**. Each treated unit gets its best match.
7. **F**. Balance holds only **on average**.
8. **F**. It's *almost* like one, but in the population such people exist; we just didn't sample them.
9. **F**. Double robustness requires at least one model to be correct.
10. **T**. Averaging more controls reduces variance (at the cost of more bias).
11. **F**. Complex models have high variance, especially in small samples.
12. **T**. Its drawbacks are choosing the buckets and still possibly having no matches.
</details>

---

## Problem 10: Short answers

(a) Why can IPW estimates have very high variance?
(b) Why does matching usually target the ATT rather than the ATE?
(c) When would the g-formula ATE and ATT differ?
(d) What should you check after matching, before looking at outcomes?
(e) You have 200 observations and 25 confounders. Would you estimate $E(Y\mid A,L)$ with subgroup means? Why not?

<details>
<summary><b>Solution</b></summary>

**(a)** If some $\hat\pi_i$ are near 0 (for treated) or near 1 (for untreated), the weights $1/\hat\pi$ or $1/(1-\hat\pi)$ become huge, and a few people dominate the estimate. This is often a sign of (near) positivity violations.

**(b)** For treated units, $Y^1$ is observed (consistency), so we only need to impute their $Y^0$ by finding similar controls. The ATE would also require imputing $Y^1$ for every control.

**(c)** When the treatment effect varies with $L$ (heterogeneity; e.g. the model has an $A\times L$ interaction) **and** the treated group's distribution of $L$ differs from the whole population's.

**(d)** Balance: compare means and distributions of $L$ (and of $\hat\pi$) between treated and matched controls; look at overlap plots. Lack of overlap may indicate a positivity violation.

**(e)** No. The curse of dimensionality: there are far more subgroups than observations, so nearly every cell lacks treated or untreated units. Use a statistical model (parametric g-formula, IPW, AIPW) or propensity score matching instead.
</details>

---

## Final checklist before the quiz

- [ ] I can write the g-formula ATE and ATT formulas and pick them out of a table.
- [ ] I know IPW uses $1/\hat\pi$ for treated, $1/(1-\hat\pi)$ for untreated, and divides by total $N$.
- [ ] I can explain double robustness and fill in the "which method is reliable" table.
- [ ] I know that omitting a confounder breaks **every** method.
- [ ] I can explain bias vs variance and which model to use with small vs large $n$.
- [ ] I know the bias–variance direction for 1:1 vs k:1, with vs without replacement, and caliper.
- [ ] I can compute Manhattan and Euclidean distances, and explain why Mahalanobis handles units and correlation.
- [ ] I can explain why propensity score matching beats CEM with many covariates.
- [ ] I remember: **matching and modeling are estimation; they don't fix identification.**

[Back to index](README.md)
