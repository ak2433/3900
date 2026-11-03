# Practice Quiz #3: Answer Key for Variations 2, 3, and 4

These are short answers for checking your work. See the [Variation 1 walkthrough](Variation1_Walkthrough.md) for the full method on each question type.

---

## Variation 2

[← Back to Variation 2](Variation2_Quiz.md)

**Q1.** Rows 1–3 are treated ($n_t=3$), rows 4–5 are untreated, and $N=5$.
- **(a) ATT: option 5.** $\tfrac13(90+100+80)-\tfrac13(50+60+40)=90-50=\mathbf{40}$.
- **(b) ATE: option 3.** $\tfrac15(400)-\tfrac15(240)=80-48=\mathbf{32}$.
- **(c) IPW: option 2.** Treated: $95/.5+110/.8+80/.4=190+137.5+200=527.5$. Untreated: $40/.8+45/.75=50+60=110$. $\tfrac15(527.5-110)=\mathbf{83.5}$. (Option 3 divides by the group sizes instead of $N$.)

**Q2.** With 200 points, choose the **linear regression**: 512 cells and only 200 people means most cells are empty or hold one person, so the cell means would have huge variance. With 200,000 points, choose the **observed averages**: about 390 people per cell gives low variance, and there is no functional-form bias.

**Q3.**
- **(a) Standardization / g-formula.** The outcome is easy to model.
- **(b) IPW and AIPW.** The propensity model is correct, but the outcome model is missing the confounder $B$. The g-formula fails, while AIPW needs only one correct model.
- **(c) Standardization and AIPW.** The outcome model is correct, but the propensity model is missing $B$.

**Q4.**
- **(a) Higher bias: no caliper.** It keeps bad, far-away matches.
- **(b) Higher variance: caliper.** Treated units without a close match get dropped, leaving fewer units. The estimand also changes to the FSATT.

**Q5.**

| | U1 | U2 | Picks |
|---|---|---|---|
| Manhattan | $3+4=7$ | $8+0=8$ | U1 |
| Euclidean | $\sqrt{9+16}=5$ | $8$ | U1 |
| Mahalanobis | $\sqrt{(3/10)^2+(4/2)^2}\approx2.02$ | $\sqrt{(8/10)^2}=0.8$ | **U2** |

A 4-year education gap is 2 SDs, which is huge, while an 8-year age gap is only 0.8 SD. Mahalanobis measures each difference relative to that variable's natural spread, so the answer doesn't depend on arbitrary units.

**Q6.** Income is continuous, so almost no two people have exactly the same income and exact matching finds no matches. CEM coarsens income into bins (e.g. \$10,000 wide) and matches exactly on the bin. Wider bins give more matches (lower variance) but bigger income differences within a bin (higher bias). Narrower bins give the reverse.

---

## Variation 3

[← Back to Variation 3](Variation3_Quiz.md)

**Q1.** Watch out: the rows are **not** sorted. The treated rows are 2 and 4; the untreated rows are 1 and 3.
- **(a) ATT: option 2.** $\tfrac12(110+100)-\tfrac12(60+70)=105-65=\mathbf{40}$.
- **(b) ATE: option 4.** $\tfrac14(360)-\tfrac14(230)=90-57.5=\mathbf{32.5}$.
- **(c) IPW: option 4.** Treated: $120/.6+90/.75=200+120=320$. Untreated: $40/.8+63/.7=50+90=140$. $\tfrac14(320-140)=\mathbf{45}$. (Option 3 has a minus sign inside the untreated sum.)

**Q2.** With 60 points, choose the **main-effects logistic regression**: 13 parameters is manageable, but about 90 parameters fit to 60 observations would overfit badly (huge variance, possibly perfect separation). With 60,000 points, choose the **richer model**: its variance is now small, and the interactions and squared terms reduce bias.

