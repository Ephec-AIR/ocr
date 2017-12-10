function [fl re] = splitLines(imageIn)
%fl => first Line
%re => restant
imageIn = cropImage(imageIn);
%On récupère notre image découpée

row = size(imageIn,1);
% On récupère le nombre de rangées

for s = 1 : row %Pour chaque rangée
    if sum(imageIn(s,:)) == 0   %Si c'est il y a une interligne
        %On est entre 2 lignes
        nm = imageIn(1 : s-1,1 : end);%On récupère la 1ère ligne
        rm = imageIn(s : end , 1:end);%On récupère le reste de la matrice avec els autres lignes
        fl = cropImage(nm);
        re = cropImage(rm); 
        break
    else %Si il n'y a que 1 ligne
        fl=~imageIn;
        re = [];
    end
end