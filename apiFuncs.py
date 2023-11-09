import requests
import json
import os
# Access the secrets

def findProductUsingUPC(upc, api_key):
    # Define the API endpoint URL
    url = f"https://api.spoonacular.com/food/products/upc/{upc}?apiKey={api_key}"

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


def main():
    # Replace these placeholders with your actual UPC and API key
    upc = "9343787001503"
    api_key = ""

    findProductUsingUPC(upc, api_key)

#Testing help
if __name__ == "__main__":
    main()