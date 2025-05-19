import pandas as pd

data = {
    'rocket':['Falcon 1',
              'Falcon 9',
              'Falcon Heavy'
              ],
    'Launches':[5, 100, 3],
}

df = pd.DataFrame(data)

# print(df)

# print(df['rocket'])

# more_than_five = df[df['Launches'] > 5]
# print(more_than_five)

df['success_rate'] = [0.4,0.98,1.0]
print(df)