import os

import yaml

paths_directory = "paths"

def extract_and_save_method(api_spec, path, method, method_data):
    # Check if $ref already exists, if it does, skip this method
    if "$ref" in method_data:
        print(f"Skipping {method} method in path: {path} as $ref is already present.")
        return
    
    operation_id = method_data.get("operationId")
    if not operation_id:
        print(f"No operationId for {method} method in path: {path}")
        return
    
    # Ensure the paths directory exists
    if not os.path.exists(paths_directory):
        os.makedirs(paths_directory)
    
    file_name = f"{operation_id}.yaml"
    file_path = os.path.join(paths_directory, file_name)

    # Save method data to new file
    with open(file_path, 'w') as new_file:
        yaml.dump(method_data, new_file)
    
    # Replace method definition with $ref to new file
    api_spec[paths_directory][path][method] = {"$ref": f"./paths/{file_name}"}

def list_api_paths(file_path):
    """
    Function to read OpenAPI specification from a YAML file
    and list all the API paths.

    :param file_path: str, path to the OpenAPI YAML file.
    :return: None
    """
    try:
        with open(file_path, "r") as file:
            api_spec = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {str(e)}")
        return

    paths = api_spec.get("paths", {})
    if not paths:
        print("No paths found in the API specification.")
        return

    print("List of API paths:")
    for path, methods in paths.items():
        print(f"  {path}")
        for method, method_data in methods.items():
            extract_and_save_method(api_spec, path, method, method_data)
    
    # Save the modified API spec back to the original file (or another file if preferred)
    with open(file_path, 'w') as file:
        yaml.dump(api_spec, file)


if __name__ == "__main__":
    # Example usage:
    # Replace 'index.yaml' with the path to your OpenAPI specification file.
    list_api_paths("index.yaml")
