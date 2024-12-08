'''
Author: Alex Cecil
Email: ajcecil@iastate.edu
Date: 2024-12-08

Description: The functions in this script are used to find comments which contain the phrase, TODO and convert those comments into a list of task stored in a csv file.
'''



import os
import csv
import re

def extract_todos(script_path):
    """
    Extracts all TODO comments from the script.
    """
    todos = []
    with open(script_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            match = re.search(r'#\s*TODO\s*:(.*)', line, re.IGNORECASE)
            if match:
                todos.append((line_number, match.group(1).strip()))
    return todos

def write_todos_to_csv(todos, csv_path):
    """
    Writes TODO comments to a CSV file.
    """
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Line Number", "Comment"])
        writer.writerows(todos)

def generate_list(script_path):
    """
    Generates a CSV file of TODO comments in the same directory as the script.
    """
    script_name = os.path.splitext(os.path.basename(script_path))[0]  # Get filename without extension
    script_dir = os.path.dirname(script_path)  # Get script's directory
    csv_path = os.path.join(script_dir, f"{script_name}_todos.csv")  # Construct CSV file path
    
    todos = extract_todos(script_path)  # Extract TODO comments
    write_todos_to_csv(todos, csv_path)  # Write to CSV

if __name__ == "__main__":
    generate_list(__file__)
