%-------------------------------------------------------------------------
% obj2catt v0.1
%-------------------------------------------------------------------------
% Converter 3D geometry from *.obj to *.geo to CATT ACOUSTIC Software
%-------------------------------------------------------------------------
% Author: Victor Espinoza, Eng.
% Santiago, Chile. 2009
%-------------------------------------------------------------------------
%edited for TUCT2 by Seth Hollandsworth, 2017

clear;clc
recfile='C:\Users\Seth\Documents\St. Paul''s Cross Project\Church Models\IN\rec.loc';% filename of receiver data
sourfile='C:\Users\Seth\Documents\St. Paul''s Cross Project\Church Models\OUT\src.loc';% filename of source data
masterfile=input('Filename of *GEO ? ','s');% Ask for filename *.geo
masterfile=['C:\Users\Seth\Documents\St. Paul''s Cross Project\Church Models\IN\' masterfile '.geo'];

%filename of  *.obj (include folder an subfolders)
objectFile='C:\Users\Seth\Documents\St. Paul''s Cross Project\Church Models\IN\sound model v3.obj';
%change material
title=[';---------------------------------------------------';
    '; obj2catt v0.1                                     ';
    ';---------------------------------------------------';
    '; Converter 3D geometry from *.obj to *.geo to be   ';
    '; used in CATT ACOUSTIC Software                    ';
    ';---------------------------------------------------';
    '; Author: Victor Espinoza, Eng.                     ';
    '; Santiago, Chile. 2009                             ';
    ';---------------------------------------------------';
    '; Edited by Seth Hollandsworth                      ';
    '; Raleigh, NC, USA. 2017                            ';
    '                                                    ';
    '                                                    ';
    'ABS stone = < 13 13 13 13 13 13>                    ';
    'ABS crowd = < 60 60 60 60 60 60>                    ';
    'ABS wood = < 15 15 15 15 15 15>                     ';
    'CORNERS                                             ';
    '                                                    '];

dlmwrite(masterfile, title,'delimiter','','newline', 'pc')
%error check to make sure file opened correctly
startFile = true;
%deletes existing file and writes new one
fid = fopen(objectFile,'r');
%error check for invalid fid
if fid == -1
    startFile = false;
end
nv=0;
vertices=[];
while startFile
    tline = fgetl(fid);
    aux=tline;
    if (not(tline==-1)|not(aux==[]))&aux(1:2)=='v '
        nv=nv+1;
        spaces=find(aux==' ');
        vertices=[num2str(nv) ' ' aux(spaces(1)+1:spaces(2)-1) ' ' aux(spaces(2)+1:spaces(3)-1) ' ' aux(spaces(3)+1:length(aux))];
        vertices = strrep(vertices,'-','');
        dlmwrite(masterfile, vertices,'delimiter','','-append','newline', 'pc');
    end;
    %vertices
    if ~ischar(tline),   break,   end
    %disp(tline)
end
fclose(fid);

dlmwrite(masterfile,' ','delimiter','','-append','newline', 'pc')
dlmwrite(masterfile,'PLANES','delimiter','','-append','newline', 'pc')

fid = fopen(objectFile);
lineNumber=0;
vc=[];
while startFile
    tline = fgetl(fid);
    aux=tline;
    if (~(tline==-1)|~(aux==[]))&aux(1:2)=='f '
        %disp(aux)
        lineNumber=lineNumber+1;
        %disp([num2str(nc) ' ' aux])
        spaces=find(aux==' ');
        for j=1:length(spaces)-1
            aux2=aux(spaces(j)+1:spaces(j+1)-1);
            aux3=['-' aux2];
            slash=find(aux2=='/');
            vc=[vc ' ' aux2(1:slash(1)-1)];
        end;
        planos=vc;
        dlmwrite(masterfile,['[' num2str(lineNumber) ' plane_' num2str(lineNumber) ' / ' planos ' / stone ]' ],'delimiter','','-append','newline', 'pc')
        %        caras=[caras; vc];
        vc=[];
        %pause
    end;
    %%%%%%figure out what this does
    if ~ischar(tline),   break,   end
    %disp(tline)
    
end
fclose(fid);

%Asks if you want to save files REC.LOC and SRC.LOC
aux=input('Save files REC and SRC? (y/n) ','s');
if aux=='y'
    %edit right here to change where the receivers go in the file
    title=[';---------------------------------------------------';
            ';---------------------------------------------------';
            '                                                    ';
            'RECEIVERS                                           ';
            '1 120 45 6                                          '];
    dlmwrite(recfile, title,'delimiter','','newline', 'pc');
    %edit here to change where the sources are and their spectrums
    title=[';---------------------------------------------------';
            ';---------------------------------------------------';
            '                                                    ';
            'SOURCE A0                                           ';
            ' DIRECTIVITY = "OMNI.SD0"                           ';
            ' POS = 122.000 48.000 8.000                         ';
            ' AIMPOS = 1.000 3.000 1.700                         ';
            ' Lp1m_a = < 85.0 88.0 91.0 94.0 97.0 100 : 103 106 >';%put in sources here
            'END                                                 '];
    dlmwrite(sourfile, title,'delimiter','','newline', 'pc');
end;

%close everything just in case
fclose('all');
