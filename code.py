import pandas as pd
### The dataset was taken utilizing beautiful soup and parsing web pages from an italian cooking website called "GialloZafferano".
### On total there are almost 6000 recipes, ranging from starters to dessert.
data = pd.read_csv('gz_dataset.csv', sep='|')
data = data.rename(columns={'link':'preparation'})
data = data.reset_index()

### This function just makes the user input "readable" by the next lines of code.
### The idea is to make everything lowercase so it's easier to find all the recipes.
search = input("""What ingredients do you have?

Separate them with a space [Example: egg sugar]
""")
def search_split(search):
    lower_search = search.lower()
    x = lower_search.split()
    return x
result = search_split(search)
result

### In the future this loop will be more intuitive.
### I want to make it so that if >n ingredients are in a recipe they get printed.
### This way if I have chicken and tuna, for example, the research does not give no output.

for ext in result:
    for i in range(len(data.index)):
        if all(ext in str(data.ingredients[i]).lower() for ext in result):
            print(data.iloc[i])
