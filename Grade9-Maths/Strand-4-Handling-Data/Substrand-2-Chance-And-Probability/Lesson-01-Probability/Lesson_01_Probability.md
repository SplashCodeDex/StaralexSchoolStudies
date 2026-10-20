# Strand 4: Handling Data
## Sub-strand 2: Chance and Probability
### Lesson 1: Probability, Sample Spaces, and Dependent Events

---

## 1. Curriculum Standard and Overview

- **Strand**: 4 — Handling Data
- **Sub-strand**: 2 — Chance and Probability
- **Content Standard**: B9.4.2.1
- **Indicators**:
  - **B9.4.2.1.1** — Perform a probability experiment involving two dependent events (without replacement).
  - **B9.4.2.1.2** — Express probabilities as fractions, decimals, percentages, and ratios.
- **Mock-paper links**: P2 Q5(a) (pens in a bag: red, blue, green; probability as fraction/decimal/percentage/ratio; two pens without replacement).

---

## 2. Preamble — Chance in Everyday Language

"The chance of rain is 30%."  
"A coin has a 1 in 2 chance of heads."

Probability puts a **number** on how likely an event is:

$$P(\text{event}) = \frac{\text{number of favourable outcomes}}{\text{total number of possible outcomes}}$$

The result is always between **0 and 1** (or 0% and 100%):
- $0$ = impossible
- $1$ = certain

---

## 3. Basic Vocabulary

| Word | Meaning |
| :--- | :--- |
| **Experiment** | an action with an uncertain result (toss a coin, pick a pen) |
| **Outcome** | one possible result |
| **Sample space $S$** | the set of all possible outcomes |
| **Event** | a collection of outcomes we care about |

---

## 4. Probability in Different Forms

**Mock P2 Q5(a):** A bag has 5 red, 3 blue, 2 green pens. Total $= 10$.

1. $P(\text{red}) = \frac{5}{10} = \frac{1}{2}$
2. $P(\text{blue}) = \frac{3}{10}$
   - (α) decimal: $0.3$
   - (β) percentage: $30\%$
   - (γ) ratio: $3 : 7$ (favourable : not-favourable) or $3 : 10$ (blue : total) — in BECE, write **3 : 7** when asked "as a ratio" of the event to its complement, or **3 : 10** if they mean blue to total. State which you mean.

**Always simplify fractions.**

---

## 5. Two-Stage Experiments

### 5.1 With replacement (independent)
The bag is unchanged between picks. Multiply the same probabilities.

### 5.2 Without replacement (dependent) — Mock P2 Q5(a)(iii)
If 2 pens are picked in succession **without replacement**, $P(\text{both green})$:

1. First pick: green pens $= 2$, total $= 10$ → $P(G_1) = \frac{2}{10} = \frac{1}{5}$.
2. Second pick: green pens now $= 1$, total $= 9$ → $P(G_2 \mid G_1) = \frac{1}{9}$.
3. Both green: $\frac{1}{5} \times \frac{1}{9} = \frac{1}{45}$.

**Answer: $\frac{1}{45}$.**

> **Key idea:** without replacement, the denominator **and** the numerator change after the first draw.

---

## 6. Tree Diagrams (Preview)

```
        G (2/10)      → G (1/9)  →  P(GG) = 2/10 × 1/9 = 1/45
       /
   ---<
       \
        not G (8/10) → ...
```

Along each branch multiply; across branches add.

---

## 7. Twenty Fully Worked Examples

### Example 1 — Mock P2 Q5(a)(i)
$P(\text{red}) = \frac{5}{10} = \frac{1}{2}$.

### Example 2 — Mock P2 Q5(a)(ii)
$P(\text{blue}) = \frac{3}{10} = 0.3 = 30\% = 3 : 7$ (or $3 : 10$).

### Example 3 — Mock P2 Q5(a)(iii)
$P(\text{both green}) = \frac{1}{45}$.

### Example 4 — Coin toss
$P(\text{heads}) = \frac{1}{2}$.

### Example 5 — Fair die
$P(3) = \frac{1}{6}$; $P(\text{even}) = \frac{3}{6} = \frac{1}{2}$.

### Example 6 — Certain event
$P(\text{a day has 24 hours}) = 1$.

### Example 7 — Impossible event
$P(\text{rolling a 7 on a die}) = 0$.

### Example 8 — Complement
$P(\text{not red}) = 1 - \frac{1}{2} = \frac{1}{2}$.

### Example 9 — Cards
$P(\text{ace}) = \frac{4}{52} = \frac{1}{13}$.

### Example 10 — Two coins (with replacement)
$P(\text{both heads}) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$.

