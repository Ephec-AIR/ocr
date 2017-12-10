clc; close all; clear all;

img = imread('Images/TEST_1.JPG');

if size(img,3) == 3 %Si c'est une image RGB
    img = rgb2gray(img);
end

tresh = graythresh(img);%Seuil global de l'image via la m�thode de Otsu
img = ~im2bw(img,tresh);

img = bwareaopen(img,30);%Nettoie l'image des objets plus petits que 30px

word = [];%Va contenir la phrase
re = img;%Copie de l'image

fId = fopen("text.txt","wt");%OUvre un fichier en mode �criture pourn oter la r�ponse

load templates;
global templates;

%Je r�cup�re mes 36 caract�res
% 2 car j'ai 36 colonnes sur 1 ligne
nbLetters = size(templates,2);
%Je commence le traitement
while 1
    %Je r�cup�re les lignes de mon texte
    [fL re] = splitLines(re);
    
    
    if isempty(re)
        break
    end
end

