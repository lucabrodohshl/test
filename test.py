from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Load credentials
credentials = Credentials.from_service_account_file('test-project-431212-b6a4d09d7301.json')

# Build the Google Drive service
drive_service = build('drive', 'v3', credentials=credentials)

# Get the folder
folder_id = '1dxpWM5UIsgjfrH2_Dsrr3dS9owzOGWzN'
results = drive_service.files().list(
    q=f"'{folder_id}' in parents",
    pageSize=10,
    fields="nextPageToken, files(id, name)").execute()

items = results.get('files', [])

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print(f"{item['name']} ({item['id']})")
