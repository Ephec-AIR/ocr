  img = imread('Images\compteur4.jpg');
  
   figure;imshow(img);
   title("Image original");
%     
% %     img = imgaussfilt(img,1);
% %     img=rgb2gray(img);
%     
%     figure;imshow(img);
%     title("Image gris");
%     
%     tresh = graythresh(img);
%     img = im2bw(img);
%     
%     figure;imshow(img);
%     title("Image binarisée");

    img = binarizeImage(img,0.5);
    
    [labels, nbObj] = bwlabel(img);
    props = regionprops(img,'basic');

    avg = 0;
    for o = 1 : nbObj
       avg =  avg + props(o).Area;
    end

    avg = round(avg/nbObj);
    avg = round(avg);

    img = img - bwareaopen(img,avg);
    
    %figure;imshow(img);
    %title("Premier nettoyage");

    %=============================================================================
    img2 = im2bw(img);


    [labels2,nbObj2] = bwlabel(img2);

    props2 = regionprops(img2,'basic');

    avg2 = 0;
    avgCenter = 0;
    avgSize = 0
    for o = 1 : nbObj2

       avg2 =  avg2 + props2(o).Area;
       avgCenter = avgCenter + props2(o).Centroid(2);
       avgSize =  avgSize + props2(o).BoundingBox(4);

    end

    avg2 = round(avg2/nbObj2);

    avgCenter = round(avgCenter/nbObj2);

    avgCenterTop = avgCenter - avgSize/2;
    
    avgCenterBot = avgCenter + avgSize/2;

    avg2 = round(avg2/2);

    img2 = bwareaopen(img2,avg2);
    
    figure;imshow(img2);
    title("Deuxième nettoyage");
    
    wImage = size(img2,1);

    img2 = img2(avgCenterTop : avgCenterBot, 1 : wImage);
    
    figure;imshow(img2);
    title("Recadrage");
  
    %============================================================================
    imgF = img2;

    [labelsF,nbObjF] = bwlabel(imgF);

    propsF = regionprops(imgF,'basic');

    result =[];

    for i = 1:nbObjF

        [row col] = find(labelsF == i);

        el = imgF(min(row):max(row),min(col):max(col));

        img_resize = imresize(el,[42 24]);

        [res acc] = readNumber(img_resize);



        disp(res);
        disp(acc);

        if ~isnan(res)
            result = [result res];
        end

    end
end

function [binaryImg] = binarizeImage(img,tresh)
    img = imgaussfilt(img,2);
    img=rgb2gray(img);
    figure;imshow(img);
    title("Image gris");
    %img=imsharpen(img);
    %img=imadjust(img);
    %tresh = graythresh(img);
    %image = im2bw(img);
    
    T = adaptthresh(img, tresh);
    binaryImg = imbinarize(img, T);
    figure;imshow(binaryImg);
    title("Image binarisée");