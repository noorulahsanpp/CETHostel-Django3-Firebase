import firebase_admin
from firebase_admin import credentials, firestore
from oauth2client.service_account import ServiceAccountCredentials


class FirebaseInit():
    cred = credentials.Certificate('/home/noorul/PycharmProjects/HostelApp/hostelapp-f9328-firebase-adminsdk-yfmwt-27619886a6.json')
    # cred = credentials.Certificate(
    #     'C:/Users/Noorul/PycharmProjects/CETHostel-Django3-Firebase/hostelapp-f9328-firebase-adminsdk-yfmwt-27619886a6.json')
    app = firebase_admin.initialize_app(cred)
    store = firestore.client()

def _get_access_token():
  """Retrieve a valid access token that can be used to authorize requests.

  :return: Access token.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      'service-account.json', SCOPES)
  access_token_info = credentials.get_access_token()
  return access_token_info.access_token