# Method will be GET
# Need to input card details you want to get info about
# format that will be sent is JSON to cardmarket API
# first get every info possible about card, later filter what we need
import requests

def fetch_card_info(card_name):
    resource_url = "https://api.cardmarket.com/ws/v2.0/products/find"

    # Replace 'your_access_token' with your actual Cardmarket API access token
    access_token = 'your_access_token'

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }

    # Specify the card details in the request payload
    payload = {
        "idGame": 1,  # Assuming you are interested in Pokemon cards (check the correct game ID)
        "search": card_name,
        "exact": True,
        "isFoil": True,  # Set to True if you want foil cards
    }

    try:
        response = requests.get(resource_url, headers=headers, params=payload)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            card_info = response.json()
            # Print or process the card information
            print(card_info)
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
card_name_to_fetch = 'example-card-name'
fetch_card_info(card_name_to_fetch)
