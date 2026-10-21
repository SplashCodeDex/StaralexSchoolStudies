# Strand 1: Number
## Sub-strand 2: Number Operations
### Lesson 3 (Day 5): Decimal Operations and Multi-Step Word Problems

---

## 1. Curriculum Standard and Overview

- **Strand**: 1 — Number
- **Sub-strand**: 2 — Number Operations
- **Content Standard**: B9.1.2.2 — Solve operations and word problems involving the four basic operations on decimals, with controlled precision.
- **Indicators**:
  - **B9.1.2.2.1** — Solve operations involving addition, subtraction, multiplication and division using word problems.
  - **B9.1.2.2.2** — Solve word problems involving the four basic operations and round the answers to the nearest two decimal places or to some significant figures.
- **Scope of this lesson**:
  1. Column addition and subtraction of decimals (the "line up the points" rule).
  2. Multiplication of decimals (decimal-place counting) and multiplication by powers of 10.
  3. Long division: whole-number divisors, then making a decimal divisor whole by shifting.
  4. Terminating and recurring decimals.
  5. Precision control: truncating versus rounding, decimal places (d.p.) and significant figures (s.f.).
  6. Multi-step word problems: money, inventory, time, and the bridge from word sentences to algebra.
- **Mock-paper links (this lesson covers directly)**:
  - Mock 2026 P1 Q1 — decimal addition, correct to 1 d.p. *(worked Example 1)*
  - Mock 2026 P1 Q14 — $(0.07 \times 0.02) \div 14$ *(worked Example 7)*
  - Mock 2026 P1 Q32 — weight of 112 flies at 0.1 kg each *(worked Example 8)*
  - Mock 2026 P2 Q2(a)(ii) — $0.893 \times 14.7$ correct to 4 d.p. *(worked Example 4)*
  - Mock 2026 P2 Q3(a) — Mark's hourly pay at GH₵ 8.25 *(worked Example 5; its rate-and-financial home is the Ratios & Financial lesson)*
  - Mock 2026 P2 Q5(b) — time arithmetic: Takoradi to Tema journey *(worked Example 13)*
- **Exercise quota (user override, October 2026)**: **5 exercise sections × 5 questions = 25 questions, no multiple choice, every question with a full worked answer.** Spiral review: 12% — questions 1.5, 2.3, 4.5 revisit earlier lessons (place value/standard form, indices).

---

## 2. Preamble — What Decimals Really Say

A decimal fraction is a fair share written on a base-10 ladder. Every step to the right of the decimal point divides by 10 again:

| Place value | Fraction | Size |
| :--- | :--- | :--- |
| Units (ones) | 1 | whole |
| Tenths | $1/10$ | 0.1 |
| Hundredths | $1/100$ | 0.01 |
| Thousandths | $1/1000$ | 0.001 |
| Ten-thousandths | $1/10000$ | 0.0001 |

So $13.458$ means $13 + \dfrac{4}{10} + \dfrac{5}{100} + \dfrac{8}{1000}$. Money trained you on this already: GH₵ 13.458 is 13 cedis, 45 pesewas and $8/10$ of a pesewa. *(You met this ladder in the Place Value lesson; here we work with it.)*

**One fact that unlocks everything in this lesson:**

> **Widening a decimal with trailing zeros changes nothing.**
> $6.5 = 6.50 = 6.500$. The zeros fill the ladder, they do not move it.

This lets you always pad the shorter number with zeros before subtracting, and always find something to share round during division.

---

## 3. Column Addition and Subtraction — Line Up the Points

The rule from the Place Value lesson applies to every decimal sum:

> **Write the numbers in a column with every decimal point directly under the one above it.** Zeros may be added at the end of any shorter number — adding trailing zeros changes nothing.

Column-wise, $124.3 + 0.275 + 74.06$ becomes:

