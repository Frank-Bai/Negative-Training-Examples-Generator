## Negative Training Examples Generator

### Introduction 
A large number of negative training examples are needed in computer vision, and they are also widely used as background images behind a positive image of object for researchers to fabricate more data.

### This Python script
uses a source image and corps it into smaller images of unified size determined by user to create a lot of negative training examples.

### How-to 
* Prepare [OpenCV Library](http://opencv.org/downloads.html), [Numpy Library](http://www.numpy.org/) and of course [Python 2.x or 3.x](https://www.python.org/downloads/).
* Prepare a source image (preferably a high-resolution one) that contains ZERO positive object and its path.
* Open the .py file and enter the information as prompted, including 
    * the path of the source image
    * the width and height of the ouput small images
* Images are prepared in folder *out* under the root folder after a `done` is printed. 

## BE CAREFUL !
**Make sure that the number of output images is not too large to avoid the lack of RAM.**