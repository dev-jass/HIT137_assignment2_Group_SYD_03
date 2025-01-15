import os
import pandas as pd

folder_path = "C:/Users/harde/OneDrive/Desktop/assignment_h/temperature_data" 
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
all_data = pd.DataFrame()

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    yearly_data = pd.read_csv(file_path)
    all_data = pd.concat([all_data, yearly_data], ignore_index=True)

all_data.columns = all_data.columns.str.strip().str.capitalize()

expected_months = [
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
]


monthly_columns = [col for col in all_data.columns if col in expected_months]

if not monthly_columns:
    raise ValueError("No monthly temperature columns found in the dataset!")

monthly_averages = all_data[monthly_columns].mean()


season_mapping = {
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August'],
    'Spring': ['September', 'October', 'November']
}

season_averages = {
    season: all_data[months].mean(axis=1).mean() 
    for season, months in season_mapping.items() if all(month in all_data.columns for month in months)
}


if 'Station_name' in all_data.columns:  
    all_data['Temperature Range'] = all_data[monthly_columns].max(axis=1) - all_data[monthly_columns].min(axis=1)
    largest_temp_range = all_data['Temperature Range'].max()
    stations_with_largest_range = all_data[all_data['Temperature Range'] == largest_temp_range]['Station_name'].unique()


if 'Station_name' in all_data.columns:
    all_data['Average Temperature'] = all_data[monthly_columns].mean(axis=1)
    warmest_station_temp = all_data['Average Temperature'].max()
    coolest_station_temp = all_data['Average Temperature'].min()

    warmest_stations = all_data[all_data['Average Temperature'] == warmest_station_temp]['Station_name'].unique()
    coolest_stations = all_data[all_data['Average Temperature'] == coolest_station_temp]['Station_name'].unique()

with open('C:/Users/harde/OneDrive/Desktop/assignment_h/average_temp.txt', 'w') as f:
    f.write("Average Temperatures for Each Month:\n")
    for month, avg_temp in monthly_averages.items():
        f.write(f"{month}: {avg_temp:.2f}°C\n")
    f.write("\nAverage Temperatures for Each Season:\n")
    for season, avg_temp in season_averages.items():
        f.write(f"{season}: {avg_temp:.2f}°C\n")

# Stations with the largest temperature range
if 'Station_name' in all_data.columns:
    with open('C:/Users/harde/OneDrive/Desktop/assignment_h/largest_temp_range_station.txt', 'w') as f:
        f.write("Station(s) with the Largest Temperature Range:\n")
        for station in stations_with_largest_range:
            f.write(f"{station}\n")

# Warmest and coolest stations
if 'Station_name' in all_data.columns:
    with open('C:/Users/harde/OneDrive/Desktop/assignment_h/warmest_and_coolest_station.txt', 'w') as f:
        f.write("Warmest Station(s):\n")
        for station in warmest_stations:
            f.write(f"{station}\n")
        f.write("\nCoolest Station(s):\n")
        for station in coolest_stations:
            f.write(f"{station}\n")

print("Analysis complete. Results saved to respective files.")
