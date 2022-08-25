import json
import urllib.parse
import boto3
import pandas as pd
import awswrangler as wr

# TODO proper logging (logger)

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object and bucket keys from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        # Get the object
        print('Getting s3 object')
        response = s3.get_object(Bucket=bucket, Key=key)
    except Exception as e:
        print(e)
        raise e
    # Parse the object as a dataframe
    df_s3_data = pd.read_csv(response['Body'], sep=',')
    # Do a simple 'pivot' on gender
    df_pivot = df_s3_data.groupby('gender').sum()
    print(df_pivot)
    # Connect to RDS
    print('Connecting to RDS')
    try:
        conn = wr.mysql.connect(
            dbname="scientific-homework",
            secret_id="arn:aws:secretsmanager:us-east-2:705867055667:secret:science_homework_rds-yNiOga",
            connect_timeout = 10
)
    except Exception as e:
        print("ERROR: Could not connect to RDS")
        print(e)
        raise(e)
    # Try connecting to the table
    print('use connection')
    wr.mysql.to_sql(
        df=df_pivot,
        table="gender_identity",
        schema="homework",
        con=conn
)
    #print('Create table')
    #conn.execute('CREATE TABLE IF NOT EXISTS gender_identity')
    #print('Write to table')
    # Hail mary
    #df_pivot.to_sql(name='gender_identity',con=conn)

    # The return can be more informative which would be useful for logging.
    return(True)
