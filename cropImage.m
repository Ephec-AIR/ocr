function newImage = cropImage(image)
%isLogical v�rifie si son param�tre contient des valeurs binaires soit 0 et
%1
image = imread('Images\TEST_1.JPG');

if ~islogical(image)%si l'image n'a pas �t� binaris�
    image = im2bw(image,0.99); %On binarise l'image
    %figure;imshow(image);
end

a = ~image;
%figure;imshow(a);
%Contient l'image binaris�e inverse(0-> 1 et 1-> 0)

[f c] = find(a);
%find => Renvoie une matrice dont les valeurs sont les colonnes et lignes
%o� la valeur 1 � �t� trouv�e.

maxCol = max(c); minCol = min(c);
%On cherche les bornes verticales de notre image
maxFloor = max(f); minFloor = min(f);
%On cherhce les bornes horizontales de notre image

newImage = a(minFloor : maxFloor, minCol : maxCol);
%On renvoie l'image born�e