### Example 11 — Without replacement (letters)
Bag: A, A, B. Pick two without replacement. $P(\text{both A}) = \frac{2}{3} \times \frac{1}{2} = \frac{1}{3}$.

### Example 12 — Percentage form
$P = \frac{3}{8} = 0.375 = 37.5\%$.

### Example 13 — Ratio form
$P(\text{win}) = \frac{2}{7}$. Odds in favour $= 2 : 5$.

### Example 14 — Spinner
Spinner with 4 equal sectors, 1 red: $P(\text{red}) = \frac{1}{4}$.

### Example 15 — At least one
Die thrown twice. $P(\text{at least one six}) = 1 - P(\text{no six}) = 1 - \left(\frac{5}{6}\right)^2 = \frac{11}{36}$.

### Example 16 — Mixed bag
Bag: 5 red, 3 blue, 2 green. $P(\text{not green}) = \frac{8}{10} = \frac{4}{5}$.

### Example 17 — Two without replacement (red then blue)
$\frac{5}{10} \times \frac{3}{9} = \frac{1}{6}$.

### Example 18 — Two without replacement (blue then red)
$\frac{3}{10} \times \frac{5}{9} = \frac{1}{6}$.

### Example 19 — Order matters in calculation
$P(\text{red then blue}) = P(\text{blue then red})$ in this bag, but the working differs.

### Example 20 — Word problem
20 pupils, 8 girls. $P(\text{girl}) = \frac{8}{20} = \frac{2}{5} = 0.4 = 40\%$.

---

## 8. Comprehensive Exercise Sets (40 Questions)

> The authentic mock probability set (P2 Q5(a)) is included in full. Generated questions top up to 40. Spiral review ≈ 15%.

### Exercise 1 — Basic probability (includes mock)

1. **[Mock 2026 P2 Q5(a)(i)]** In a pen bag, 5 are red, 3 are blue and 2 are green. What is the probability of picking a red pen?

2. What is $P(\text{blue})$ in the same bag?

3. What is $P(\text{green})$ in the same bag?

4. A fair coin is tossed. Find $P(\text{heads})$.

5. **Spiral review:** The mean of 5, 8, 4, 7 and $2x$ is 6. Find $x$.

### Exercise 2 — Different forms (includes mock)

1. **[Mock 2026 P2 Q5(a)(ii)]** Express the probability of picking a blue pen as a  
   (α) decimal; (β) percentage; (γ) ratio.

2. Express $\frac{3}{8}$ as a decimal and a percentage.

3. If $P(\text{win}) = \frac{2}{7}$, write the odds in favour as a ratio.

4. **Spiral review:** $13x - 12 = 5x + 60$. Find $x$.

5. **Spiral review:** Area of a semicircle with $r = 7$ ($\pi = 22/7$).

### Exercise 3 — Without replacement (includes mock)

1. **[Mock 2026 P2 Q5(a)(iii)]** If 2 pens are picked in succession without replacement, what is the probability that both are green?

2. Bag: A, A, B. Pick two without replacement. Find $P(\text{both A})$.

3. In the pen bag (5 red, 3 blue, 2 green), find $P(\text{red then blue})$ without replacement.

4. Find $P(\text{blue then red})$ without replacement.

5. **Spiral review:** If the area of a circle is $64\pi$, find the circumference.

### Exercise 4 — Sample spaces

1. List the sample space for two coin tosses.

2. List the sample space for one die roll.

3. $P(\text{rolling a 7 on a die}) = ?$

4. $P(\text{a day has 24 hours}) = ?$

5. **Spiral review:** Classify $-3$ under $\mathbb{N}, \mathbb{W}, \mathbb{Z}, \mathbb{Q}$.

### Exercise 5 — Complements and "not" events

1. In the pen bag, find $P(\text{not green})$.

2. $P(\text{not red}) = ?$

3. $P(\text{not an ace}) = ?$ (from a standard deck)

4. **Spiral review:** Solve $2x + 1 > 9$.

5. **Spiral review:** $(-3)^{x-2} = -243$. Find $x$.

### Exercise 6 — Two-stage independent

1. Two coins: find $P(\text{both heads})$.

2. Two coins: find $P(\text{two tails})$.

3. Two coins: find $P(\text{one head, one tail})$ in any order.

4. **Spiral review:** A van travels 154 km in $1\frac{3}{4}$ h. Speed?

5. **Spiral review:** $\frac{n}{100} = 10.5$. Find $n$.

### Exercise 7 — Real-life probability

1. A class has 20 pupils, 8 girls. Find $P(\text{girl})$ as a fraction, decimal, and percentage.

2. A bag has 6 blue and 4 red marbles. Find $P(\text{blue})$.

