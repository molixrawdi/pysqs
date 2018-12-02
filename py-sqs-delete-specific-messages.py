#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
import boto3, sys, getopt

# Create SQS client
sqs = boto3.client('sqs')

queue_url = str(sys.argv[1])  # 'SQS_QUEUE_URL'
#SentTimestamps = Possible to use as alternative to Message_ID if needed
Message_ID= str(sys.argv[2])
# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'Message_ID'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

# Delete received message from queue
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)
print('Received and deleted message: %s' % message)
