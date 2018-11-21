import boto3
# Get the service resource
# Due to the nature and features of 'boto3' it has come to my attention that one can do this
sqs = boto3.resource('sqs')
sqs_c = boto3.client('sqs')
# Create the queue. This returns an SQS.Queue instance
#queue = sqs.create_queue(QueueName='DS-380', Attributes={'DelaySeconds': '5'})
# Different ways for getting queue name
#queue = sqs.get_queue_by_name(QueueName='DS-380')
queue = sqs.get_queue_by_name(QueueName = input('Enter Queue Name Please:'))
# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))

print('Creating new message for this queue that was identifies')
# Create a new message
# Send message to SQS queue
msg_generate = sqs_c.send_message(
    QueueUrl=queue.url,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
    )
)

print(msg_generate['MessageId'])

# Delete SQS queue
# sqs.delete_queue(QueueUrl='SQS_QUEUE_URL')

# Deleting a message