```
     1 2 4 . 3 0 0
         0 . 2 7 5
        7 4 . 0 6 0
   -----------------
       1 9 8 . 6 3 5
```

The padding ($124.3 = 124.300$, $74.06 = 74.060$) is what makes the columns trustworthy. Subtraction uses the exact same column layout, "borrow" working exactly like whole numbers.

---

## 4. Multiplying Decimals — Count the Places

The easy shortcut: **multiply the numbers without points first, then insert the point so the answer has as many decimal places as the two factors had in total.**

$$0.893 \times 14.7: \qquad 893 \times 147 = 131271$$

- $0.893$ has 3 decimal places, $14.7$ has 1 → the answer must have $3 + 1 = 4$ decimal places → $13.1271$.

Why does counting work? Because $0.893 = 893/1000$ and $14.7 = 147/10$, so the product is $\dfrac{893 \times 147}{1000 \times 10} = \dfrac{131271}{10^4}$ — dividing by $10^4$ is the same as moving the point 4 places. *(This is the same "shift by powers of 10" idea as standard form from the Place Value lesson.)*

**Multiplying by 10, 100, 1000** just slides the point rightward: $24.5 \times 100 = 2450$. And a multiplication such as $0.07 \times 0.02$ is $7 \times 2$ with the point placed $2 + 2 = 4$ places left: $0.0014$.

---

## 5. Dividing Decimals — Make the Divisor Whole

Division needs the divisor (the number outside) to be a whole number. Two cases:

### 5.1 Whole-number divisor — plain long division

Use ordinary long division and keep the point of the dividend in line. Example: $122.5 \div 5$.

| Step | What happens | Working |
| :--- | :--- | :--- |
| 1 | Divide 12 by 5 → 2, remainder 2 | $5 \times 2 = 10$ |
| 2 | Bring down 2 → 22 → divide by 5 → 4, remainder 2 | $5 \times 4 = 20$ |
| 3 | Pass the point into the answer (it travels straight through) | answer so far 2**.**4 |
| 4 | Bring down 5 → 25 → divide by 5 → 5, no remainder | $5 \times 5 = 25$ |

Quotient: $24.5$. Check: $24.5 \times 5 = 122.5$ — correct.

### 5.2 Decimal divisor — shift until the divisor is whole

Move the point of **both** numbers the *same* number of places so the divisor becomes whole:

$$6.25 \div 0.25 = 625 \div 25 = 25 \qquad \text{(2-place shift)}$$

$$8.58 \div 2.6 = 85.8 \div 26 = 3.3 \qquad \text{(1-place shift)}$$

Shifting both numbers the same amount multiplies both by the same power of 10, and dividing both dividend and divisor by equal amounts changes nothing: $\dfrac{a \times 10}{b \times 10} = \dfrac{a}{b}$.

---

## 6. Terminating and Recurring Decimals

- A decimal **terminates** when it stops: $3 \div 40 = 0.075$. It stops because the division reaches remainder 0.
- A decimal **recurring (repeating)** when the same digit-block cycles forever: $2 \div 3 = 0.666\ldots$, written $0.6$ recurring. The sixes never end, no remainder ever reaches 0.

How does a recurring decimal's multiplication behave? For example, $0.6$ recurring $\times 3$: $0.666\ldots \times 3 = 1.999\ldots$, which is exactly 2 — that is why rounding matters: we agree on a stopping place (**precision control**, next section).

**How to state a rounded recurring decimal:** $2 \div 3 = 0.666\ldots \approx 0.67$ (2 d.p.) — look at the third decimal digit (6) and round the second digit up.

---

## 7. Precision Control — Truncating vs Rounding, d.p. vs s.f.

Two different ways of cutting a decimal:

| Method | Rule | $24.0179$ at 1 d.p. | $24.0179$ at 2 d.p. |
| :--- | :--- | :--- | :--- |
| **Truncating** | chop at the stated digit, ignore the rest | $24.0$ | $24.01$ |
| **Rounding** | look at the digit just after the stated one: 5 or more → bump up; 4 or less → leave | $24.0$ (next digit 1) | $24.02$ (next digit 7) |

