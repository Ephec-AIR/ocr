function [ result ] = ocrReader( minH,maxH,minW,maxW,pathFile )

img = imread(pathFile);

iRed = find(img(:,:,1)<185);
iGreen = find(img(:,:,2)<185);
iBlue = find(img(:,:,3)<185);


img(iRed) = 0;
img(iGreen) = 0;
img(iBlue) = 0;


img = img(minH:maxH,minW:maxW);

result = [];

if size(img,3)==3 %RGB image
    img=rgb2gray(img);
end

tresh = graythresh(img);

img = ~im2bw(img,tresh);

[Lab nbConn] = bwlabel(~img);

for i = 1:nbConn
    [row col] = find(Lab == i);
    
    el = img(min(row):max(row),min(col):max(col));
    
    img_resize = imresize(el,[42 24]);
    
    img_resize = bwmorph(img_resize,'thicken');
    
    [res acc] = readNumber(~img_resize);
    
    %disp(i);
    %imshow(img_resize);
    %disp(corr2(imread('Images\letters_numbers\3.bmp'),~img_resize));pause(1);
    
    if ~isnan(res)
        result = [result res];
    end
   
end

end

