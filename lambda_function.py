import os
from datetime import datetime
from urllib.request import Request, urlopen

SITE = os.environ['site']  # URL of the site to check, stored in the site environment variable
EXPECTED = os.environ['expected']  # String expected to be on the page, stored in the expected environment variable
BUCKET_NAME = os.environ['bucket']

def validate(file_as_string):
    '''Return False to trigger the canary

    Currently this simply checks whether the EXPECTED string is present.
    However, you could modify this to perform any number of arbitrary
    checks on the contents of SITE.
    '''
    import json
    
    obj = json.loads(file_as_string)

    provider_name = obj['countries'][0]['name']
    
    return EXPECTED == provider_name
    
def write_to_bucket(contents: bytes, timestamp: str):
    import boto3
    file_name = f"{BUCKET_NAME}/{timestamp}.json"
    
    s3 = boto3.resource("s3")
    s3.Bucket(BUCKET_NAME).upload_fileobj(Key=file_name, Body=contents)


def lambda_handler(event, context):
    print('Checking {} at {}...'.format(SITE, event['time']))

    try:
        req = Request(SITE, headers={'User-Agent': 'AWS Lambda'})
        contents = urlopen(req).read()

        write_to_bucket(contents, event['time'])
        
    except:
        print('Check failed!')
        raise
    else:
        print('Check passed!')
        return event['time']
    finally:
        print('Check complete at {}'.format(str(datetime.now())))
