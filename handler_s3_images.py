from dotenv import load_dotenv
import boto3
import os

load_dotenv()

AWS_ACCESS_KEY_ID=os.getenv("ENV_AWS_ACCES_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("ENV_AWS_SECRET_ACCESS_KEY")



def upload_images(filename):

    s3 = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    with open("images/"+filename+".png", "rb") as f:
        s3.upload_fileobj(f, "awsradarimages", "images/"+filename+".png")


def upload_images_color(filename):

    s3 = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    with open("images_color/"+filename+".png", "rb") as f:
        s3.upload_fileobj(f, "awsradarimages", "images_color/"+filename+".png")


def upload_images_small(filename):

    s3 = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    with open("images_small/"+filename+".png", "rb") as f:
        s3.upload_fileobj(f, "awsradarimages", "images_small/"+filename+".png")





def download_images(filename):

    s3 = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    s3.download_file("awsradarimages","images/"+filename,"images/"+filename)
    

def download_images_color(filename):

    s3 = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    s3.download_file("awsradarimages","images_color/"+filename,"images_color/"+filename)


def download_images_small(filename):

    s3 = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    
    s3.download_file("awsradarimages","images_small/"+filename,"images_small/"+filename)




def s3_images_list():

    images_list = []

    s3 = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    for obj in s3.list_objects(Bucket="awsradarimages")['Contents']:
        image_name = (obj['Key'])

        if not "images_small" in image_name and not "images_color" in image_name:  
            image_name = image_name.replace("images/","")
            images_list.append(image_name)
            
    images_list.pop(0)
    
    return images_list



def s3_images_small_list():

    images_list = []

    s3 = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    for obj in s3.list_objects(Bucket="awsradarimages")['Contents']:
        image_name = (obj['Key'])

        if "images_small" in image_name:  
            image_name = image_name.replace("images_small/","")
            images_list.append(image_name)
            
    images_list.pop(0)
    
    return images_list



def s3_images_color_list():

    images_list = []

    s3 = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    for obj in s3.list_objects(Bucket="awsradarimages")['Contents']:
        image_name = (obj['Key'])

        if "images_color" in image_name:  
            image_name = image_name.replace("images_color/","")
            images_list.append(image_name)
            
    images_list.pop(0)
    
    return images_list








#print(len(s3_images_color_list()))
#print(len(s3_images_list()))
#print(len(s3_images_small_list()))


"""images_color = s3_images_color_list()
images = s3_images_list()
images_small = s3_images_small_list()

print(images)
print("_________")
print(images_small)
print("_________")
print(images_color)
print("_________")



lista_ok = []
lista_nok = []

for image1 in images:
    for image2 in images_small:
        for image3 in images_color:
            if image1 == image2 and image2 == image3:
                lista_ok.append(image1)
            else:
                lista_nok.append(image1)

print (lista_ok)
"""