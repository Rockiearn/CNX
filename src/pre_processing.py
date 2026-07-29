import pandas as pd
import os


file_list = ["May", "June", "July"]


def file_charging(files):

    name = f"{files}.csv"
    path = os.path.join("data", name)
    df = pd.read_csv(path)

    date_cols = [col for col in df.columns if "/" in col]

    df_long = pd.melt(
        df,
        id_vars=["WD EID", "Emp Name"],
        value_vars=date_cols,
        var_name="temp_col",
        value_name="val",
    )

    df_long[["Date", "Metric"]] = df_long["temp_col"].str.rsplit(
        "_", n=1, expand=True
    )
    df_long = df_long.drop(columns=["temp_col"])

    df_final = df_long.pivot_table(
        index=["WD EID", "Emp Name", "Date"],
        columns="Metric",
        values="val"
    ).reset_index()


    df_final = df_final.reindex(columns=["WD EID", "Emp Name", "Date", "Answered", "AHT"])

    return df_final

def file_combiner(input):
    file_col = []
    run = input

    for i in run:
        dataframe = file_charging(i)
        file_col.append(dataframe)
    df = pd.concat(file_col, ignore_index=True)

    return df

if __name__ == "__main__":

    df = file_combiner(file_list)
    df.to_csv("data/Cleaned_sheet(pivot_table).csv", index=False)