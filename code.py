import pandas as pd
data = pd.read_csv('gz_dataset.csv', sep='|')
data = data.rename(columns={'link':'preparation'})
data.dropna(inplace = True)

search = input("""What ingredients do you have?

Separate them with a space [Example: egg sugar]
""")
def search_split(search):
    lower_search = search.lower()
    x = lower_search.split()
    return x
result = search_split(search)

