Automated Image Processing System Using AWS

Project Description

This project automatically resizes images uploaded to Amazon S3 using AWS Lambda, Python, and Pillow.

AWS Services Used

- Amazon S3
- AWS Lambda
- AWS IAM
- Amazon CloudWatch

Technologies Used

- Python
- Pillow
- AWS Console

Project Workflow

1. Upload an image to the input S3 bucket.
2. Amazon S3 triggers the Lambda function automatically.
3. Lambda reads the uploaded image.
4. Pillow resizes the image to fit within 300 × 300 pixels.
5. The resized image is saved in the output S3 bucket.
6. CloudWatch records the execution logs.

AWS Resources

- Input Bucket: "image-input-bucket"
- Output Bucket: "image-output-buck"
- Lambda Function: "ImageProcessingFunction"
- Runtime: Python 3.14

IAM Permissions

The Lambda execution role uses the following permissions:

- "s3:GetObject" — Reads images from the input bucket.
- "s3:PutObject" — Saves resized images to the output bucket.
- CloudWatch logging permissions — Allows Lambda to record execution logs.

Result

Images uploaded to the input S3 bucket are automatically resized and saved in the output S3 bucket.

Learning Outcomes

- Understanding Amazon S3 buckets and event notifications.
- Creating and configuring AWS Lambda functions.
- Configuring IAM permissions for S3 access.
- Using Python and Pillow for image processing.
- Monitoring Lambda execution using CloudWatch.