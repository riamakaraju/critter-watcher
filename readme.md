# Squirrel Watcher
The Squirrel Watcher is a program that helps detect the presence of squirrels through images. This detection can help pet owners to make sure their pets are inside when a squirrel is present to prevent their pets from running off.
image description

## The Algorithm
The algorithm runs on Resnet-19, a machine learning framwoek from Pytorch. Specifically, it uses imagenet to classify images, having over 1000 objects that it can classify an image as. If the image that user uploads is detected as a type of squirrel, the user recieves a message alerting them that a squirrel has been spotted.

## Running this project
1) Log into your Nano through SSH on VS Code.
2) From Github, download the Squirrel Watcher folder and upload it into the Nvidia folder on VS Code.
3) In this folder, upload any jpg file or rename an image file by adding ".jpg" at the end of it.
4) Create a new terminal and type "python3 squirrel-watch.py (image_file_name_here)" and press enter.
video explanation
