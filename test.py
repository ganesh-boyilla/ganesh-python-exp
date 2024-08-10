print(" Poll SCM hello world!!")
import csv
  
def process_csv(file_path):
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)  # Process each row as needed

# Example usage
if __name__ == "__main__":
    process_csv('data.csv')