**Q3.**
- **(a) Standardization / g-formula.** Propensity scores near 0 or 1 give enormous IPW weights ($1/0.01=100$), so one person can dominate the estimate (huge variance).
- **(b) None of these.** $H$ is a **mediator**, a descendant of $A$. Adjusting for it blocks part of the effect we want, so the total effect isn't identified, whichever estimator you use.
- **(c) Standardization and AIPW.** The outcome model is correct and the propensity model is wrong.

**Q4.**
- **(a) Higher variance: 1 to 1.** Each counterfactual rests on a single control.
- **(b) Higher bias: 3 to 1.** The 2nd and 3rd nearest controls are worse look-alikes.

**Q5.** SAT spans about 1,200 points while GPA spans 4, so under Euclidean distance a 10-point SAT gap outweighs a full 2.0 GPA gap, and GPA is essentially ignored. Mahalanobis divides each difference by that variable's variance, so both covariates count on a comparable scale. It also accounts for the SAT–GPA correlation, so their shared "academic ability" information isn't double-counted.

**Q6.** The matched sets are **not balanced** on age. Either the propensity model is misspecified (e.g. age entered wrongly or should be nonlinear), or there is a **lack of overlap**: few older controls exist, which suggests a possible positivity problem. Possible fixes:
- Re-specify the propensity model (e.g. add age terms or interactions).
- Use a caliper (the estimand becomes the FSATT).
- Match exactly, or with CEM, on age.
- Combine matching with regression adjustment for leftover differences.

Do all of this **before** looking at the outcomes.

---

## Variation 4

[← Back to Variation 4](Variation4_Quiz.md)

**Q1.** Rows 1, 2, and 4 are treated ($n_t=3$), row 3 is untreated, and $N=4$.
- **(a) ATT: option 3.** $\tfrac13(210)-\tfrac13(120)=70-40=\mathbf{30}$.
- **(b) ATE: option 1.** $\tfrac14(285)-\tfrac14(170)=71.25-42.5=\mathbf{28.75}$.
- **(c) IPW: option 3.** Treated: $88/.8+60/.5+63/.7=110+120+90=320$. Untreated: $45/.6=75$. $\tfrac14(320-75)=\mathbf{61.25}$. (Option 2 uses $\tfrac13$ and 1 instead of $\tfrac14$.)

**Q2.** With 20 points, choose **linear regression**: a degree-10 polynomial has 11 parameters fit to 20 points, so it wiggles wildly (high variance). With 1,000 points, choose the **degree-10 polynomial**: its variance is now small and it can bend to fit the curve. The **linear model's bias never goes away**: a straight line can never become a curve, no matter how much data you have (misspecification).

**Q3.**
- **(a) IPW.** The treatment mechanism is known and logistic, while the outcome is complex.
- **(b) IPW, standardization, and AIPW.** Both models are correct, so all three methods are reliable.
- **(c) None of these.** Both models are misspecified (the true propensity is logistic, not linear; the true outcome is complex, not linear), and double robustness allows only one failure.

**Q4.**
- **(a) Higher bias: wide caliper.** It allows matches whose propensity scores differ by up to 0.25.
- **(b) Higher variance: narrow caliper.** Many treated units find no control within 0.01 and get dropped.

**Q5.** Euclidean distance adds squared differences in raw units. In USD, a \$1,000 income gap counts as 1,000 while a 10-year age gap counts as 10, so income dominates. In thousands of USD, that same income gap counts as only 1, so age now dominates and the nearest neighbors change. The matches depend on an arbitrary choice of units. Mahalanobis distance divides by each variable's variance (through $\Sigma^{-1}$). Rescaling a variable rescales its variance by the same factor, so the distance is unchanged: it is **scale-free**.

**Q6.** *"Matching is an estimation strategy. It does not solve identification problems."* Balance on the 30 measured covariates says nothing about the unmeasured $U$. The backdoor path $A\leftarrow U\to Y$ stays open, so conditional exchangeability given the measured covariates fails, and the estimate is biased no matter how good the matches look. Matching does target the ATT, so that label is right; the estimate just isn't causal here.
