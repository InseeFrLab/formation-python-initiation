import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import seaborn as sns


def load_data():
    data = pd.read_excel(
        "https://www.insee.fr/fr/statistiques/fichier/1893198/estim-pop-dep-sexe-aq-1975-2023.xls",
        sheet_name=None,
        header=[3, 4],
    )
    return data


def reshape_table_by_year(df, year):
    """
    This function reshapes a DataFrame by filtering and transforming it based on the year.

    Parameters:
        df (DataFrame): The input DataFrame to reshape.
        year (str): The year to filter the DataFrame by.

    Returns:
        DataFrame: The reshaped and filtered DataFrame.
    """
    # Removing NaNs and set Départements as Index
    df = df.dropna().set_index("Départements")

    # Reshaping dataframe by stacking levels and using melt function (from wide to long format)
    df = pd.melt(
        df.stack(level=0, future_stack=True).reset_index(),
        id_vars=["Départements", "level_1"],
        value_name="population",
        var_name="age",
    )

    # Renaming column
    df = df.rename(columns={"level_1": "genre"})

    # Splitting Départements column into dep_code and dep
    df[["dep_code", "dep"]] = pd.DataFrame(df["Départements"].tolist())

    # Drop Départements column
    df = df.drop(columns=["Départements"])

    # Adding a year column
    df["annee"] = year

    # Making sure that population column is numeric
    df["population"] = df["population"].astype("int64")

    # Making sure that department code column is a string (problems with 0 and overseas territories)
    df["dep_code"] = df["dep_code"].astype(str)

    return df


def reshape_data(data):
    df = pd.concat(
        [reshape_table_by_year(data[f"{year}"], year) for year in range(1975, 2023)]
    )
    return df


def plot_population_by_gender_per_department(df, department_code):
    """
    This function plots the evolution of population by gender for a given department code.

    Parameters:
        df (DataFrame): The input DataFrame containing population data.
        department_code (str): The department code to filter the DataFrame by.

    Returns:
        None. Displays a line chart of population evolution by gender for the specified department.
    """

    # Filter the DataFrame by department code
    df = df[df["dep_code"] == department_code]

    # Filter out the total population rows
    df = df[df["genre"] != "Ensemble"]

    # Create a pivot table with population values by year and gender
    df_pivot = df.pivot_table(
        values="population", index="annee", columns="genre", aggfunc="sum"
    )

    # Get first year of data
    first_year = list(df_pivot.index)[0]

    # Get the department name for the title
    department_name = pd.unique(df["dep"])[0]

    # Plot the data
    df_pivot.plot(kind="line")

    # Set x-axis label
    plt.xlabel("Année")
    # Set y-axis label
    plt.ylabel("Population")
    # Set chart title
    plt.title(
        f"Evolution de la population entre {first_year} et 2022 dans le {department_code} ({department_name})"
    )
    # Set legend
    plt.legend(title="Genre")
    # Show the chart
    plt.show()


def get_age_pyramid_data(df, year):
    """
    This function takes a DataFrame as input, and returns a subset of the dataframe that contains
    the population by age, gender, and year, grouped by the specified year.

    Parameters:
    df (pandas.DataFrame): DataFrame containing population data.
    year (int): the year for which to group the population data.

    Returns:
    pandas.DataFrame: DataFrame containing population data for the specified year,
                      grouped by age, gender and year.
    """
    df = df.groupby(["age", "genre", "annee"]).sum("population")
    df = df.unstack(["genre"])
    df.columns = df.columns.droplevel(level=0)
    df = df.reset_index()
    df["Hommes"] = df["Hommes"] * -1
    pyramide_data = df[df["annee"] == year]
    return pyramide_data


def plot_age_pyramid(df, year, ax=None):
    """
    This function takes a DataFrame as input, and plots an age pyramid for a specified year.
    It also optionally takes an axes object to plot the pyramid on.

    Parameters:
    df (pandas.DataFrame): DataFrame containing population data.
    year (int): the year for which to plot the age pyramid.
    ax (matplotlib.axes._subplots.AxesSubplot, optional): Axes on which to plot the pyramid.
                                                        Default is None.

    Returns:
    None
    """
    if ax is None:
        ax = plt.gca()

    data = get_age_pyramid_data(df, year)
    idx = [f"{i-4} à {i} ans" for i in range(94, 0, -5)]

    ax1 = sns.barplot(x="Hommes", y="age", data=data, order=idx, color="purple", ax=ax, legend=False)
    ax2 = sns.barplot(x="Femmes", y="age", data=data, order=idx, color="blue", ax=ax, legend=False)
    ax1.set(ylabel=None)
    ax1.set_title(f"Pyramides des âges de la France en {year}")
    ax1.set_xlabel("Hommes - Femmes")
    ax1.grid()


def load_departements_regions(url):
    df_matching = pd.read_json(url)
    df_matching["num_dep"] = df_matching["num_dep"].astype(str)
    return df_matching


def match_department_regions(df, df_matching):
    df_regions = pd.merge(df, df_matching, left_on=["dep_code"], right_on=["num_dep"])
    return df_regions


def load_geo_data(url):
    geo = gpd.read_file(url)
    return geo


def plot_population_by_regions(df, geo, year):
    df = df[df["annee"] == year]
    df = df.groupby(by=["region_name"]).sum("population")
    df_geo = geo.merge(df.reset_index(), right_on=["region_name"], left_on=["NOM"])

    df_geo.plot(
        column="population",
        legend=True,
        cmap="OrRd",
        edgecolor="black",
        figsize=[15, 7.5],
        legend_kwds={
            "label": "Population des différentes régions de France",
            "orientation": "horizontal",
        },
    )
    # Votre code ici


def compute_population_growth_per_region(df):
    """
    This function takes a DataFrame as input and returns the population growth as a percentage
    for each region, grouped by year.

    Parameters:
    df (pandas.DataFrame): DataFrame containing population data.

    Returns:
    pandas.DataFrame: DataFrame containing population growth as a percentage for each region,
                      grouped by year.
    """
    df = df[df["genre"] != "Ensemble"]
    df = df.pivot_table(
        values="population", index="annee", columns="region_name", aggfunc="sum"
    )
    df_croissance = df.pct_change() * 100
    return df_croissance


def compute_mean_population_growth_per_region(df, min_year, max_year):
    """
    This function takes a DataFrame as input, and returns the mean population growth as a percentage
    for each region, between a given range of years.

    Parameters:
    df (pandas.DataFrame): DataFrame containing population data.
    min_year (int): the minimum year of the range to consider
    max_year (int): the maximum year of the range to consider

    Returns:
    pandas.DataFrame: DataFrame containing mean population growth as a percentage for each region,
                      between the given range of years
    """
    df = compute_population_growth_per_region(df)
    df.reset_index(inplace=True)
    df = df[(df["annee"] >= min_year) & (df["annee"] <= max_year)]
    df = pd.melt(df, id_vars=["annee"], value_name="croissance_pop", var_name="region")
    df_croissance = df.groupby("region").mean()
    return df_croissance


def plot_growth_population_by_regions(df, geo, min_year, max_year):
    df = compute_mean_population_growth_per_region(df, min_year, max_year)
    df_geo = geo.merge(df.reset_index(), right_on=["region"], left_on=["NOM"])

    df_geo.plot(
        column="croissance_pop",
        legend=True,
        cmap="OrRd",
        edgecolor="black",
        figsize=[15, 7.5],
        legend_kwds={
            "label": "Croissance de la population des différentes régions de France (en %)",
            "orientation": "horizontal",
        },
    )
