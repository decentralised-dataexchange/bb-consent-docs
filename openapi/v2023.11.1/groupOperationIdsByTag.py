import csv
import os

import yaml


def get_operation_ids_from_file(file_path):
    """
    Given a file path, read the OpenAPI file, extract and return a dictionary 
    where the keys are tags and values are lists of operationId's
    """
    with open(file_path, 'r') as file:
        try:
            api_spec = yaml.safe_load(file)
            paths = api_spec.get('paths', {})
            tag_operation_map = {}
            tags = api_spec.get('tags', [])
            operation_id = api_spec.get('operationId')
            description = api_spec.get('description')
            for tag in tags:
                if tag in tag_operation_map:
                    tag_operation_map[tag].append({'operationId': operation_id, 'description': description})
                else:
                    tag_operation_map[tag] = [{'operationId': operation_id, 'description': description}]
            return tag_operation_map
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file {file_path}: {str(e)}")
            return {}

def iterate_through_files(folder_name, output_csv_file):
    """
    Iterate through all YAML files in the specified folder, 
    extract tags and operationIds and print them
    """
    tags = {}

    folder_path = os.path.join(os.getcwd(), folder_name)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".yaml"):
                file_path = os.path.join(root, file)
                tag_operation_map = get_operation_ids_from_file(file_path)
                print(f"APIs in {file_path}:")
                for tag, operations in tag_operation_map.items():
                    print(f"  {tag}:")
                    for operation in operations:
                        print(f"    - {operation.get('operationId')}: {operation.get('description')}")
                        tags.setdefault(tag, []).append(operation)
    

    # Print number of api's per tag
    print("Number of APIs per tag:")
    for tag, operations in tags.items():
        print(f"  {tag}: {len(operations)}")

    # Write to CSV file
    with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Tag", "OperationId", "Description"])
        writer.writeheader()
        for tag, operations in tags.items():
            for operation in operations:
                writer.writerow({
                    "Tag": tag, 
                    "OperationId": operation.get('operationId'), 
                    "Description": operation.get('description')
                })

if __name__ == "__main__":
    # Example usage:
    # Replace 'index.yaml' with the path to your OpenAPI specification file.
    iterate_through_files("paths", "output.csv")