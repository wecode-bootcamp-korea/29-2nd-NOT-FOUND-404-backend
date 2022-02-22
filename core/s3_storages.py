import boto3

from notfound.settings import aws_secret_access_key, aws_access_key_id, aws_storage_bucket_name

class S3:
    def __init__(self, aws_access_key_id, aws_secret_access_key, aws_storage_bucket_name):
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        self.s3_client = s3_client
        self.bucket = aws_storage_bucket_name

    def upload(self, file):
        try:
            self.s3_client.upload_fileobj(
            file,
            aws_storage_bucket_name,
            file.name,
            )
            return f'https://s3.ap-northeast-2.amazonaws.com/notfound404/{file.name}'
        except:
            return None

    def delete(self, file):
        return self.s3_client.delete_object(Bucket=self.bucket, Key=file)

s3_client = S3(aws_access_key_id, aws_secret_access_key, aws_storage_bucket_name)
