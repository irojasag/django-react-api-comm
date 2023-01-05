import csv

def get_csv_data():
    # create a dictionary
    data = []
     
    # Open a csv reader called DictReader
    with open("./api/diabetes.csv", encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            data.append(rows)
    return data