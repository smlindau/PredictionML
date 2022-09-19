import pandas as pd
from pathlib import Path

county_data_2020 = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-2020.csv"
county_data_2021 = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-2021.csv"
county_data_2022 = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-2022.csv"

# Check if the 2020 and 2021 data files already exist; if not, download and create them
if not Path("countyData2020.csv").exists():
    pd.read_csv(county_data_2020).to_csv("countyData2020.csv")
if not Path("countyData2021.csv").exists():
    pd.read_csv(county_data_2021).to_csv("countyData2021.csv")

# Update the 2022 csv file with new data
pd.read_csv(county_data_2022).to_csv("countyData2022.csv")
