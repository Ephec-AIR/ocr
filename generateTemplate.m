
one=imread('Images\letters_numbers\1.bmp');  two=imread('Images\letters_numbers\2.bmp');
three=imread('Images\letters_numbers\3.bmp');four=imread('Images\letters_numbers\4.bmp');
five=imread('Images\letters_numbers\5.bmp'); six=imread('Images\letters_numbers\6.bmp');
seven=imread('Images\letters_numbers\7.bmp');eight=imread('Images\letters_numbers\8.bmp');
nine=imread('Images\letters_numbers\9.bmp'); zero=imread('Images\letters_numbers\0.bmp');

number=[one two three four five...
    six seven eight nine zero];
templates=mat2cell(number,42,[24 24 24 24 24 24 24 24 24 24]);
save ('templates','templates')