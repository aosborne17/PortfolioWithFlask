import logging
import boto3
import os

"""
Here we are creating a new logger specific to this module
If ran from this file, the variable will be = main, else if ran elsewhere then the variable will be name of the module,
in this case that will be 'aws_upload'
"""
logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

# we want the configurations to be same as it was for our root configuration, thus we do the following
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

# here we are specifying a file that will be contain our logs
file_handler = logging.FileHandler('upload_s3_new_logger.log')

# Here we are setting the file that we create to have the following formatting when showing the log messages
file_handler.setFormatter(formatter)

# here we are adding the file handler to our new logger
logger.addHandler(file_handler)

# Here we are creating a stream handler that will log the statements in the console
stream_handler = logging.StreamHandler()

# We must then add the stream handler as we did for the life
logger.addHandler(stream_handler)




# we are creating a file that will store our logs
# we are setting the default logging level to debug (it is usually warning)
logging.basicConfig(filename='upload_s3.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def upload_to_aws():

    ACCESS_KEY = os.environ["AWS_ACCESS_KEY"]
    SECRET_KEY = os.environ["AWS_SECRET_KEY"]

    s3_client = boto3.client(
            's3',
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY
        )

    s3_client.upload_file('Downloads/ItJobsWatchTop30.csv', 'andrew-mvc-with-itjobs', 'ItJobsWatchTop30.csv')
    # now we can use the specific logger instead of root
    logger.info("Your file has been successfully uploaded to an AWS bucket!")