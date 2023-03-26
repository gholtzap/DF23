import csv
from collections import defaultdict
from datetime import datetime

# Function to read CSV file and return a list of rows
def read_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    return data

# Function to convert the date format to a datetime object
def parse_date(date_string):
    return datetime.strptime(date_string, '%m/%d/%Y %I:%M:%S %p')

# Function to split the data into months
def split_data_by_month(data):
    monthly_data = defaultdict(list)
    
    for row in data:
        date_str = row[0] # assuming the date is the first column in your CSV
        date_obj = parse_date(date_str)
        month_key = (date_obj.year, date_obj.month)
        monthly_data[month_key].append(row)
    
    return monthly_data


file_path = 'data/clients.csv' 
csv_data = read_csv(file_path)
monthly_data, header = split_data_by_month(csv_data)
print(monthly_data)

def write_monthly_data_to_csv(monthly_data, header, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header row with an additional 'Month-Year' column
        writer.writerow(['Month-Year'] + header)

        for month_key, data in monthly_data.items():
            month_year = f"{month_key[1]}/{month_key[0]}"
            
            for row in data:
                writer.writerow([month_year] + row)

output_file = 'data/grouped_data.csv'  # Replace with your desired output file name
write_monthly_data_to_csv(monthly_data, header, output_file)

# Print data by month
    
def split_data_by_month(data):
    monthly_data = defaultdict(list)

    header = data[0]  # Save the header row

    for row in data[1:]:  # Skip the header row
        date_str = row[0]  # assuming the date is the first column in your CSV
        try:
            date_obj = parse_date(date_str)
            month_key = (date_obj.year, date_obj.month)
            monthly_data[month_key].append(row)
        except ValueError:
            print(f"Unable to parse date from row: {row}")

    return monthly_data, header

