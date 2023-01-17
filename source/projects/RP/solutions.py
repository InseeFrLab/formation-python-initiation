import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import seaborn as sns


def load_data():
    data = pd.read_excel(
        "https://minio.lab.sspcloud.fr/tfaria/public/estim-pop-dep-sexe-aq-1975-2022.ods",
        engine="odf",
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
        df.stack(level=0).reset_index(),
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
    sample = df[df["annee"] == year]
    return sample


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

    ax1 = sns.barplot(x="Hommes", y="age", data=data, order=idx, palette="RdPu", ax=ax)
    ax2 = sns.barplot(x="Femmes", y="age", data=data, order=idx, palette="Blues", ax=ax)
    ax1.set(ylabel=None)
    ax1.set_title(f"Pyramides des âges de la France en {year}")
    ax1.set_xlabel("Hommes - Femmes")
    ax1.grid()
