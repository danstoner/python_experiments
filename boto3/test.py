import logging
import boto3
from botocore.exceptions import ClientError

"""
Create an S3 presigned url to a particular version of an object.
"""

def create_presigned_url(bucket_name, object_name, object_version_id, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    session = boto3.Session(profile_name='dev')
    # Generate a presigned URL for the S3 object
    s3_client = session.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name,
                                                            'VersionId': object_version_id},
                                                    ExpiresIn=expiration)
        print(response)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response

if __name__ == '__main__':


    create_presigned_url('test-bucket', 'sample.txt', 'uoP4bCAavmKSb6syb1FoOkp3iIZT5xIa', expiration=3600)
