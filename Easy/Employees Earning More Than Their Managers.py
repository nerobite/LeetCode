"""
Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
Write a solution to find the employees who earn more than their managers.
Return the result table in any order.
The result format is in the following example.
Example 1:
Input:
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output:
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.
"""
import pandas as pd

data = {'id':[1,2,3,4], 'name':['Joe', 'Henry', 'Sam', 'Max'], 'salary': [70000, 80000, 60000, 90000], 'managerId': [3, 4, None, None]}
df = pd.DataFrame(data)

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merge_df = employee.merge(employee, how='inner', left_on='managerId', right_on='id')
    name= merge_df.loc[merge_df['salary_x'] > merge_df['salary_y']]
    return pd.DataFrame({"Employee": name["name_x"]})