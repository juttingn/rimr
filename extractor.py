import pandas as pd
pd.options.display.max_rows = 10

lx = pd.read_csv('data/lexique.csv', sep='\t')

for x in lx.loc[lx['4_cgram'] == "NOM", :]:
    print(lx["1_ortho"])

print(x)


