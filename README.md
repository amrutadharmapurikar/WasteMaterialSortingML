# WasteMaterialSortingML

Update: This project won second place in the engineering category at the Santa Clara County Science Fair!

This project is meant to automatically classify waste and dispose of it appropriately.

This project has 2 parts. 1) Machine learning model to classify trash as recyclable, compostable, or trashable. 2) Mechanical part to throw away the trash in the correct bin after classification.

Steps:
1) take videos of different trash items
2) use ffmpeg to split the videos into images
3) feed images to a neural network model
4) improve model
