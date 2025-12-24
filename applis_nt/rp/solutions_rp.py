# %%
# import copy
import polars as pl
import plotnine as p9
import geopandas as gpd
# import seaborn as sns
# import fastexcel
import solutions
import matplotlib.pyplot as plt

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
        if df[0, colname] is not None:
            if colname[:11] == '__UNNAMED__':
                temp_colnames_list[index] = temp_colnames_list[index-1].split("_")[0] + "__" + df[0, colname]
            else:
                temp_colnames_list[index] = temp_colnames_list[index] + "__" + df[0, colname]
        else:
            temp_colnames_list[index] = temp_colnames_list[index-1].split("_")[0] + "__00"
    temp_colnames_list[0]="dep_code"
    temp_colnames_list[1]="dep"
    df_new = df.rename(dict(zip(df.columns, temp_colnames_list)))

    # Reshaping data
    df_new = (
        df_new.drop_nulls(pl.col('dep_code'))
            .unpivot(index=['dep_code', 'dep'], value_name="population")
            .with_columns(
                variablelist=pl.col.variable.str.split('__')
            )
            .with_columns(
                genre=pl.col.variablelist.list.get(0, null_on_oob=True), 
                age=pl.col.variablelist.list.get(1, null_on_oob=True), 
                population=pl.col.population.cast(pl.Int64), 
                annee=pl.lit(year).cast(pl.Int64)
            )
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


df = reshape_data(load_data())

# %%
def plot_population_by_gender_per_department(data, department_code):
    
    df_plot = (data\
        .filter(
            pl.col.dep_code.is_in([department_code]), 
            pl.col.genre!="Ensemble", 
            pl.col.age=="Total"
            )
        .with_columns(pl.col.population/1e6)
    )

    plot = (
        p9.ggplot(df_plot,        
            p9.aes(x="annee", y="population", group="genre", colour="genre")) 
        + p9.geom_line(size=1)
        + p9.theme_matplotlib()
        + p9.labs(
            title=f"Évolution de la population entre {df_plot.min()[0, "annee"]} et {df_plot.max()[0, "annee"]} dans le {df_plot.min()[0, "dep_code"]} ({df_plot.min()[0, "dep"]})", 
            x="Année", 
            y="Population (M)"
        )
    )

    return plot

# %%
plot_population_by_gender_per_department(df, '31')

# %%
solutions.plot_population_by_gender_per_department(df.to_pandas(), "31")

# %%

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(15,6))

solutions.plot_age_pyramid(df.to_pandas(), 1975, ax=ax1)
solutions.plot_age_pyramid(df.to_pandas(), 2022, ax=ax2)
# %%
