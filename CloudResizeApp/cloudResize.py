from PIL import Image
filename = "buildings.jpg"
with Image.open(filename) as img:
    img.load()
type(img)
# regenerate imgs
# img.show()

# for logs
# print(isinstance(img, Image.Image))
# img.format
# img.size
# img.mode


# extract one building from all buildings
cropped = img.crop((300,50,700,1000))
# cropped.show()

# resize for customized low resolution 1
# low_res_img = cropped.resize(
#     (cropped.width//4, cropped.height//4)
# )
# low_res_img.show()

# resize for customized low resolution 2
low_res_img2 = cropped.reduce(4)
# low_res_img2.show()
low_res_img2.save("thumbnail.png", "PNG")

# make thumbnail
thumb = img.thumbnail((200,200))



# connect this to AWS S3 BUCKET 
import boto3
# env file
from dotenv import load_dotenv

load_dotenv()

def s3_connection():
    try:
        # s3 클라이언트 생성
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id="{ACCESS_KEY}",
            aws_secret_access_key="{SECRET_KEY}",
        )
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!") 
        return s3
        
s3 = s3_connection()
 
uploading_file = "thumbnail.png"
try:
    s3.upload_file("{uploading_file}","{S3_BUCKET}","{uploading_file[:4]}_thumbnail")
except Exception as e:
    print(e)