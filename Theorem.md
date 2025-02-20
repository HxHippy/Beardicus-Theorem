# Dr. Beardicus' Theorem

## Formal Definition

For any given anime profile picture, let:
- $A \in [0,10]$ denote the cuteness level
- $B \in [0,10]$ denote the beard prominence
- $P \in [0,1]$ denote the probability of being a medieval fantasy dwarf

## Core Equations

### Beard Prominence Function
The beard prominence $B$ is given by:

$B = \frac{A^2}{10}$

This quadratic relationship implies that beard growth accelerates with increasing cuteness levels.

### Dwarf Probability Function
The probability $P$ of being a medieval fantasy dwarf is given by:

$P = \frac{1}{1 + e^{-(A - 8)}}$

This sigmoid function creates a sharp transition around $A = 8$, representing the critical threshold for dwarf transformation.

## Key Properties

1. **Domain Constraints**
   - $A \in [0,10]$ (Cuteness Level)
   - $B \in [0,10]$ (Beard Prominence)
   - $P \in [0,1]$ (Dwarf Probability)

2. **Monotonicity**
   - Both $B$ and $P$ are strictly increasing functions of $A$
   - $\frac{dB}{dA} = \frac{2A}{10} > 0$ for $A > 0$
   - $\frac{dP}{dA} = \frac{e^{-(A-8)}}{(1 + e^{-(A-8)})^2} > 0$

3. **Critical Points**
   - $A = 8$ is the inflection point for dwarf probability
   - $P(8) = 0.5$ (50% chance of being a dwarf)
   - $B(8) = 6.4$ (substantial beard at the critical point)

## Notable Values

| Cuteness ($A$) | Beard Prominence ($B$) | Dwarf Probability ($P$) |
|----------------|------------------------|------------------------|
| 0 | 0.0 | 0.000 |
| 5 | 2.5 | 0.047 |
| 8 | 6.4 | 0.500 |
| 9 | 8.1 | 0.731 |
| 10 | 10.0 | 0.881 |

## Implementation Notes

1. **Numerical Stability**
   - For extreme values of $A$, consider using log-space calculations for the sigmoid function
   - Ensure proper handling of floating-point arithmetic

2. **Visualization**
   - Plot $B$ vs $A$ to show quadratic growth
   - Plot $P$ vs $A$ to show sigmoid transition
   - Consider combined plots with dual y-axes

## Applications

1. **Profile Picture Analysis**
   - Automated cuteness assessment
   - Beard length prediction
   - Dwarf risk assessment

2. **Community Management**
   - Early dwarf detection systems
   - Beard growth monitoring
   - Convention planning (beard trimmer availability)

## References

1. Dr. Beardicus, "On the Correlation Between Anime Avatars and Facial Hair Growth Patterns," *Journal of Digital Anthropology*, 2025
2. "Proceedings of the Grand Symposium of Digital Discoveries," 2025
3. "The Dwarf Transformation Index: A New Metric for Online Identity Studies," *Internet Culture Quarterly*, 2025