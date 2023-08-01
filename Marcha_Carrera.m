close all
clear all
clc
%% COORDENADAS
%CABEZA
xcabeza=0;
ycabeza=20;
zcabeza=5;
%CUELLO
xcuello=0;
ycuello=18;
zcuello=5;
%HOMBRO
xhombrod=2;
yhombrod=17.6;
zhombrod=5;
xhombroi=-2;
yhombroi=17.6;
zhombroi=5;
%CENTRO
xcentro=0;
ycentro=16;
zcentro=5;
%CODO
xcodod=2;
ycodod=15;
zcodod=5;
xcodoi=-2;
ycodoi=15;
zcodoi=5;
%MUNECA
xmunecad=2;
ymunecad=13;
zmunecad=5;
xmunecai=-2;
ymunecai=13;
zmunecai=5;
%CENTRO CADERA
xcadera=0;
ycadera=13;
zcadera=5;
%CADERA
xcaderai=-1.5;
ycaderai=12;
zcaderai=5;
xcaderad=1.5;
ycaderad=12;
zcaderad=5;
%RODILLA
xrodillad=1.5;
yrodillad=9;
zrodillad=5;
xrodillai=-1.5;
yrodillai=9;
zrodillai=5;
%TOBILLO
xtobillod=1.5;
ytobillod=6;
ztobillod=5;
xtobilloi=-1.5;
ytobilloi=6;
ztobilloi=5;
%PIES
xpied=1.5;
ypied=5.5;
zpied=6;
xpiei=-1.5;
ypiei=5.5;
zpiei=6;
%TALONES
xtalond=1.5;
ytalond=5.5;
ztalond=4.5;
xtaloni=-1.5;
ytaloni=5.5;
ztaloni=4.5;
%REFERENCIA
xref = 8;
yref = 5.5;
zref = 5;
%% VECTORES
X=[xref,xcabeza,xcuello,xhombrod,xhombroi,xcodod,xcodoi,xmunecad,xmunecai,xcadera,xcaderad,xcaderai,xrodillad,xrodillai,xtobillod,xtobilloi,xtalond,xtaloni,xpied,xpiei];
Y=[yref,ycabeza,ycuello,yhombrod,yhombroi,ycodod,ycodoi,ymunecad,ymunecai,ycadera,ycaderad,ycaderai,yrodillad,yrodillai,ytobillod,ytobilloi,ytalond,ytaloni,ypied,ypiei];
Z=[zref,zcabeza,zcuello,zhombrod,zhombroi,zcodod,zcodoi,zmunecad,zmunecai,zcadera,zcaderad,zcaderai,zrodillad,zrodillai,ztobillod,ztobilloi,ztalond,ztaloni,zpied,zpiei];
%% CARACTERISTICAS DE LA GRAFICA
figurab=figure;
title ('ESQUELETO')
grid on
hold on
xlabel('x')
ylabel('y')
zlabel('z')
drawnow
axis equal
%% MARCAR PUNTOS
%REFERENCIA
plot3(zref,xref,yref,'*m','linewidth',5);
%CABEZA
plot3(zcabeza,xcabeza,ycabeza,'*b','lineWidth',5);
%CUELLO
plot3(zcuello,xcuello,ycuello,'*b','lineWidth',5);
%HOMBROS
plot3(zhombrod,xhombrod,yhombrod,'*b','lineWidth',5);
plot3(zhombroi,xhombroi,yhombroi,'*b','lineWidth',5);
%CENTRO
plot3(zcentro,xcentro,ycentro,'*r','lineWidth',5);
%CODOS
plot3(zcodod,xcodod,ycodod,'*b','lineWidth',5);
plot3(zcodoi,xcodoi,ycodoi,'*b','lineWidth',5);
%MUNECAS
plot3(zmunecad,xmunecad,ymunecad,'*b','lineWidth',5);
plot3(zmunecai,xmunecai,ymunecai,'*b','lineWidth',5);
%CENTROCADERA
plot3(zcadera,xcadera,ycadera,'*b','lineWidth',5);
%RODILLAS
plot3(zrodillad,xrodillad,yrodillad,'*b','lineWidth',5);
plot3(zrodillai,xrodillai,yrodillai,'*b','lineWidth',5);
%TOBILLOS
plot3(ztobillod,xtobillod,ytobillod,'*b','lineWidth',5);
plot3(ztobilloi,xtobilloi,ytobilloi,'*b','lineWidth',5);
%CADERA
plot3(zcaderad,xcaderad,ycaderad,'*b','lineWidth',5);
plot3(zcaderai,xcaderai,ycaderai,'*b','lineWidth',5);
%PIES
plot3(zpied,xpied,ypied,'*b','lineWidth',5);
plot3(zpiei,xpiei,ypiei,'*b','lineWidth',5);
%TALONES
plot3(ztalond,xtalond,ytalond,'*b','lineWidth',5);
plot3(ztaloni,xtaloni,ytaloni,'*b','lineWidth',5);
%% CONEXION PUNTOS
%CABEZA-CUELLO
line([zcabeza zcuello],[xcabeza xcuello],[ycabeza
ycuello],'color','b','lineWidth',2.5)
%CUELLO-HOMBROS
line([zcuello zhombrod],[xcuello xhombrod],[ycuello yhombrod],'color','b','lineWidth',2.5)
line([zcuello zhombroi],[xcuello xhombroi],[ycuello yhombroi],'color','b','lineWidth',2.5)
%HOMBROS-CODOS
line([zhombrod zcodod],[xhombrod xcodod],[yhombrod ycodod],'color','b','lineWidth',2.5)
line([zhombroi zcodoi],[xhombroi xcodoi],[yhombroi ycodoi],'color','b','lineWidth',2.5)
%CODOS-MUNECAS
line([zcodod zmunecad],[xcodod xmunecad],[ycodod
ymunecad],'color','b','lineWidth',2.5)
line([zcodoi zmunecai],[xcodoi xmunecai],[ycodoi
ymunecai],'color','b','lineWidth',2.5)
%CUELLO-CENTRO
line([zcuello zcentro],[xcuello xcentro],[ycuello
ycentro],'color','b','lineWidth',2.5)
%CENTRO-CADERA
line([zcentro zcadera],[xcentro xcadera],[ycentro
ycadera],'color','b','lineWidth',2.5)
%CENTRO-CADERAS
line([zcadera zcaderai],[xcadera xcaderai],[ycadera ycaderai],'color','b','lineWidth',2.5)
line([zcadera zcaderad],[xcadera xcaderad],[ycadera ycaderad],'color','b','lineWidth',2.5)
%CADERA-RODILLAS
line([zcaderad zrodillad],[xcaderad xrodillad],[ycaderad yrodillad],'color','b','lineWidth',2.5)
line([zcaderai zrodillai],[xcaderai xrodillai],[ycaderai yrodillai],'color','b','lineWidth',2.5)
%RODILLAS-TOBILLOS
line([zrodillad ztobillod],[xrodillad xtobillod],[yrodillad ytobillod],'color','b','lineWidth',2.5)
line([zrodillai ztobilloi],[xrodillai xtobilloi],[yrodillai ytobilloi],'color','b','lineWidth',2.5)
%TOBILLOS-TALONES
line([ztalond ztobillod],[xtalond xtobillod],[ytalond ytobillod],'color','b','lineWidth',2.5)
line([ztaloni ztobilloi],[xtaloni xtobilloi],[ytaloni ytobilloi],'color','b','lineWidth',2.5)
%TOBILLOS-PIES
line([ztobillod zpied],[xtobillod xpied],[ytobillod ypied],'color','b','lineWidth',2.5)
line([ztobilloi zpiei],[xtobilloi xpiei],[ytobilloi ypiei],'color','b','lineWidth',2.5)
view([-37.5 -30])
%% LONGITUDES (vectores)
%REFERENCIA
ref=[zref,xref,yref];
%CABEZA
cabeza=[zcabeza,xcabeza,ycabeza];
%CUELLO
cuello=[zcuello,xcuello,ycuello];
%HOMBROS
hombrod=[zhombrod,xhombrod,yhombrod];
hombroi=[zhombroi,xhombroi,yhombroi];
%CENTRO
centro=[zcentro,xcentro,ycentro];
%CODOS
codod=[zcodod,xcodod,ycodod];
codoi=[zcodoi,xcodoi,ycodoi];
%MUNECAS
munecad=[zmunecad,xmunecad,ymunecad];
munecai=[zmunecai,xmunecai,ymunecai];
%CENTROCADERA
centro_cadera=[zcadera,xcadera,ycadera];
%RODILLAS
rodillad=[zrodillad,xrodillad,yrodillad];
rodillai=[zrodillai,xrodillai,yrodillai];
%TOBILLOS
tobillod=[ztobillod,xtobillod,ytobillod];
tobilloi=[ztobilloi,xtobilloi,ytobilloi];
%CADERA
caderad=[zcaderad,xcaderad,ycaderad];
caderai=[zcaderai,xcaderai,ycaderai];
%PIES
pied=[zpied,xpied,ypied];
piei=[zpiei,xpiei,ypiei];
%TALONES
talond=[ztalond,xtalond,ytalond];
taloni=[ztaloni,xtaloni,ytaloni];
%% LONGITUD
%CUELLO
longc=cabeza-cuello;
lngcuello=norm(longc);
%HOMBROS
lnghd=cuello-hombrod;
lnghombrod=norm(lnghd);
lnghi=cuello-hombroi;
lnghombroi=norm(lnghi);
%BRAZOS
lngbd=hombrod-codod;
lngbrazod=norm(lngbd);
lngbi=hombroi-codoi;
lngbrazoi=norm(lngbi);
%ANTEBRAZO
lngantd=codod-munecad;
lngantebrazod=norm(lngantd);
lnganti=codoi-munecai;
lngantebrazoi=norm(lnganti);
%TORZO
lngt=cuello-centro_cadera;
lngtrozo=norm(lngt);
%CADERA
lngcd=centro_cadera-caderad;
lngcaderad=norm(lngcd);
lngci=centro_cadera-caderai;
lngcaderai=norm(lngci);
%PIERNAS
lngpd=caderad-rodillad;
lngpiernad=norm(lngpd);
lngpi=caderai-rodillai;
lngpiernai=norm(lngpi);
%PANTORRILLA
lngpand=rodillad-tobillod;
lngpantorrillad=norm(lngpand);
lngpani=rodillai-tobilloi;
lngpantorrillai=norm(lngpani);
%PIES
lngpid=talond-pied;
lngpied=norm(lngpid);
lngpii=taloni-piei;
lngpiei=norm(lngpii);
hold off
%% PARTE 1
figura2=figure
title ('MARCHA')
grid on
hold on
xlabel('x')
ylabel('y')
zlabel('z')
drawnow
axis equal
%CAMBIO DE PUNTOS
%abduccion_x = 0:1:180;
%abduccion_y= 0:1:90;
abduccion=-44:1:45;
aduccion=45:-1:-44;
%90 Grados
%% Vactores Movimientos Complementarios de Articulaciones
angle_caderaD1 = linspace(30,25,8);
angle_caderaD2 = linspace(25,-10,24);
angle_caderaD3 = linspace(-10,-20,18);
angle_caderaI1 = linspace(-20,-15,7);
angle_caderaI2 = linspace(-15,25,21);
angle_cadeaI3 = linspace(25,30,10);
angle_caderaI4 = linspace(30,30,12);
angle_rodD1 = linspace(0,12,8);
angle_rodD2 = linspace(13,10,24);
angle_rodD3 = linspace(10,30,18);
angle_rodI1 = linspace(30,35,7);
angle_rodI2 = linspace(35,47,21);
angle_rodI3 = linspace(45,24,10);
angle_rodI4 = linspace(22,0,12);
angle_tobD1 = linspace(10,15,8);
angle_tobD2 = linspace(15,0,24);
angle_tobD3 = linspace(0,11,18);
angle_tobI1 = linspace(12,20,7);
angle_tobI2 = linspace(20,-4,21);
angle_tobI3 = linspace(-3,3,10);
angle_tobI4 = linspace(4,10,12);
angle_mano_ad1 = linspace(0,30,25);
angle_mano_ad2 = linspace(30,0,25);
angle_mano_atras1 = linspace (0,-25,25);
angle_mano_atras2 = linspace(-25,0,25);
mov=linspace(.1,.76,100);
MovCad = [angle_caderaD1 angle_caderaD2 angle_caderaD3 angle_caderaI1 angle_caderaI2 angle_cadeaI3 angle_caderaI4];
MovCad_Comp = [angle_caderaI1 angle_caderaI2 angle_cadeaI3 angle_caderaI4 angle_caderaD1 angle_caderaD2 angle_caderaD3];
MovRod = [angle_rodD1 angle_rodD2 angle_rodD3 angle_rodI1 angle_rodI2 angle_rodI3 angle_rodI4];
MovRod_Comp = [angle_rodI1 angle_rodI2 angle_rodI3 angle_rodI4 angle_rodD1 angle_rodD2 angle_rodD3];
MovTob = [angle_tobI2 angle_tobI3 angle_tobI4 angle_tobD1 angle_tobD2 angle_tobD3 angle_tobI1];
MovTob_Comp = [angle_tobD2 angle_tobD3 angle_tobI1 angle_tobI2 angle_tobI3 angle_tobI4 angle_tobD1];
MovMano = [angle_mano_atras2, angle_mano_ad1,angle_mano_ad2, angle_mano_atras1];
%%
for i = 1 :length(MovCad)
%hold on
ycodod = yhombrod - (lngbrazod*cosd(-MovMano(i))); %yhombrod - (lngbrazod*sind(90));
zcodod = zhombrod - (lngbrazod*sind(-MovMano(i)));
ycodoi = yhombroi - (lngbrazoi*cosd(MovMano(i)));
%yhombrod - (lngbrazod*sind(90));
zcodoi = zhombroi - (lngbrazoi*sind(MovMano(i)));
ymunecad = ycodod - (lngantebrazod*cosd(-MovMano(i)-30)); %ycodod -(lngantebrazod*sind(90));
zmunecad = zcodod - (lngantebrazod*sind(-MovMano(i)-30));
ymunecai = ycodoi -(lngantebrazoi*cosd(MovMano(i)-30)); %ycodod -(lngantebrazod*sind(90));
zmunecai = zcodoi -(lngantebrazoi*sind(MovMano(i)-30));
yrodillai = ycaderai -(lngpiernai*cosd(MovCad(i)));
zrodillai = zcaderai -(lngpiernai*sind(MovCad(i)));
yrodillad = ycaderad -(lngpiernad*cosd(MovCad_Comp(i)));
zrodillad = zcaderad -(lngpiernad*sind(MovCad_Comp(i)));
ytobilloi = yrodillai -(lngpantorrillai*cosd(MovRod_Comp(i)));
ztobilloi = zrodillai -(lngpantorrillai*sind(MovRod_Comp(i)));
ytobillod = yrodillad -(lngpantorrillad*cosd(MovRod(i)));
ztobillod = zrodillad -(lngpantorrillad*sind(MovRod(i)));
ytaloni = ytobilloi -(lngpiei*cosd(MovTob(i)-45));
ztaloni = ztobilloi -(lngpiei*sind(MovTob(i)-45));
ytalond = ytobillod -(lngpied*cosd(MovTob_Comp(i)-45));
ztalond = ztobillod -(lngpied*sind(MovTob_Comp(i)-45));
ypiei = ytobilloi - (0.8*cosd(MovTob_Comp(i)));
zpiei = ztobilloi - (0.8*sind(MovTob_Comp(i)));
ypied = ytobillod - (0.8*cosd(MovTob(i)));
zpied = ztobillod - (0.8*sind(MovTob(i)));
zcabeza= mov(i)+ zcabeza;
zcuello= mov(i)+zcuello;
zhombrod= mov(i)+zhombrod;
zhombroi= mov(i)+zhombroi;
zcentro= mov(i)+zcentro;
zcodod= mov(i)+zcodod;
zcodoi= mov(i)+zcodoi;
zmunecad=mov(i)+zmunecad;
zmuencai=mov(i)+zmunecai;
zcadera=mov(i)+zcadera;
zrodillad=mov(i)+zrodillad;
zrodillai=mov(i)+zrodillai;
ztobillod=mov(i)+ztobillod;
ztonilloi=mov(i)+ztobilloi;
zcaderad=mov(i)+zcaderad;
zcaderai=mov(i)+zcaderai;
zpied=mov(i)+zpied;
zpiei=mov(i)+zpiei;
ztalond=mov(i)+ztalond;
ztaloni=mov(i)+ztaloni;
%MARCAR PUNTOS
%REFERENCIA
plot3(zref,xref,yref,'*m','linewidth',5);
%CABEZA
plot3(zcabeza,xcabeza,ycabeza,'*b','lineWidth',5);
%CUELLO
plot3(zcuello,xcuello,ycuello,'*b','lineWidth',5);
%HOMBROS
plot3(zhombrod,xhombrod,yhombrod,'*b','lineWidth',5);
plot3(zhombroi,xhombroi,yhombroi,'*b','lineWidth',5);
%CENTRO
plot3(zcentro,xcentro,ycentro,'*r','lineWidth',5);
%CODOS
plot3(zcodod,xcodod,ycodod,'*b','lineWidth',5);
plot3(zcodoi,xcodoi,ycodoi,'*b','lineWidth',5);
%MUNECAS
plot3(zmunecad,xmunecad,ymunecad,'*b','lineWidth',5);
plot3(zmunecai,xmunecai,ymunecai,'*b','lineWidth',5);
%CENTROCADERA
plot3(zcadera,xcadera,ycadera,'*b','lineWidth',5);
%RODILLAS
plot3(zrodillad,xrodillad,yrodillad,'*b','lineWidth',5);
plot3(zrodillai,xrodillai,yrodillai,'*b','lineWidth',5);
%TOBILLOS
plot3(ztobillod,xtobillod,ytobillod,'*b','lineWidth',5);
plot3(ztobilloi,xtobilloi,ytobilloi,'*b','lineWidth',5);
%CADERA
plot3(zcaderad,xcaderad,ycaderad,'*b','lineWidth',5);
plot3(zcaderai,xcaderai,ycaderai,'*b','lineWidth',5);
%PIES
plot3(zpied,xpied,ypied,'*b','lineWidth',5);
plot3(zpiei,xpiei,ypiei,'*b','lineWidth',5);
%TALONES
plot3(ztalond,xtalond,ytalond,'*b','lineWidth',5);
plot3(ztaloni,xtaloni,ytaloni,'*b','lineWidth',5);
%CABEZA-CUELLO
line([zcabeza zcuello],[xcabeza xcuello],[ycabeza
ycuello],'color','b','lineWidth',2.5)
%CUELLO-HOMBROS
line([zcuello zhombrod],[xcuello xhombrod],[ycuello yhombrod],'color','b','lineWidth',2.5)
line([zcuello zhombroi],[xcuello xhombroi],[ycuello yhombroi],'color','b','lineWidth',2.5)
%HOMBROS-CODOS
line([zhombrod zcodod],[xhombrod xcodod],[yhombrod ycodod],'color','b','lineWidth',2.5)
line([zhombroi zcodoi],[xhombroi xcodoi],[yhombroi ycodoi],'color','b','lineWidth',2.5)
%CODOS-MUNECAS
line([zcodod zmunecad],[xcodod xmunecad],[ycodod
ymunecad],'color','b','lineWidth',2.5)
line([zcodoi zmunecai],[xcodoi xmunecai],[ycodoi
ymunecai],'color','b','lineWidth',2.5)
%CUELLO-CENTRO
line([zcuello zcentro],[xcuello xcentro],[ycuello
ycentro],'color','b','lineWidth',2.5)
%CENTRO-CADERA
line([zcentro zcadera],[xcentro xcadera],[ycentro
ycadera],'color','b','lineWidth',2.5)
%CENTRO-CADERAS
line([zcadera zcaderai],[xcadera xcaderai],[ycadera ycaderai],'color','b','lineWidth',2.5)
line([zcadera zcaderad],[xcadera xcaderad],[ycadera ycaderad],'color','b','lineWidth',2.5)
%CADERA-RODILLAS
line([zcaderad zrodillad],[xcaderad xrodillad],[ycaderad yrodillad],'color','b','lineWidth',2.5)
line([zcaderai zrodillai],[xcaderai xrodillai],[ycaderai yrodillai],'color','b','lineWidth',2.5)
%RODILLAS-TOBILLOS
line([zrodillad ztobillod],[xrodillad xtobillod],[yrodillad ytobillod],'color','b','lineWidth',2.5)
line([zrodillai ztobilloi],[xrodillai xtobilloi],[yrodillai ytobilloi],'color','b','lineWidth',2.5)
%TOBILLOS-TALONES
line([ztalond ztobillod],[xtalond xtobillod],[ytalond ytobillod],'color','b','lineWidth',2.5)
line([ztaloni ztobilloi],[xtaloni xtobilloi],[ytaloni ytobilloi],'color','b','lineWidth',2.5)
%TOBILLOS-PIES
line([ztobillod zpied],[xtobillod xpied],[ytobillod ypied],'color','b','lineWidth',2.5)
line([ztobilloi zpiei],[xtobilloi xpiei],[ytobilloi ypiei],'color','b','lineWidth',2.5)
view([-37.5 -30])
%Longitud del paso
lngpi=zref-zpiei;
lngpd=zref-zpied;
A=num2str(MovCad(i));
B=num2str(MovRod(i));
C=num2str(MovTob(i));
D=num2str(MovMano(i));
text(5+zcadera,xcadera,ycadera,'GRADOS Cadera:')
text(10+zcadera,.5-xcadera,ycadera,A)
text(zrodillad+5,xrodillad,yrodillad,'GRADOS Rodilla:')
text(10+zrodillad,.5+zrodillad,yrodillad,B)
text(5+ztobillod,xtobillod,ytobillod,'GRADOS Tobillo:')
text(10+ztobillod,.5+xtobillod,ytobillod,C)
text(zcodod,10+xcodod,10+ycodod,'GRADOS Mano:')
text(zcodod,10+xcodod,9+ycodod,D)
%grid on;
F1=getframe;
cla
end

