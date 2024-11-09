import pandas as pd

data = {
    'rocket': [
        'Falcon 1',
        'Falcon 9',
        'Falcon Heavy'
    ],
    'launches': [5, 100, 3]
}

df = pd.DataFrame(data)

# print data
# print(df)
# print(df['rocket'])

# filterin row
falcon9 = df[df['rocket'] == 'Falcon 9']
# print(falcon9)

# add new columns
df['success_rate'] = [0.4, 0.98, 1.0]
print(df)

# adding missed rockets

new_data = {
    'rocket': [
        'Falcon 2',
        'Falcon 3',
        'Falcon 4',
        'Falcon 5',
        'Falcon 6',
        'Falcon 7',
        'Falcon 8'
    ],
    'launches': [50, 45, 78, 9, 33, 900, 21],
    'success_rate': [0.76, 0.89, 0.99, 1.0, 0.33, 0.85, 0.10]
}
df2 = pd.DataFrame(new_data)

df = pd.concat([df, df2], ignore_index=True)

print(df)