from maltego_trx.entities import Person
from maltego_trx.entities import Image
from maltego_trx.maltego import UIM_PARTIAL
from maltego_trx.transform import DiscoverableTransform
import face_recognition
import pathlib
import requests
import os

class ai_image_comparison(DiscoverableTransform):
    """
    Compare two images to determine if they are snapshots of the same person
    """

    @classmethod
    def create_entities(cls, request, response):

        #Download the image and save it locally
        try:
            known_image_path = cls.download_images(request.getProperty("fullImage"), "known_image")
        except:
            response.addUIMessage("Check if the link provided is valid. The link should point to a PNG or JPG image.")

        try:
            #Invoke the compare_images function and if a match exists, create the entities
            (image_url, name) = cls.compare_images(known_image_path)

            # if a matching image is found, return a Person and Image entity
            if name:


            else:
                response.addUIMessage("The person does not match any of the images in the database!")
        except IOError:
            response.addUIMessage("An error occurred fetching the images from the database.", messageType=UIM_PARTIAL)

    # Download the images using the links found in the CSV file
    @staticmethod
    def download_images(image_url, name):
      #code
        return "{}/{}".format(str(pathlib.Path().resolve()), name)


    @staticmethod
    def compare_images(known_image_path):

        known_image = face_recognition.load_image_file(known_image_path)
        known_encoding = face_recognition.face_encodings(known_image)[0]

        with open("{}/missing_cases_db.csv".format(str(pathlib.Path().resolve()))) as f:
            #read all lines from the database

                #face_recognition compare

                if face_recognition.compare_faces([known_encoding], unknown_encoding)[0]:
                    return (image_url, name)
                    break
                else:
                    os.remove(downloaded_image_path)

        return (None, None)


if __name__ == "__main__":
    print(ai_image_comparison.compare_images("test"))
