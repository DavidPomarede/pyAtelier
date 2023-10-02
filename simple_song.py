{\rtf1\ansi\ansicpg1252\cocoartf2757
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 p9 >> jbass([5,4,0,2], dur=[1/2,1,1/2,1], amp=[1,3/4,3/4,3/4])\
\
p1 >> \
\
p2 >> piano([11,0,11,7,11,0,11,7,4], dur=1)\
\
p4 >> pluck([-12, -12, -12,-12], dur=[1, 1/2, 1, 1/2], amp=0.75) \
\
Scale.default = Scale.minor\
\
p9.stop\
\
tempo = 240\
\
d1.stop\
\
k2 >> karp(dur=1/4, oct=1)\
k2.bend(1)\
\
k2.stop()\
\
!#$%&*0-0/1234:=@ABCDEFGHIJKLMNOPQRSTUVWXYZ\\\\^abcdefghijklmnopqrstuvwxyz~\
\
x--(-[--])o--o(-=)-\
\
d1 >> play(P["o--o"].layer("mirror"),\
	pan=(-1,1),\
	dur=PDur(5,8),\
	sample=-1,\
	rate=var([1,4],[28,4]))\
\
\
d1 >> play(P[":="].layer("mirror"),\
	pan=(-1,1),\
	dur=PDur(5,8),\
	sample=-1,\
	rate=var([1,4],[28,4]))\
\
d1.stop()\
\
d2 >> play(PZip("Vs", "  n "), sample=10, hpf=var([0,4000],[28,4])).every(3, 'stutter', dur=1)\
\
d2.stop()\
\
d1.stop()\
d2.stop()\
d3.stop()\
d4.stop()\
\
p1.stop()\
p2.stop()\
p3.stop()\
p4.stop()\
p9.stop()\
\
}