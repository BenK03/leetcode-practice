# Write your MySQL query statement below
# Outer Query
SELECT (
    # Sub query (runs first)
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1 # return one row and skip index 0
) AS SecondHighestSalary

# time complexity O(nlogn)
