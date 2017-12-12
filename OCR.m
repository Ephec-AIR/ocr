clear all; close all; clc;

warning('off','images:initSize:adjustingMag');
warning('off','images:im2bw:binaryInput');
warning('off','MATLAB:colon:nonIntegerIndex');

img = imread('Images\compteur4.jpg');
figure;imshow(img);
title("Image original");

img = binarizeImage(img,0.5);

%erosion
se = strel('square', 1);
img = imerode(img, se);

%filtre mmoyeneur pour supprimer le bruit
%img = medfilt2(img);

figure;
imshow(img);
title("apres erosion");


img = labelAreaClean(img, 1, 3);

figure;imshow(img);
title("Premier nettoyage");

%=============================================================================
img2 = imbinarize(img);
img2 = labelAreaClean(img2, -1, 1);

figure;imshow(img2);
title("Deuxi�me nettoyage");

%============================================================================
img2 = findAlignementAndCrop(img2); 
figure;imshow(img2);
title("recadrage");


result = readEachComponent(img2);

function [croppedImg] = crop(img, X, Y, W, H)
    croppedImg = img(Y : Y+H, X : X+W);
end
function img = findAlignementAndCrop(img)
    [labels, nbObj] = bwlabel(img);
    props = regionprops(img,'basic');
    
     yTreshMin = size(img, 1)/4;
     yTreshMax = size(img, 1)*3/4;
     
     avgY = 0;
     avgHeight = 0;
     counter = 0;

    for o = 1 : nbObj
        if((props(o).BoundingBox(2)> yTreshMin) && (props(o).BoundingBox(2) < yTreshMax))
            avgY =  avgY + props(o).BoundingBox(2);
            avgHeight = avgHeight + props(o).BoundingBox(4);
            counter = counter + 1;
        end
    end
    yAl = round(avgY/counter);
    avgH = round(avgHeight/counter);
    
    img = crop(img, 10, yAl-120, 700, avgH + 120);
end
function result = readEachComponent(img)

    [labels,nbObj] = bwlabel(img);
    result =[];

    for i = 1:nbObj

        [row col] = find(labels == i);

        el = img(min(row):max(row),min(col):max(col));

        img_resize = imresize(el,[42 24]);
        se2 = strel('disk', 2);
        img_resize = imerode(img_resize, se2);

        [res acc] = readNumber(img_resize);

         figure;imshow(img_resize); 
         %pause(0.5);

        if ~isnan(res)
            result = [result res];
        end
    end
    disp(result);
end
function [binaryImg] = binarizeImage(img,tresh)

    img = imgaussfilt(img,2);

    if size(img,3)==3 %RGB image
        img=rgb2gray(img);
    end

    figure;imshow(img);
    title("Image gris");
    img=imadjust(img);


    T = adaptthresh(img, tresh);
    binaryImg = imbinarize(img, T);
    figure;imshow(binaryImg);
    title("Image binaris�e");
end
function [cleanedImg] = labelAreaClean(img, deleteSmall, quotientArea)
   
    [labels, nbObj] = bwlabel(img);
    props = regionprops(img,'basic');
    avg = 0;

    % moyenne des surfaces
    for o = 1 : nbObj
        avg =  avg + props(o).Area;
    end
    avg = round((avg/nbObj)*quotientArea);
    
    % doit on supprimer les obetjs plus grand ou plus petit que la surface
    % moyenne 
    if(deleteSmall < 0)
        cleanedImg = bwareaopen(img,avg);
    else
        cleanedImg = img - bwareaopen(img,avg);
    end
end
