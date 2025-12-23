# import copy
import polars as pl
import plotnine as p9
import geopandas as gpd
# import seaborn as sns
# import fastexcel
# import solutions

def load_data():
    data = pl.read_excel(
    'https://www.insee.fr/fr/statistiques/fichier/1893198/estim-pop-dep-sexe-aq-1975-2023.xls', 
    sheet_name=[str(i) for i in range(1975,2024,1)], 
    read_options={ "header_row": 3})

    return data


def reshape_table_by_year(df, year):
    # Merging columns to Genre__Age
    temp_colnames_list = df.columns
    for index, colname in enumerate(temp_colnames_list):
        if colname[:11] == '__UNNAMED__':
            if df[0, colname] is not None:
                temp_colnames_list[index] = temp_colnames_list[index-1].split("_")[0] + "__" + df[0, colname]
            else:
                temp_colnames_list[index] = temp_colnames_list[index-1].split("_")[0] + "__00"
    df_new = df.rename(dict(zip(df.columns, temp_colnames_list)))

    # Reshaping data
    df_new = (
        df_new.drop_nulls(pl.col('Départements__00'))
            .unpivot(index=['Départements', 'Départements__00'], value_name="population")
            .with_columns(
                variablelist=pl.col.variable.str.split('__')
            )
            .with_columns(
                genre=pl.col.variablelist.list.get(0, null_on_oob=True), 
                age=pl.col.variablelist.list.get(1, null_on_oob=True), 
                population=pl.col.population.cast(pl.Int64), 
                annee=pl.lit(year).cast(pl.Int64)
            )
            .rename({'Départements':'dep_code','Départements__00':'dep'})
            .select(['dep_code', 'dep', 'annee', 'genre', 'age', 'population'])
    )

    return df_new


def reshape_data(data):
    df = pl.DataFrame(schema=
        ['dep_code', 'dep', 'annee', 'genre', 'age', 'population']
    )
    for annee_dic, annee_df in data.items():
        df=pl.concat([df, reshape_table_by_year(annee_df, annee_dic)], strict=False, how='vertical_relaxed')

    return df


# reshape_table_by_year(load_data()['1977'], '1977')
reshape_data(load_data())
