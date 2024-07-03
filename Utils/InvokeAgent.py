# Import libraries
import requests
import json

# Replace with your actual values
project_id = "YOUR_PROJECT_ID"
agent_id = "YOUR_AGENT_ID"
region = "global"  # Replace with your region
session_id = "1234y"  # You can generate a random ID here
user_query = "Any flights from New York?"
access_token="REPLACE_WITH_ACCESS_TOKEN"

# Construct the API request URL
api_url = f"https://dialogflow.googleapis.com/v3/projects/{project_id}/locations/{region}/agents/{agent_id}/sessions/{session_id}:detectIntent"
#print(api_url) 

# Prepare the request body
request_body = {
  "queryInput": {
    "text": {
      "text": user_query      
    },
    "language_code": "en"
  }
}

# Send HTTP POST request with JSON data
#headers = {'Content-Type': 'application/json; charset=utf-8'}
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json; charset=utf-8'
}

response = requests.post(api_url, headers=headers, data=json.dumps(request_body))

# Check for successful response
if response.status_code == 200:
  print(response.text)
  
  # Parse JSON response
  ##response_data = json.loads(response.text)
  
  # Access relevant data from the response
  ## detected_intent = response_data.get('queryResult', {}).get('intent', {})
  ## intent_name = detected_intent.get('displayName')
  ## print(f"Detected Intent: {intent_name}")
  
  ## Access additional information from the response (optional)
  ## fulfillment_text = response_data.get('queryResult', {}).get('fulfillmentText')
  ## print(f"Agent Response: {fulfillment_text}")
else:
  print(f"API request failed with status code: {response.status_code}")
