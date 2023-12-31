#!/usr/bin/env python3
#
# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#

from jetson_inference import imageNet
from jetson_utils import loadImage

import argparse


# parse the command line
parser = argparse.ArgumentParser()

parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be:  googlenet, resnet-18, ect.")
args = parser.parse_args()

# load an image (into shared CPU/GPU memory)
img = loadImage(args.filename)
# load the recognition network
net = imageNet(args.network)
# classify the image
class_idx, confidence = net.Classify(img)
# find the object description
class_desc = net.GetClassDesc(class_idx)

sureness = str(confidence*100)

# print out the result
if (class_desc == "fox squirrel, eastern fox squirrel, Sciurus niger"):
    print("\nSquirrel alert! (: We are " + sureness + " percent sure...")
elif (class_desc == "wood rabbit, cottontail, cottontail rabbit"):
    print("\nA bunny has been spotted! Please be careful with your pets! We are " + sureness + " percent sure...")
elif (class_desc == "robin, American robin, Turdus migratorius"):
    print("\nThere is a robin nearby! We are " + sureness + " percent sure about this.")
elif (class_desc == "jay"):
    print("\nThere is a gorgeous jay nearby. Please be careful with your pets. We are " + sureness + " of it's presence.")
elif (class_desc == "house finch, linnet, Carpodacus mexicanus"):
    print("\nFinch alert!!! We are " + sureness + " percent sure there is one nearby.")
