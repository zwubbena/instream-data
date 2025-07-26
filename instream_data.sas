/* Generate instream dataset */
DATA ETH_RACE;
    INPUT ID $ SPED H I A P B W; *Read instream data using column input;
    DATALINES;
    0001 1 1 0 0 0 0 0
    0002 1 0 1 0 0 0 0
    0003 1 0 0 1 0 0 0
    0004 1 0 0 0 1 0 0
    0005 1 0 0 0 0 1 0
    0006 1 0 0 0 0 0 1
    0007 1 1 1 0 0 0 0
    0008 1 0 1 1 0 0 0
    0009 1 1 0 1 0 0 0
    0010 1 0 0 1 1 0 0
    0011 1 0 1 0 1 0 0
    0012 1 1 0 0 1 0 0
    0013 1 0 0 0 1 1 0
    0014 1 0 0 1 0 1 0
    0015 1 0 1 0 0 1 0
    0016 1 1 0 0 0 1 0
    0017 1 0 0 0 0 1 1
    0018 1 0 0 0 1 0 1
    0019 1 0 0 1 0 0 1
    0020 1 . . . . . .
	;
RUN;

/* Run descriptive check on test dataset */
PROC CONTENTS DATA=ETH_RACE; RUN;
PROC PRINT DATA=ETH_RACE (obs=20); RUN;
