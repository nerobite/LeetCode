"""
Table: Activity
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.
The result format is in the following example.
Example 1:
Input:
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output:
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+
Explanation:
Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33
"""
import pandas as pd

data = {'player_id':[1,1,2,3,3], 'device_id':[2,2,3,1,4],
        'event_date':['2016-03-01', '2016-03-02', '2017-06-25', '2016-03-02', '2018-07-03'],
        'games_played':[5,6,1,0,5]}
activity = pd.DataFrame(data)

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    one_entrance = activity[activity.groupby('player_id')['event_date'].rank() == 1][['player_id', 'event_date']]
    two_entrance = activity[activity.groupby('player_id')['event_date'].rank() == 2][['player_id', 'event_date']]
    df = one_entrance.merge(two_entrance, how='inner', on='player_id', suffixes=('_first', '_second'))
    df['event_date_first'] = pd.to_datetime(df['event_date_first'])
    df['event_date_second'] = pd.to_datetime(df['event_date_second'])
    next_day_user = df[df['event_date_second'] == df['event_date_first'] + pd.Timedelta(days=1)]['player_id'].count()
    total_user = len(activity['player_id'].unique())
    return pd.DataFrame({"fraction": [round(next_day_user / total_user, 2)]})