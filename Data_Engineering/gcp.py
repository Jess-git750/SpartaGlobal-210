#Import the necessary modules and create a client object with the credentials of the service account:
from google.cloud import storage
client = storage.Client.from_service_account_json('turnkey-topic-379316-a81feacb6938.json')
#Access the bucket by its name using the client object:
bucket = client.get_bucket('jess_sparta_bucket')
#Once you have access to the bucket, you can perform various operations such as uploading, downloading, and deleting files. For example, to upload a file to the bucket:
blob = bucket.blob('myfile.txt')
blob.upload_from_filename('image_test.JPG')

blob.download_to_filename('Image_downloaded.jpg') #This is to download our file

content = blob.download_as_string()  #this is to read only a text file