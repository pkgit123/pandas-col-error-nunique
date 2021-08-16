import pandas as pd

print(f"Rows and columns: {df.shape}  \n")
print(f"Null values per column: \n{df.isna().sum()}  \n")

# check which columns error when counting number of uniques
ls_cols_nunique = []
ls_cols_error_nunique = []
for each_col in df.columns:
    try:
        df[each_col].nunique()
        ls_cols_nunique.append(each_col)
    except:
        ls_cols_error_nunique.append(each_col)

print(f"Unique values per column: \n{df[ls_cols_nunique].nunique()}  \n")
print(f"Columns error nunique: \n{ls_cols_error_nunique}  \n")
