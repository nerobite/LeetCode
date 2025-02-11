"""
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.
Return the result table in any order.
The result format is in the following example.
Example 1:
Input:
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
Output:
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Explanation: a@b.com is repeated two times.
"""
import pandas as pd

data = {'id':[1,2,3], 'email':['a@b.com', 'c@d.com', 'a@b.com']}
person = pd.DataFrame(data)
person = person.set_index('id')

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    email = person['email'].value_counts().loc[person['email'].value_counts() > 1].reset_index()
    return email[['email']]

