import pandas as pd
### The dataset was taken utilizing beautiful soup and parsing web pages from an italian recipe website called "GialloZafferano".
### On total there are almost 6000 recipes, ranging from starters to dessert.
data = pd.read_csv('gz_dataset.csv', sep='|')
data = data.rename(columns={'link':'preparation'})
data = data.reset_index()

search = input("""What ingredients do you have?

Separate them with a space [Example: egg sugar]
""")
def search_split(search):
    lower_search = search.lower()
    x = lower_search.split()
    return x
result = search_split(search)
result

for ext in result:
    for i in range(len(data.index)):
        if all(ext in str(data.ingredients[i]).lower() for ext in result):
            print(data.iloc[i])
