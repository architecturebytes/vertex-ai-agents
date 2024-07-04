import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account

# Path to your service account key file
SERVICE_ACCOUNT_FILE = '/<PATH_TO_YOUR_SERVICE_ACCOUNT_KEY_FILE>/your-key-file.json'

# Scope required for Dialogflow
SCOPES = ['https://www.googleapis.com/auth/dialogflow']

# Create credentials using the service account file and the required scopes
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Refresh the credentials to get an access token
credentials.refresh(Request())
access_token = credentials.token
expiry = credentials.expiry

print(f'Access Token: {access_token}')
# print(datetime.now(timezone.utc))
print(f'Expiry: {expiry}')
