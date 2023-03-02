import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'D:\Sparta\dir1\data210\data_engineering\data-210-2626a442f581.json'

client = storage.Client()
bucket_name = 'sparta-data210-gcp'
bucket = client.get_bucket('sparta-data210-gcp')


def read_file(blob_name):
    # storage_client = storage.Client()
    # storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    data_string = blob.download_as_string()
    print(data_string.decode())


def download_file(blob_name):
    # storage_client = storage.Client()
    # storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.download_to_filename(blob_name)
    print("Downloaded from bucket {} to local file {}.".format(bucket_name, blob_name))

download_file('img.PNG')

def upload_file(blob_name):
    # storage_client = storage.Client()
    # bucket = bucket # storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(blob_name)
    print("Downloaded from bucket {} to local file {}.".format(bucket_name, blob_name))

upload_file('img.PNG')