def Google_Drive_API(files):
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload

    # Set up the service account credentials
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = 'E:\Codeing\Python Language\Projects\Project_13_YT_Video_Download_Convert\Project-13_Service_key.json'

    Credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    drive_service = build('drive', 'v3', credentials=Credentials)

    # Extract the folder ID from the URL
    Folder_URL = 'https://drive.google.com/drive/folders/1af5MLZn2HbBP9JAbIze0h8xQjQnS-Sz6'
    Folder_ID = Folder_URL.split('/')[-1]

    # Upload a File to Google Drive within the specified folder
    File_Metadata = {
        'name': "Music",  # Name for the uploaded File
        'parents': [Folder_ID],  # ID of the target folder
    }
    Upload=files
    Media = MediaFileUpload(Upload, mimetype='audio/wav')
    File = drive_service.files().create(body=File_Metadata, media_body=Media).execute()

    print(f'File ID: {File.get("id")}')
    print("File Upload Completed")




