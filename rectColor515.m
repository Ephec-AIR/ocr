I = imread('flowers.tif');
figure,imshow(I)

%Pour la couche 2 et 3
for i=2:3
    for y = 1:400
        for x = 1:400
            %Je les mets à 0
            I(x,y,i) = 0;
        end
    end
end

figure,imshow(I);

I = imread('flowers.tif');


%Pour la couche 2 et 3
for i=1:2:3
    for y = 1:400
        for x = 1:400
            %Je les mets à 0
            I(x,y,i) = 0;
        end
    end
end

figure,imshow(I);


I = imread('flowers.tif');


%Pour la couche 2 et 3
for i=1:2
    for y = 1:400
        for x = 1:400
            %Je les mets à 0
            I(x,y,i) = 0;
        end
    end
end

figure,imshow(I);


I = imread('flowers.tif');





for y = 1:400
    for x = 1:400
      %Je les mets à 0
      I(x,y,3) = 0;
    end
 end



figure,imshow(I);
I = imread('flowers.tif');

for y = 1:400
    for x = 1:400
      %Je les mets à 0
      I(x,y,2) = 0;
    end
 end



figure,imshow(I);
I = imread('flowers.tif');

for y = 1:400
    for x = 1:400
      %Je les mets à 0
      I(x,y,1) = 0;
    end
 end



figure,imshow(I);

I = imread('flowers.tif');

info = imfinfo('flowers.tif');

r = I(info.Height,info.Width,1);
g = I(info.Height,info.Width,2);
b = I(info.Height,info.Width,3);

for i = 1:3
    for y = 1:400
        for x = 1:400
            if i == 1         
            I(x,y,i) = r;
            elseif i == 2
                 I(x,y,i) = g;
            elseif i == 3
                 I(x,y,i) = b;   
            end     
        end
    end
end

figure,imshow(I);








            