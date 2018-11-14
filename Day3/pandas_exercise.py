import pandas as pd

if __name__ == "__main__":
    df = pd.read_table('resources/chipotle.tsv')
    print('------HEAD-------')
    print(df.head)
    # print('------SIZE-------')
    # print(df.size)
    # print('------Describe-------')
    # print(df.describe())
    # print('------Getting Specific column-------')
    # print(df['item_name'])
    
    # df = pd.read_table('resources/u.user')
    # print('------HEAD-------')
    # print(df.head)
    # print('------SIZE-------')
    # print(df.size)
    # print('------Describe-------')
    # print(df.describe())