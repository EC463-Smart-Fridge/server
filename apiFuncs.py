import requests
import json
import os
# Access the secrets

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


def main():
    # Replace these placeholders with your actual UPC and API key
    upc = "0024000258292"
    api_key = "DEMO_KEY"

    findProductUsingUPC(upc, api_key)

#Testing help
if __name__ == "__main__":
    main()