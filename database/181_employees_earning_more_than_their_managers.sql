# Write your MySQL query statement below
SELECT name as Employee From Employee WHERE salary > (
    SELECT salary FROM Employee AS Manager 
    WHERE Manager.id=Employee.managerId
);

# time complexity O(n)