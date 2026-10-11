import boto3
import os
from PIL import Image
from io import BytesIO
from urllib.parse import unquote_plus

s3 = boto3.client("s3")

OUTPUT_BUCKET = "image-output-buck"


def lambda_handler(event, context):
    for record in event["Records"]:
        input_bucket = record["s3"]["bucket"]["name"]
        image_key = unquote_plus(record["s3"]["object"]["key"])

        response = s3.get_object(
            Bucket=input_bucket,
            Key=image_key
        )

        image_data = response["Body"].read()

        image = Image.open(BytesIO(image_data))
        image.thumbnail((300, 300))

        output_buffer = BytesIO()

        image.convert("RGB").save(
            output_buffer,
            format="JPEG"
        )

        output_buffer.seek(0)

        output_key = (
            os.path.splitext(image_key)[0] + "_resized.jpg"
        )

        s3.put_object(
            Bucket=OUTPUT_BUCKET,
            Key=output_key,
            Body=output_buffer.getvalue(),
            ContentType="image/jpeg"
        )

        print(f"Resized image saved: {output_key}")

    return {
        "statusCode": 200,
        "body": "Image processed successfully!"
    }