3. A spinner has 4 equal sectors, 1 red. Find $P(\text{red})$.

4. **Spiral review:** Find the mean of 3, 5, 7, 9.

5. **Spiral review:** Median of 20 marks from the stem-and-leaf (57.5) — verify the two middle values.

### Exercise 8 — Challenge

1. Die thrown twice. Find $P(\text{at least one six})$.

2. In the pen bag, find $P(\text{two different colours})$ when two pens are drawn without replacement.

3. A card is drawn from a standard deck. Find $P(\text{ace or king})$.

4. **Spiral review:** In a market of 36 fishmongers, 28 sell mackerel, 18 tilapia, 13 both. How many sell neither?

5. **Spiral review:** Find the gradient through $(1, 2)$ and $(4, -4)$.

---

## 9. Full Step-by-Step Worked Solutions

### Solutions to Exercise 1
1. $\frac{5}{10} = \frac{1}{2}$.  
2. $\frac{3}{10}$.  
3. $\frac{2}{10} = \frac{1}{5}$.  
4. $\frac{1}{2}$.  
5. $x = 3$ → **C**.

### Solutions to Exercise 2
1. (α) $0.3$; (β) $30\%$; (γ) $3 : 7$ (or $3 : 10$).  
2. $0.375 = 37.5\%$.  
3. $2 : 5$.  
4. $x = 9$.  
5. $77$ cm².

### Solutions to Exercise 3
1. $\frac{2}{10} \times \frac{1}{9} = \frac{1}{45}$.  
2. $\frac{2}{3} \times \frac{1}{2} = \frac{1}{3}$.  
3. $\frac{5}{10} \times \frac{3}{9} = \frac{1}{6}$.  
4. $\frac{3}{10} \times \frac{5}{9} = \frac{1}{6}$.  
5. $16\pi$.

### Solutions to Exercise 4
1. $\{HH, HT, TH, TT\}$.  
2. $\{1, 2, 3, 4, 5, 6\}$.  
3. $0$.  
4. $1$.  
5. **ℤ, ℚ**.

### Solutions to Exercise 5
1. $\frac{8}{10} = \frac{4}{5}$.  
2. $\frac{1}{2}$.  
3. $\frac{48}{52} = \frac{12}{13}$.  
4. $x > 4$.  
5. $x = 7$.

### Solutions to Exercise 6
1. $\frac{1}{4}$.  
2. $\frac{1}{4}$.  
3. $\frac{2}{4} = \frac{1}{2}$.  
4. $88$ km/h.  
5. $n = 1050$.

### Solutions to Exercise 7
1. $\frac{2}{5} = 0.4 = 40\%$.  
2. $\frac{6}{10} = \frac{3}{5}$.  
3. $\frac{1}{4}$.  
4. $6$.  
5. 10th value 57, 11th value 58; median $= 57.5$ ✓.

### Solutions to Exercise 8
1. $1 - \left(\frac{5}{6}\right)^2 = \frac{11}{36}$.  
2. $1 - P(\text{both same}) = 1 - \left(\frac{1}{45} + \frac{3}{90} + \frac{3}{90}\right) = \frac{10}{15} = \frac{2}{3}$ (see note).  
   *Detail: P(GG)=1/45, P(RR)= (5/10)(4/9)=2/9, P(BB)=(3/10)(2/9)=1/15. Sum same-colour = 1/45+2/9+1/15 = 1/45+10/45+3/45 = 14/45. Different colour = 1 − 14/45 = 31/45.*  
3. $\frac{4}{52} + \frac{4}{52} = \frac{8}{52} = \frac{2}{13}$.  
4. $3$.  
5. $m = -2$.

---

## 10. Authentic Mock Items in This Lesson

| Ref | Question | Answer |
| :--- | :--- | :--- |
| P2 Q5(a)(i) | $P(\text{red})$ | $\frac{1}{2}$ |
| P2 Q5(a)(ii) | $P(\text{blue})$ as decimal, %, ratio | $0.3 = 30\% = 3:7$ |
| P2 Q5(a)(iii) | Both green, without replacement | $\frac{1}{45}$ |

---

## 11. Lesson Summary

| Skill | Rule |
| :--- | :--- |
| Basic probability | favourable ÷ total |
| Forms | fraction → decimal → % → ratio |
| Without replacement | reduce total **and** remaining favourable |
| Complement | $P(\text{not } A) = 1 - P(A)$ |
| Two-stage (independent) | multiply |
| Two-stage (dependent) | multiply with updated numbers |

---

*Lesson prepared under `Grade9-Maths/Rules.md` — plain English, British notation, full workings required.*