hold off
%% VECTORES PARA LA CARRERA
%figura3=figure
title ('CARRERA')
grid on
hold on
xlabel('x')
ylabel('y')
zlabel('z')
drawnow
axis equal
%CAMBIO DE PUNTOS
%abduccion_x = 0:1:180;
%abduccion_y= 0:1:90;
abduccion=-44:1:45;
aduccion=45:-1:-44;
%90 Grados
HIPESF=linspace(-9,55,32);
HIPLSE=linspace(55,45,7);
HIPLPF=linspace(45,50,3);
HIPMSE=linspace(50,15,24);
HIPDOE=linspace(15,-9,4);
KNEEESF=linspace(25,90,22);
KNEELSE=linspace(90,20,23);
KNEELPF=linspace(20,40,7);
KNEEMSF=linspace(40,40,13);
KNEEDOE=linspace(40,25,5);
ANKLEESDF = linspace(20,10,14);
ANKLELSPF = linspace(10,5,7);
ANKLELPDF = linspace(5,20,21);
ANKLEMSDF = linspace(20,30,14);
ANKLEDOPF = linspace(30,20,14);
angle_mano_ad1 = linspace(0,40,18);
angle_mano_ad2 = linspace(40,0,18);
angle_mano_atras1 = linspace (0,-35,18);
angle_mano_atras2 = linspace(-35,0,18);
mov=linspace(.1,.76,70);
MovCad = [HIPESF HIPLSE HIPLPF HIPMSE HIPDOE HIPESF HIPLSE HIPLPF HIPMSE HIPDOE];
MovCad_Comp = [HIPLPF HIPMSE HIPDOE HIPESF HIPLSE HIPLPF HIPMSE HIPDOE HIPESF HIPLSE];
MovRod = [KNEEESF KNEELSE KNEELPF KNEEMSF KNEEDOE KNEEESF KNEELSE KNEELPF KNEEMSF KNEEDOE];
MovRod_Comp =  [KNEELPF KNEEMSF KNEEDOE KNEEESF KNEELSE KNEELPF KNEEMSF KNEEDOE KNEEESF KNEELSE];
MovTob = [ANKLEESDF ANKLELSPF ANKLELPDF ANKLEMSDF ANKLEDOPF ANKLEESDF ANKLELSPF ANKLELPDF ANKLEMSDF ANKLEDOPF];
MovTob_Comp = [ANKLELPDF ANKLEMSDF ANKLEDOPF ANKLEESDF ANKLELSPF ANKLELPDF ANKLEMSDF ANKLEDOPF ANKLEESDF ANKLELSPF];
MovMano = [angle_mano_atras2, angle_mano_ad1, angle_mano_ad2, angle_mano_atras1 angle_mano_atras2, angle_mano_ad1, angle_mano_ad2, angle_mano_atras1 ];
% zcabeza=zcabeza+1;
% ycabeza=ycabeza-.1;
% zcuello=zcuello+.80;
% zhombrod=zhombrod+.70;
% yhombrod=yhombrod-.1;
% zhombri=zhombroi+.70;
% yhombroi=yhombroi-.1;
% zcentro=zcentro+.60;
zcadaera=zcadera+.50;
mov=linspace(.1,.76,140);
for i = 1 :length(MovCad)
%hold on
cla
ycodod = yhombrod - (lngbrazod*cosd(MovMano(i)));
%yhombrod - (lngbrazod*sind(90));
zcodod = zhombrod - (lngbrazod*sind(MovMano(i)));
ycodoi = yhombroi - (lngbrazoi*cosd(-MovMano(i))); %yhombrod - (lngbrazod*sind(90));
zcodoi = zhombroi - (lngbrazoi*sind(-MovMano(i)));
ymunecad = ycodod -(lngantebrazod*cosd(MovMano(i)-30)); %ycodod -(lngantebrazod*sind(90));
zmunecad = zcodod -(lngantebrazod*sind(MovMano(i)-30));
ymunecai = ycodoi - (lngantebrazoi*cosd(-MovMano(i)-30)); %ycodod -(lngantebrazod*sind(90));
zmunecai = zcodoi - (lngantebrazoi*sind(-MovMano(i)-30));
yrodillai = ycaderai -(lngpiernai*cosd(MovCad(i)));
zrodillai = zcaderai -(lngpiernai*sind(MovCad(i)));
yrodillad = ycaderad -(lngpiernad*cosd(MovCad_Comp(i)));
zrodillad = zcaderad -(lngpiernad*sind(MovCad_Comp(i)));
ytobilloi = yrodillai -(lngpantorrillai*cosd(MovRod_Comp(i)));
ztobilloi = zrodillai -(lngpantorrillai*sind(MovRod_Comp(i)));
ytobillod = yrodillad -(lngpantorrillad*cosd(MovRod(i)));
ztobillod = zrodillad -(lngpantorrillad*sind(MovRod(i)));
ytaloni = ytobilloi -(lngpiei*cosd(MovTob(i)-45));
ztaloni = ztobilloi -(lngpiei*sind(MovTob(i)-45));
ytalond = ytobillod -(lngpied*cosd(MovTob_Comp(i)-45));
ztalond = ztobillod -(lngpied*sind(MovTob_Comp(i)-45));
ypiei = ytobilloi - (0.8*cosd(MovTob_Comp(i)));
zpiei = ztobilloi - (0.8*sind(MovTob_Comp(i)));
ypied = ytobillod - (0.8*cosd(MovTob(i)));
zpied = ztobillod - (0.8*sind(MovTob(i)));
zcabeza= mov(i)+ zcabeza;
zcuello= mov(i)+zcuello;
zhombrod= mov(i)+zhombrod;
zhombroi= mov(i)+zhombroi;
zcentro= mov(i)+zcentro;
zcodod= mov(i)+zcodod;
zcodoi= mov(i)+zcodoi;
zmunecad=mov(i)+zmunecad;
zmuencai=mov(i)+zmunecai;
zcadera=mov(i)+zcadera;
zrodillad=mov(i)+zrodillad;
zrodillai=mov(i)+zrodillai;
ztobillod=mov(i)+ztobillod;
ztonilloi=mov(i)+ztobilloi;
zcaderad=mov(i)+zcaderad;
zcaderai=mov(i)+zcaderai;
zpied=mov(i)+zpied;
zpiei=mov(i)+zpiei;
ztalond=mov(i)+ztalond;
ztaloni=mov(i)+ztaloni;
%MARCAR PUNTOS
%REFERENCIA
plot3(zref,xref,yref,'*m','linewidth',5);
%CABEZA
plot3(zcabeza,xcabeza,ycabeza,'*b','lineWidth',5);
%CUELLO
plot3(zcuello,xcuello,ycuello,'*b','lineWidth',5);
%HOMBROS
plot3(zhombrod,xhombrod,yhombrod,'*b','lineWidth',5);
plot3(zhombroi,xhombroi,yhombroi,'*b','lineWidth',5);
%CENTRO
plot3(zcentro,xcentro,ycentro,'*r','lineWidth',5);
%CODOS
plot3(zcodod,xcodod,ycodod,'*b','lineWidth',5);
plot3(zcodoi,xcodoi,ycodoi,'*b','lineWidth',5);
%MUNECAS
plot3(zmunecad,xmunecad,ymunecad,'*b','lineWidth',5);
plot3(zmunecai,xmunecai,ymunecai,'*b','lineWidth',5);
%CENTROCADERA
plot3(zcadera,xcadera,ycadera,'*b','lineWidth',5);
%RODILLAS
plot3(zrodillad,xrodillad,yrodillad,'*b','lineWidth',5);
plot3(zrodillai,xrodillai,yrodillai,'*b','lineWidth',5);
%TOBILLOS
plot3(ztobillod,xtobillod,ytobillod,'*b','lineWidth',5);
plot3(ztobilloi,xtobilloi,ytobilloi,'*b','lineWidth',5);
%CADERA
plot3(zcaderad,xcaderad,ycaderad,'*b','lineWidth',5);
plot3(zcaderai,xcaderai,ycaderai,'*b','lineWidth',5);
%PIES
plot3(zpied,xpied,ypied,'*b','lineWidth',5);
plot3(zpiei,xpiei,ypiei,'*b','lineWidth',5);
%TALONES
plot3(ztalond,xtalond,ytalond,'*b','lineWidth',5);
plot3(ztaloni,xtaloni,ytaloni,'*b','lineWidth',5);
%CABEZA-CUELLO
line([zcabeza zcuello],[xcabeza xcuello],[ycabeza
ycuello],'color','b','lineWidth',2.5)
%CUELLO-HOMBROS
line([zcuello zhombrod],[xcuello xhombrod],[ycuello yhombrod],'color','b','lineWidth',2.5)
line([zcuello zhombroi],[xcuello xhombroi],[ycuello yhombroi],'color','b','lineWidth',2.5)
%HOMBROS-CODOS
line([zhombrod zcodod],[xhombrod xcodod],[yhombrod ycodod],'color','b','lineWidth',2.5)
line([zhombroi zcodoi],[xhombroi xcodoi],[yhombroi ycodoi],'color','b','lineWidth',2.5)
%CODOS-MUNECAS
line([zcodod zmunecad],[xcodod xmunecad],[ycodod
ymunecad],'color','b','lineWidth',2.5)
line([zcodoi zmunecai],[xcodoi xmunecai],[ycodoi
ymunecai],'color','b','lineWidth',2.5)
%CUELLO-CENTRO
line([zcuello zcentro],[xcuello xcentro],[ycuello
ycentro],'color','b','lineWidth',2.5)
%CENTRO-CADERA
line([zcentro zcadera],[xcentro xcadera],[ycentro
ycadera],'color','b','lineWidth',2.5)
%CENTRO-CADERAS
line([zcadera zcaderai],[xcadera xcaderai],[ycadera ycaderai],'color','b','lineWidth',2.5)
line([zcadera zcaderad],[xcadera xcaderad],[ycadera ycaderad],'color','b','lineWidth',2.5)
%CADERA-RODILLAS
line([zcaderad zrodillad],[xcaderad xrodillad],[ycaderad yrodillad],'color','b','lineWidth',2.5)
line([zcaderai zrodillai],[xcaderai xrodillai],[ycaderai yrodillai],'color','b','lineWidth',2.5)
%RODILLAS-TOBILLOS
line([zrodillad ztobillod],[xrodillad xtobillod],[yrodillad ytobillod],'color','b','lineWidth',2.5)
line([zrodillai ztobilloi],[xrodillai xtobilloi],[yrodillai ytobilloi],'color','r','lineWidth',2.5)
%TOBILLOS-TALONES
line([ztalond ztobillod],[xtalond xtobillod],[ytalond ytobillod],'color','b','lineWidth',2.5)
line([ztaloni ztobilloi],[xtaloni xtobilloi],[ytaloni ytobilloi],'color','r','lineWidth',2.5)
%TOBILLOS-PIES
line([ztobillod zpied],[xtobillod xpied],[ytobillod ypied],'color','b','lineWidth',2.5)
line([ztobilloi zpiei],[xtobilloi xpiei],[ytobilloi ypiei],'color','r','lineWidth',2.5)
% view([-37.5 -30])
view([62 14])
%Longitud del paso
lngpi=zref-zpiei;
lngpd=zref-zpied;
A=num2str(MovCad(i));
B=num2str(MovRod(i));
C=num2str(MovTob(i));
D=num2str(MovMano(i));
text(5+zcadera,xcadera,ycadera,'GRADOS Cadera:')
text(10+zcadera,.5-xcadera,ycadera,A)
text(zrodillad+5,xrodillad,yrodillad,'GRADOS Rodilla:')
text(10+zrodillad,.5+zrodillad,yrodillad,B)
text(5+ztobillod,xtobillod,ytobillod,'GRADOS Tobillo:')
text(10+ztobillod,.5+xtobillod,ytobillod,C)
text(zcodod,10+xcodod,10+ycodod,'GRADOS Mano:')
text(zcodod,10+xcodod,9+ycodod,D)
grid on;
F1=getframe;

end