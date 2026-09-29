# SKU Data Python Project

Personal project to test my Python skills by analysing SKU data for a cabling company and creating visualisations using matplotlib

### Overview
- Goal: Analyse revenue figures to locate key drivers of growth
- Stack: Python 3.0 (Pandas, NumPy, Matplotlib), SpyderPy 3.0 environment

### Dataset
- Source: https://www.kaggle.com/datasets/vireshmistry01/sku-data/data
- Included: tiny sample only (see `data/`)

### Methods
- Loading data: rename, assign, df
- Analysing data: pivot, group by
- Plotting: matplotlib charts, for loops
- AI: usage to create loops for pie chart as well as refining code

### Results (highlights)
- Range 19 is the largest revenue producing range with it and Range 83 accounting for over 50% of revenue each year
- A number of ranges revenues' rose in the year to 2022 and subsequent drops into 2023 which can be explained by increasing copper prices as well as international conflicts reducing demand
- All ranges other than 19 and 83 produced less than £1.5m of revenue each year

### How to Run
1) Download CSV from source into Downloads folder
3) Run SKU_Data_Project.py project to view tables and results

### Structure
- `python/`: code file
- `data/`: data sample

### Challenges
- Maintaining consistent format and colours within plots
- Ensuring correct syntax was used for each function
- Updating data prior to analysis to ensure the data types were correct and values were usable for analysis
- Data was only yearly as opposed to monthly which limited the ability to look at trends

### Next
- Further analysis on margin and Price-Volume as well as cable lengths
- More variety in plot usage

### License
MIT
