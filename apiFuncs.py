import requests
import json
import os

# Access the secrets / api keys stored in github secrets

def findProductUsingUPC(upc, api_key):
    # Define the API endpoint URL
    url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={api_key}&query={upc}"

    try:
        # Send an HTTP GET request to the API endpoint
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Save the JSON data to a file
            with open("output.json", "w") as output_file:
                output_file.write(json.dumps(data, indent=4))

            print("JSON data saved to 'output.json'")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def getInfoFromJSON(filename):
    print("Getting info...")

    # Specify the path to the JSON file
    jsonFilePath = filename

    # Open the JSON file
    with open(jsonFilePath, 'r') as file:
        # Load the JSON data
        data = json.load(file)
    
    name = data["foods"][0]["description"].lstrip().capitalize()
    category = data["foods"][0]["foodCategory"].lstrip().capitalize()

    #Find block with kcal info
    calories = 0
    for index, block in enumerate(data["foods"][0]["foodNutrients"]):
        if block["nutrientId"] == 1008:
            calories = block["value"]
            break

    return name, category, calories

def main():
    # Replace these placeholders with your actual UPC and API key
    upc = "878589001707 "
    api_key = "DEMO_KEY"

    findProductUsingUPC(upc, api_key)
    name, category, cal = getInfoFromJSON("output.json")

    print(name, category, cal)

#Testing help
if __name__ == "__main__":
    main()