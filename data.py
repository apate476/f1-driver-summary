import pandas as pd


# load data from the csv
race_results = pd.read_csv("E:/f1-predictor/data/race_results_2025.csv")

# print(race_results.head())

# sum the points - practice
total_points = race_results.groupby("driver_name")["points"].sum()

total_wins = race_results.groupby("driver_name")["finish_position"].agg(lambda x: (x == 1).sum())

# print(total_wins, total_points)

def load_drivers():
    grouped = race_results.groupby("driver_name").agg({"points":"sum","finish_position": lambda x: (x == 1).sum()}).reset_index()

    grouped.columns = ['driver_name', 'total_points', 'wins']
    
    drivers_list = grouped.to_dict('records')
    return drivers_list

drivers = load_drivers()
print(drivers[0])