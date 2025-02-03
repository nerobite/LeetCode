import pandas as pd

# Создание датафрейма для таблицы Person
person_data = {
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob']
}
person_df = pd.DataFrame(person_data)

# Создание датафрейма для таблицы Address
address_data = {
    'addressId': [1, 2],
    'personId': [2, 3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
}
address_df = pd.DataFrame(address_data)

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(person, address, how='left')
    return df[['firstName', 'lastName', 'city', 'state']]