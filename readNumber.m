function [number accuracy] = readNumber( img )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

load templates;

comp = [];

for n=1:11
    
    sem=corr2(templates{1,n},img);
    
    comp=[comp sem];

    
end
accuracy = max(comp);
vd=find(comp==max(comp));
%*-*-*-*-*-*-*-*-*-*-*-*-*-
%if accuracy >= 0.5
 if accuracy >= 0.3
    if vd==1
        number='1';
    elseif vd==2
        number = '1';
    elseif vd==3
        number='2';
    elseif vd==4
        number='3';
    elseif vd==5
        number='4';
    elseif vd==6
        number='5';
    elseif vd==7
        number='6';
    elseif vd==8
        number='7';
    elseif vd==9
        number='8';
    elseif vd==10
        number='9';
    elseif vd==11
        number='0';
    else
        number = NaN;
    end
else
    number = NaN;
end



end

