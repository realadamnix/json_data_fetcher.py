"""
Copyright: Adam Nix (2024)
"""

import requests  # Import the requests library for making HTTP requests
import json  # Import the json library for handling JSON data

def fetch_data(api_url):
    """
    Fetches data from the given API URL.
    """
    response = requests.get(api_url)  # Make a GET request to the API
    if response.status_code == 200:  # Check if the request was successful
        return response.json()  # Return the JSON data from the response
    else:
        print(f"Error: Unable to fetch data (Status code: {response.status_code})")  # Print an error message if the request failed
        return None

def save_to_file(data, filename):
    """
    Saves the given data to a JSON file.
    """
    with open(filename, 'w') as file:  # Open the file in write mode
        json.dump(data, file, indent=4)  # Write the data to the file in JSON format with indentation
    print(f"Data saved to {filename}")  # Print a confirmation message

if __name__ == "__main__":
    api_url = ""  # Enter the API URL here
    data = fetch_data(api_url)  # Fetch the data from the API

    if data:  
        print("Data was fetched successfully:")
        filename = "posts_data.json"  # Name of the file to save the data to
        save_to_file(data, filename)  # Save the data to the file
    else:
        print("Data not fetched successfully.")
