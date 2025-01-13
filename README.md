# OPTIMIZATION-MODEL

**Company:** CODTECH IT SOLUTIONS PVT. LTD.

**Name:** KEYUR AMIT CHAUHAN

**Intern ID:** CT08EOQ

**Domain:** DATA SCIENCE

**Duration:** December 17th, 2024 - January 17th, 2025 (4 weeks)

**Mentor:** Neela Santhosh Kumar,HR & Academic Head

This task involves solving a business optimization problem using Linear Programming (LP) and the Python library PuLP. The objective is to maximize the profit of a company that manufactures two products, Product A and Product B, within a limited production time constraint.

Problem Setup:
The company earns a profit of $40 per unit of Product A and $30 per unit of Product B. Each unit of Product A requires 2 hours of manufacturing time, while Product B requires 3 hours. With a total of 120 hours available, the goal is to determine the optimal number of units of each product to produce to maximize profit.

Optimization Model:
Decision Variables:

x: Number of Product A units to produce.
y: Number of Product B units to produce.
Objective Function:
Maximize profit: 
𝑃
𝑟
𝑜
𝑓
𝑖
𝑡
=
40
𝑥
+
30
𝑦
Profit=40x+30y.

Constraints:

Total production time: 
2
𝑥
+
3
𝑦
≤
120
2x+3y≤120.
Non-negativity: 
𝑥
≥
0
,
𝑦
≥
0
x≥0,y≥0.
Solution:
Using PuLP, the optimization model was implemented, solved, and analyzed. The results are as follows:

Optimal number of Product A to produce: 60 units.
Optimal number of Product B to produce: 0 units.
Maximum profit: $2400.
Insights and Business Implications:
The solution suggests that producing only Product A is the optimal strategy to maximize profit, given the time constraint. Product A provides a higher return on investment per manufacturing hour compared to Product B.

To improve overall production flexibility and profits, the company could consider:

Increasing the total production time to allow the inclusion of Product B.
Reallocating resources to focus more on manufacturing Product A.
This task demonstrates how optimization techniques can support data-driven decision-making in real-world business scenarios.

![image](https://github.com/user-attachments/assets/df23c486-bc91-4256-87b6-7d39a3f3314c)
