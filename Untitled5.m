img = imread('Images\compteur4.jpg');

img=rgb2gray(img);

img = img(100:200,100:660);

imshow(img);