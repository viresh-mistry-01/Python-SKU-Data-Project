import os
import pandas as pd
import numpy as np
import matplotlib as mb
import matplotlib.pyplot as plt


#Settings to view tables in full
pd.set_option('display.max_columns', None)
pd.set_option('display.width',1000)
pd.set_option('display.max_rows', 100)

#Loading the data into dataframe
username = os.getlogin()
path = fr"C:\Users\{username}\Downloads\VM_SKU_Data_Project.csv"
path2 = path.replace(os.sep,'/')
sku_table = pd.read_csv(path2, sep=',')


#Modifying and inserting columns

sku_table = sku_table.assign(Margin_pct = sku_table['Margin']/sku_table['Revenue']) #Margin % column
sku_table.rename(columns={'Cost of Sales':'Cost_of_Sales','Qty':'Quantity','Price per unit':'Price_per_Unit'}, inplace=True) #Renaming columns
sku_table['Revenue']=np.where(sku_table['Revenue'] < 0,0,sku_table['Revenue'])

#Pivot of yearly Revenue and Margin by Product_Range
sku_pivot = sku_table.pivot_table(values=['Revenue','Margin'],index='Product_Range',columns='FY', aggfunc='sum', sort=False)
sku_pivot = sku_pivot.sort_values(by=("Revenue",2023),ascending=False)
print('SKU_Pivot')
sku_pivot

#Table grouping by Product Range and FY ordered by 2023 revenue descending
sku_plot_tab = sku_table.groupby(by=['Product_Range','FY'],sort=True).agg(TotalRev=('Revenue','sum')).unstack()
sku_plot_tab.sort_values(by=('TotalRev',2023), ascending=False,inplace=True)

#Plot showing the total revenue by product range each year for top 10 revenue ranges in 2023
sku_plot_top_ten = sku_plot_tab.head(10)
sku_plot_top_ten.plot(kind='bar', stacked=True, title = 'Total revenue by product range by year')

#Layered Pie chart showing proportion of total yearly revenue each range contributes to

years = sku_table['FY'].unique()

fig, ax = plt.subplots(figsize=(8, 8))
width = 0.25; radius = 1.0
cmap = plt.cm.tab20

'mapping each range to a colour'
colour_map = {
    idx: cmap(i % cmap.N)
    for i, idx in enumerate(sku_plot_tab.index)
             }

wedges = None

'plot for each year and excluding any values equal to 0'
for i, year in enumerate(reversed(years)):
   values = sku_plot_tab[('TotalRev', year)]
   values = values[values != 0]

   ring_colours = [colour_map[idx] for idx in values.index]

   w, _ = ax.pie(values, colors=ring_colours, radius=radius - i * width,
   wedgeprops=dict(width=width),startangle=90)

   # Save the wedges from the outer ring
   if i == 0:
        wedges = w
        legend_labels = values.index.astype(str)


ax.legend(wedges, sku_plot_tab.index.astype(str),
    title="Product_Range",
    loc="center left",
    bbox_to_anchor=(1.05, 0.5)
        )

ax.set(aspect="equal")
plt.title("Proportion of Total Revenue by Year")
plt.show()

#boxplot showing 
sku_plot_tab['TotalRev'].boxplot()
plt.ylabel("Revenue")
plt.xlabel("Year")
plt.title("Revenue Distribution by Year")
plt.show()

# Slope chart showing yearly changes in revenue per range
log_rev = sku_plot_tab.apply(np.log10)
fig, ax = plt.subplots(figsize=(10, 8))

for ranges in log_rev.index:
    revenues = log_rev.loc[ranges, 'TotalRev']

    ax.plot(years, revenues.values, marker='o', linewidth=2, alpha=0.8)

ax.set_xticks(years)
ax.set_xlabel("Year")
ax.set_ylabel("Revenue")
ax.set_title("Revenue by Company")
plt.show()

log_rev = sku_plot_tab.apply(np.log10)
