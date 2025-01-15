import os
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "temperature_data")
output_dir = os.path.join(current_dir, "output")

os.makedirs(output_dir, exist_ok=True)

# Combine all CSV data
all_data = pd.DataFrame()
csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

try:
    for file_name in csv_files:
        file_path = os.path.join(data_dir, file_name)
        df = pd.read_csv(file_path)
        all_data = pd.concat([all_data, df], ignore_index=True)

    # Clean column names
    all_data.columns = all_data.columns.str.strip().str.capitalize()

    # Check for expected months
    months = [
        'January', 'February', 'March', 'April', 'May',
        'June', 'July', 'August', 'September', 'October',
        'November', 'December'
    ]
    monthly_cols = [col for col in all_data.columns if col in months]
    if not monthly_cols:
        raise ValueError("No monthly temperature columns found.")

    # Monthly average temperatures
    monthly_averages = all_data[monthly_cols].mean()

    # Seasonal averages
    season_map = {
        'Summer': ['December', 'January', 'February'],
        'Autumn': ['March', 'April', 'May'],
        'Winter': ['June', 'July', 'August'],
        'Spring': ['September', 'October', 'November']
    }
    season_averages = {}
    for season, season_months in season_map.items():
        if all(m in all_data.columns for m in season_months):
            season_averages[season] = all_data[season_months].mean(axis=1).mean()

    # Station-level stats (if available)
    if 'Station_name' in all_data.columns:
        # Temperature range per station
        all_data['Temperature range'] = (
            all_data[monthly_cols].max(axis=1) - all_data[monthly_cols].min(axis=1)
        )
        max_range = all_data['Temperature range'].max()
        largest_range_stations = all_data[
            all_data['Temperature range'] == max_range
        ]['Station_name'].unique()

        # Average temperature per station
        all_data['Average temperature'] = all_data[monthly_cols].mean(axis=1)
        warmest_temp = all_data['Average temperature'].max()
        coolest_temp = all_data['Average temperature'].min()
        warmest_stations = all_data[
            all_data['Average temperature'] == warmest_temp
        ]['Station_name'].unique()
        coolest_stations = all_data[
            all_data['Average temperature'] == coolest_temp
        ]['Station_name'].unique()

    # Write monthly and seasonal averages
    avg_temp_file = os.path.join(output_dir, 'average_temp.txt')
    with open(avg_temp_file, 'w') as f:
        f.write("Monthly Averages:\n")
        for m, val in monthly_averages.items():
            f.write(f"{m}: {val:.2f}°C\n")
        f.write("\nSeason Averages:\n")
        for s, val in season_averages.items():
            f.write(f"{s}: {val:.2f}°C\n")

    # Write station with largest temp range
    if 'Station_name' in all_data.columns:
        largest_range_file = os.path.join(output_dir, 'largest_temp_range_station.txt')
        with open(largest_range_file, 'w') as f:
            f.write("Stations with Largest Temperature Range:\n")
            for station in largest_range_stations:
                f.write(f"{station}\n")

        # Write warmest and coolest stations
        warmest_coolest_file = os.path.join(output_dir, 'warmest_and_coolest_station.txt')
        with open(warmest_coolest_file, 'w') as f:
            f.write("Warmest Stations:\n")
            for station in warmest_stations:
                f.write(f"{station}\n")
            f.write("\nCoolest Stations:\n")
            for station in coolest_stations:
                f.write(f"{station}\n")

    print("Analysis done. Results are in the 'output' folder.")

except Exception as e:
    print(f"Error: {e}")