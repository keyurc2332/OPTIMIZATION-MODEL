# Step 1: Install PuLP (if not installed)
!pip install pulp

# Step 2: Import PuLP library
from pulp import LpMaximize, LpProblem, LpVariable

# Step 3: Problem Setup
## Problem Data:
# - Product A: Profit per unit = $40, Manufacturing time per unit = 2 hours.
# - Product B: Profit per unit = $30, Manufacturing time per unit = 3 hours.
# - Total Available Time: 120 hours.

# Step 4: Define the optimization problem
model = LpProblem(name="profit-maximization", sense=LpMaximize)

# Step 5: Define the decision variables
x = LpVariable("x", lowBound=0, cat="Continuous")  # Number of Product A
y = LpVariable("y", lowBound=0, cat="Continuous")  # Number of Product B

# Step 6: Define the objective function
model += 40 * x + 30 * y, "Profit"

# Step 7: Define the constraint (production time limit)
model += 2 * x + 3 * y <= 120, "Time Constraint"

# Step 8: Solve the problem
model.solve()

# Step 9: Display the results
print(f"Status: {model.status}")  # Display the status of the solution
print(f"Optimal number of Product A to produce: {x.varValue}")
print(f"Optimal number of Product B to produce: {y.varValue}")
print(f"Maximum Profit: ${model.objective.value()}")

# Step 10: Insights and Interpretation
print("\n### Insights and Interpretation:")
print(f"The optimal production strategy is:")
print(f"- Produce {x.varValue} units of Product A.")
print(f"- Produce {y.varValue} units of Product B.")
print(f"This maximizes the total profit to ${model.objective.value()}.")
print("\nThis solution suggests that, given the time constraint, focusing entirely on Product A is the best choice.")
print("This result indicates that Product A provides a higher return on investment per manufacturing hour compared to Product B.")
print("\nBusiness Implications:")
print("1. The company should consider reallocating resources to focus more on Product A.")
print("2. If the company wishes to produce both products, they may need to increase the available production time.")