Significant figures on decimals follow the Place Value lesson's rules — count digits from the **first non-zero digit**, including any zeros that come after it: $0.0496$ (2 s.f.) $= 0.050$: first non-zero digit is 4, second is 9, and the *next* digit is 6, so the 9 bumps the 4 up to 5. The zero written after the 5 is *part of the statement* — it holds the decimal places.

> **Exam habit:** the phrase **"correct to ..."** always means **round** (unless the question says truncate). "Give your answer to 2 decimal places" for $13.1271$ means $13.13$, because the third decimal digit is 7 (5 or more, round up).

---

## 8. Fifteen Fully Worked Examples (Mixed Angles)

### Example 1 — Column addition, then round (Mock P1 Q1)
**Find the value of $124.3 + 0.275 + 74.06$, correct to one decimal place.** *(Official key: A)*

Pad and add: $124.300 + 0.275 + 74.060 = 198.635$ (see the column in Section 3).
Round to 1 d.p.: the digit after the first decimal place is 3 (less than 5), so $198.635 \to 198.6$.
**Answer: $198.6$ — matches option A.** *(Bank: `Q_f41cbf8aff88`.)*

### Example 2 — Column subtraction with padding
**Evaluate $15.07 - 3.285$.** *(Bank: `Q_156ff5549611`.)*

Pad: $15.070 - 3.285$. Column by column: $0 - 5$ → borrow, making $10-5=5$; $6-8$ → borrow again; the running result is $11.785$.
**Answer: $11.785$.**

### Example 3 — Decimal places decide the point (Mock P2 Q2(a)(ii))
**Find $0.893 \times 14.7$, correct to 4 decimal places.**

Points first: $893 \times 147 = 131271$. Place counters: $3 + 1 = 4$ decimal places → $13.1271$.
"Correct to 4 d.p." is satisfied exactly (the 5th digit does not exist).
**Answer: $13.1271$.** *(Bank: `Q_548f6faaa69d` — answer part ii.)*

### Example 4 — Multi-tier pay with decimals (Mock P2 Q3(a))
**Mark earns GH₵ 8.25 per hour for 8 hours and overtime at $1\frac{1}{2}$ times his regular rate for 4 hours. How much does he earn altogether in a day?**

