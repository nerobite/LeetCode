"""
Table: Logs
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.
Find all numbers that appear at least three times consecutively.
Return the result table in any order.
The result format is in the following example.
Example 1:
Input:
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.
"""
import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['prev1'] = logs['num'].shift(1)
    logs['prev2'] = logs['num'].shift(2)
    mask = (logs['num'] == logs['prev1']) & (logs['num'] == logs['prev2'])
    result = logs[mask]['num'].drop_duplicates()
    return pd.DataFrame({'ConsecutiveNums': result})