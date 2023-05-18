import os
from venv import create
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# https://www.youtube.com/watch?v=rcE3iL0URhU&ab_channel=SamuelChan
# https://developers.google.com/youtube/reporting/v1/reports/metrics?hl=en

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']

API_SERVICE_NAME = 'youtubeAnalytics'
API_VERSION = 'v2'
CLIENT_SECRETS_FILE = 'client_secret_898467674662-a1b5vidubbadgt1om1cic23mho33ngok.apps.googleusercontent.com.json'


def get_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_local_server()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def execute_api_request(client_library_function, **kwargs):
  response = client_library_function(
    **kwargs
  ).execute()
  return response

if __name__ == "__main__":
    youtubeAnalytics = get_service()
    result = execute_api_request(
        youtubeAnalytics.reports().query,
        ids='channel==MINE',
        startDate='2022-01-01',
        endDate='2023-04-30',
        metrics='estimatedMinutesWatched,views,likes,subscribersGained',
        dimensions='video, day',
        sort='day'
    )
    print(result)