Regular pay: $8.25 \times 8 = 66.00$.
Overtime rate: $1.5 \times 8.25 = 12.375$ (multiply without the point: $15 \times 825 = 12375$, then 3 decimal places).
Overtime pay: $12.375 \times 4 = 49.50$.
Total: $66.00 + 49.50 = 115.50$.
**Answer: GH₵ 115.50 for the day.** *(Money questions are the natural home of decimal arithmetic; this exact question's rate-and-wage treatment lives in the Ratios & Financial lesson.)*

### Example 5 — Powers of 10 (authentic 2026 mock Aug)
**Find the product of 24.5 and 100.** *(Bank: `Q_5e794c261f96`.)*

Multiplying by 100 moves the point two places right: $24.5 \times 100 = 2450$.
**Answer: $2450$ (option B).**

### Example 6 — Tiny decimals, big care (Mock P1 Q14)
**Evaluate $(0.07 \times 0.02) \div 14$.** *(Official key: C)*

Step 1: $0.07 \times 0.02$. Points: $7 \times 2 = 14$, place $2 + 2 = 4$ → $0.0014$.
Step 2: $0.0014 \div 14 = 0.0001$ (because $14 \times 0.0001 = 0.0014$).
**Answer: $0.0001$ — option C.** *(Bank: `Q_9ececd81b447`.)*
*Spiral view (Day 3 + Day 1): $0.07 \times 0.02 = 7 \times 10^{-2} \times 2 \times 10^{-2} = 1.4 \times 10^{-4} = 0.0001$ — the same number in standard form's clothes.*

### Example 7 — Weighing by multiplication (Mock P1 Q32)
**A fly weighs 0.1 kg. How much would 112 flies weigh combined?** *(Official key: C)*

$112 \times 0.1 = 11.2$ (multiply $112$ by 1, then shift the point one place left).
**Answer: $11.2$ kg — option C.** *(Bank: `Q_d92f8defe34e`.)*

### Example 8 — Long division ladder
**Work out $122.5 \div 5$ completely.**

The four steps in the table of Section 5.1 give quotient $24.5$.
**Answer: $24.5$.** Check: $24.5 \times 5 = 122.5$ — correct.

### Example 9 — Make the divisor whole
**Evaluate $8.58 \div 2.6$.**

Shift one place: $85.8 \div 26$. Long division: $26 \times 3 = 78$; carry the 7.8 over the point → $26 \times 0.3 = 7.8$ no remainder. Quotient: $3.3$.
**Answer: $3.3$.** Check: $2.6 \times 3.3 = 8.58$ — correct.

### Example 10 — Spotting a recurring decimal
**Write $2 \div 3$ as a decimal and state whether it terminates or recurs; give it correct to 2 d.p.**

$20 \div 3 = 6$ r 2; $20 \div 3 = 6$ r 2 — the same remainder returns forever → $0.666\ldots$, a **recurring** decimal.
Correct to 2 d.p.: the third digit 6 (5 or more) rounds the second digit up → $0.67$.
**Answer: $0.6$ recurring, which is $0.67$ (2 d.p.).**

### Example 11 — Truncating vs rounding
**Work out $24.0179$ (a) truncated to 2 d.p. (b) rounded to 2 d.p. (c) rounded to 3 s.f.**

(a) Chop: $24.01$.
(b) Third decimal digit is 7 → bump: $24.02$.
(c) First three significant digits: $2, 4, 0$ with next digit 1 (less than 5, leave) → $24.0$ — the written zero is meaningful (it is the third significant figure).
**Answers: (a) $24.01$  (b) $24.02$  (c) $24.0$.**

### Example 12 — Significant figures near the point
**Express $0.0496$ correct to 2 significant figures.**

First non-zero digit is 4; second is 9; next digit is 6 → round the 9 up, carrying into the 4: $0.050$.
**Answer: $0.050$** (2 s.f. — the final zero holds the place).

### Example 13 — Time as a multi-step operation (Mock P2 Q5(b))
**Asamoah left Takoradi at 11:13 am and got to Tema at 3:08 pm. How long did the journey take?**

Work from 11:13 forward:
11:13 → 12:00 = 47 minutes; 12:00 → 3:00 pm = 3 hours; 3:00 → 3:08 pm = 8 minutes.
Total: $47 + 180 + 8 = 235$ minutes $= 3$ h $55$ min (since $235 = 3 \times 60 + 55$).
**Answer: 3 hours 55 minutes.** *(Bank: `Q_61656d556769` — tagged B9.1.2.2.2: word problems with the four operations.)*

### Example 14 — The jacket problem (from the B9.1.2.2.2 indicator itself)
**The price of a jacket is three times that of a shirt. A jacket costs GH₵ 560.65. Mr Mensa bought two jackets and four shirts for his twin sons. Calculate the total amount he paid, correct to (a) two decimal places (b) three significant figures.**

Shirt price: $560.65 \div 3 = 186.8833\ldots$ (3 shares: $186.88\ldots$ each — this division genuinely recurs, precision control is not decoration here).
Two jackets: $2 \times 560.65 = 1121.30$.
Four shirts: $4 \times 186.8833\ldots = 747.5333\ldots$
Total: $1121.30 + 747.5333\ldots = 1868.8333\ldots$
(a) 2 d.p.: the third decimal digit is 3 → leave → **GH₵ 1868.83**.
(b) 3 s.f.: digits $1, 8, 6$ with next digit 8 → bump → **GH₵ 1870** (the trailing zeros are placeholders, not counted).

### Example 15 — Decimals meeting algebra (authentic BECE 2017)
**Write the total cost, in cedis, of $x$ shirts at GH₵ 5.00 each and $y$ shirts at GH₵ 1.50 each, fully simplified.** *(Bank: `Q_297c6f3b7796`, official key: $5x + 1.5y$.)*

$x$ shirts at GH₵ 5.00 cost $5x$; $y$ shirts at GH₵ 1.50 cost $1.5y$; total is $5x + 1.5y$. The decimals live inside the terms; the simplification is ordinary collecting of like terms.
**Answer: $5x + 1.5y$.** *(This is the bridge: decimals feed the Algebraic Expressions lesson.)*

---

## 9. Exercise Sets (5 × 5, No MCQ)

**Instructions:** write full workings for every question. Show column layouts for additions/subtractions, state decimal-place counts for multiplication, and state the rounding rule you applied wherever an answer is given "correct to ...". No calculators.

### Exercise 1 — Column arithmetic and rounding

1. $86.7 + 259.08 + 12.315$, correct to 1 d.p.
2. $120 - 73.485$
3. A customer's bill is GH₵ 214.35 for cement and GH₵ 326.80 for sand. She pays with GH₵ 750.00. Find her change.
4. $5.4 + 0.68 + 0.007 + 9.993$
5. **Spiral review (Day 1):** Write the exact unrounded sum in question 1 in standard form.

### Exercise 2 — Multiplication

1. $23.51 \times 4$
2. $6.04 \times 0.52$ (state the decimal-place count you used)
3. **Spiral review (Day 3 + Day 1):** Evaluate $0.003 \times 0.02$ and express the answer in standard form.
4. A crate holds 24 bottles and each bottle contains 0.35 litres. How many litres does a full crate contain?
5. $0.285 \times 1000$

### Exercise 3 — Division

1. $96.06 \div 6$
2. $8.58 \div 2.6$
3. $3 \div 7$: state the six-digit recurring block of digits, then give the value correct to 2 d.p.
4. $2.1 \div 0.07$
5. A merchant shares 12.6 kg of rice equally into 8 bags. Find the weight of rice in one bag (exact decimal).

### Exercise 4 — Precision control

1. Truncate $24.0179$ to 1 d.p. and to 2 d.p.
2. Round the true product of Exercise 2, question 2 — that is, $0.893 \times 14.7 = 13.1271$ — to 2 d.p.
3. Round $0.0749$ to (a) 1 s.f. (b) 2 s.f.
4. A decimal $46.9839$ is (a) truncated to 2 d.p. (b) rounded to 2 d.p. (c) rounded to 3 s.f. Give all three answers.
5. **Spiral review (Day 3):** Write the answer to Example 6, $0.0001$, in standard form.

### Exercise 5 — Multi-step word problems

1. Awurama measures three flights of timber: 26.5 m, 74.98 m and 152.405 m. Find the total length, correct to 2 d.p.
2. A bus leaves Kumasi at 09:47 and arrives in Sunyani at 13:05. How long is the journey? Give the answer in hours and minutes.
3. A shop had 87.5 m of wire. It cut and sold 39.68 m in week one and 21.355 m in week two. How much wire is left?
4. Ama buys 3 exercise books at GH₵ 4.75 each and 2 pens at GH₵ 3.10 each. She pays with GH₵ 25.00. Find her change.
5. Write the total cost, in cedis, of $x$ shirts at GH₵ 5.00 each and $y$ shirts at GH₵ 1.50 each, fully simplified, and state what the expression gives when $x = 4$ and $y = 6$.

---

## 10. Full Worked Solutions

### Exercise 1

**1.** Pad and column-add: $86.700 + 259.080 + 12.315 = 358.095$.
Correct to 1 d.p.: next digit is 9 (5 or more) → $358.095 \to \mathbf{358.1}$.

**2.** Pad: $120.000 - 73.485$. Column subtraction with borrowing gives $\mathbf{46.515}$.
Check: $73.485 + 46.515 = 120.000$ — correct.

**3.** Total spent: $214.35 + 326.80 = 541.15$.
Change: $750.00 - 541.15 = \mathbf{GH\text{₵}\,208.85}$.

**4.** Pad equally: $5.400 + 0.680 + 0.007 + 9.993 = \mathbf{16.080}$ (trailing zero may be dropped: $16.08$).

**5.** Exact sum was $358.095$: in standard form $= \mathbf{3.58095 \times 10^2}$.

### Exercise 2

**1.** $2351 \times 4 = 9404$; $23.51$ has 2 decimal places → $\mathbf{94.04}$.

**2.** $604 \times 52 = 31408$; decimal places: $2 + 2 = 4$ → $\mathbf{3.1408}$.

**3.** $3 \times 2 = 6$; decimal places $3 + 2 = 5$ → $0.00006$.
Standard form: $0.00006 = \mathbf{6 \times 10^{-5}}$.

**4.** $24 \times 0.35$: $24 \times 35 = 840$; decimal places $0 + 2 = 2$ → $\mathbf{8.40}$ litres (drop the trailing zero: $8.4$ litres).

**5.** $0.285 \times 1000$: the point moves three places right → $\mathbf{285}$.

### Exercise 3

**1.** $96.06 \div 6$: pad to $96.060$; long division $96 \div 6 = 16$; the point travels through; the remaining $0.060 \div 6 = 0.01$ → $\mathbf{16.01}$. Check: $6 \times 16.01 = 96.06$ — correct.

**2.** Shift one place: $85.8 \div 26$. Long division: $26 \times 3 = 78$, remainder $7.8$; point travels; $78 \div 26 = 3$, so $0.3$ fits exactly → $\mathbf{3.3}$. Check: $2.6 \times 3.3 = 8.58$ — correct.

**3.** $3.0 \div 7$: remainders cycle $2 \to 6 \to 4 \to 5 \to 1 \to 3 \to 2\ldots$ producing digits $0.428571\,428571\ldots$
Recurring block: $\mathbf{428571}$.
2 d.p.: third digit 8 (5 or more) → $0.42 \to \mathbf{0.43}$.

**4.** Divisor 0.07 → shift two places: $210 \div 7 = \mathbf{30}$. Check: $0.07 \times 30 = 2.1$ — correct.

**5.** $12.6 \div 8$: long division gives $1.575$ exactly ($8 \times 1.575 = 12.6$).
Each bag holds $\mathbf{1.575}$ kg.

### Exercise 4

**1.** Truncate (chop, never round): 1 d.p. → $\mathbf{24.0}$; 2 d.p. → $\mathbf{24.01}$. (Rounding would give $24.0$ and $24.02$ — different at 2 d.p.!)

**2.** $13.1271$ rounded to 2 d.p.: third decimal digit is 7 (bump) → $\mathbf{13.13}$.

**3.** (a) 1 s.f.: first significant digit 7; next digit 4 (leave) → $\mathbf{0.07}$.
(b) 2 s.f.: digits 7, 4; next digit 9 (bump) → $\mathbf{0.075}$.

**4.** (a) Truncating: chop after hundredths → $\mathbf{46.98}$.
(b) Rounding: next digit is 3 (leave) → $\mathbf{46.98}$.
(c) 3 s.f.: digits $4, 6, 9$ with next digit 8 → the 9 bumps past 10 and carries into the 6: $46.9839 \to \mathbf{47.0}$ (the 0 holds the third significant figure).

**5.** $0.0001 = \mathbf{1 \times 10^{-4}}$.

### Exercise 5

**1.** $26.5 + 74.98 + 152.405$: pad → $26.500 + 74.980 + 152.405 = 253.885$.
2 d.p.: third decimal digit 5 (bump) → $\mathbf{253.89}$ m.

**2.** 09:47 → 10:00 = 13 min; 10:00 → 13:00 = 3 h; 13:00 → 13:05 = 5 min. Total $13 + 180 + 5 = 198$ min.
$198 = 3 \times 60 + 18$ → $\mathbf{3\ hours\ 18\ minutes}$.

**3.** Sold: $39.68 + 21.355 = 61.035$ m.
Left: $87.5 - 61.035 = 87.500 - 61.035 = \mathbf{26.465}$ m.

**4.** Books: $3 \times 4.75 = 14.25$; pens: $2 \times 3.10 = 6.20$.
Total: $14.25 + 6.20 = 20.45$; change: $25.00 - 20.45 = \mathbf{GH\text{₵}\,4.55}$.

**5.** Cost of $x$ shirts: $5x$; cost of $y$ shirts: $1.5y$; total $\mathbf{5x + 1.5y}$.
When $x = 4, y = 6$: $5(4) + 1.5(6) = 20 + 9 = \mathbf{27}$ cedis.

---

## 11. Bank and Mock Links

| Item | ID | Source | Where used |
| :--- | :--- | :--- | :--- |
| $124.3 + 0.275 + 74.06$, 1 d.p. (Mock P1 Q1) | `Q_f41cbf8aff88` | user mock 0201-026/27 | Example 1 |
| $15.07 - 3.285$ | `Q_156ff5549611` | bank lesson exercises | Exercise ref |
| $0.893 \times 14.7$, 4 d.p. (Mock P2 Q2(a)(ii)) | `Q_548f6faaa69d` | user mock 0201-026/27 | Example 3 |
| Mark's day pay, GH₵ 8.25 (Mock P2 Q3(a)) | `Q_83b389d16cd2`* see note | user mock 0201-026/27 | Example 4 |
| $24.5 \times 100$ (authentic 2026 mock) | `Q_5e794c261f96` | Aug-2026 mock paper | Example 5 |
| $(0.07 \times 0.02) \div 14$ (Mock P1 Q14) | `Q_9ececd81b447` | user mock 0201-026/27 | Example 6 |
| 112 flies at 0.1 kg (Mock P1 Q32) | `Q_d92f8defe34e` | user mock 0201-026/27 | Example 7 |
| Takoradi → Tema time (Mock P2 Q5(b)) | `Q_61656d556769` | user mock 0201-026/27 | Example 13 |
| Total cost of $x$ shirts (BECE 2017) | `Q_297c6f3b7796` | BECE 2017 past questions | Exercise 5, Q5 |

*Note: Example 4's mock item is tagged B9.1.4.1.2 (rates/wages) — its full financial treatment belongs to the Ratios & Financial lesson; it is kept here as a decimal-arithmetic model.

---

## 12. Lesson Summary (Cheat Sheet)

| Operation | The one rule to carry |
| :--- | :--- |
| Add / subtract | Line the points up; pad with trailing zeros (free!) |
| Multiply | Multiply point-free, then give the answer $d_1 + d_2$ decimal places |
| Divide | Make the divisor whole by shifting both numbers equally |
| Recurring decimals | Same remainder returning = forever pattern; round at the asked d.p. |
| "Correct to n d.p." | Round — look at digit $n+1$: 5 or more bumps |
| "Truncate" | Chop at digit $n$, ignore the rest |

**Money time-saver:** pad every GH₵ figure to two decimal places before any operation — GH₵ 8.25 already is; GH₵ 115.5 → GH₵ 115.50.

---

*Lesson prepared under `Grade9-Maths/Rules.md` — plain English, British notation, full workings for every question. Quota override in force for this round: 5 sections × 5 questions.*
