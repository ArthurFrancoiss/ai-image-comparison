# ai_based_recognition

This is a Maltego transorm. Make sure you have the needed libraries installed. It is preferred you follow the Maltego walkthrough and set the project locally. 

The transform uses Python's face recognition library and the lost children database found in http://www.maltegoctf.org. It compares an Image entity in Maltego will all images in that database. I am trying to find out my own childhood name and history through this transform.

What needs to be added:
1. I need to figure out a way to downlaod the images locally so that tehy can be loaded into the face_recognition funtions
2. I need to figure out how to properly show the result in Maltego entities
