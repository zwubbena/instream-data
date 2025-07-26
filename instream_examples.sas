/**************************************************************************
| Program: instream_data.sas
| Purpose: Demonstrate instream data using SAS DATALINES
**************************************************************************/

/***********************************
| EXAMPLE #1
***********************************/

/************
| SECTION 1: Define Instream Data
************/
data MOVIES;
    infile datalines dlm='|' dsd;
    length ID $2 Title $50 Year 4;
    input ID $ Title : $50. Year;
    datalines;
01|The Big Lebowski|1998
02|Happy Gilmore|1996
03|Kindergarten Cop|1990
04|Good Will Hunting|1997
05|Pretty Woman|1990
06|Groundhog Day|1993
07|Twister|1996
08|Sphere|1998
09|Home Alone|1990
;
run;

/************
| SECTION 2: Display Output
************/
proc contents data=MOVIES; run;

title "Instream Movie Data with Leading Zeros in ID (SAS)";
proc print data=MOVIES noobs label;
    label 
        ID = "Movie ID"
        Title = "Title"
        Year = "Release Year";
run;


/***********************************
| EXAMPLE #2
***********************************/

/************
| SECTION 1: Define Instream Data
************/
data ETH_RACE;
    input ID $ SPED H I A P B W; *Read instream data using column input;
    datalines;
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
run;

/************
| SECTION 2: Display Output
************/
proc contents data=ETH_RACE; run;

title "Instream Race/Ethnicity Data with Leading Zeros in ID (SAS)";
proc print data=ETH_RACE noobs label;
    label 
        ID   = "Student ID"
        SPED = "Special Education"
        H    = "Hispanic"
        I    = "American Indian or Alaska Native"
        A    = "Asian"
        P    = "Pacific Islander"
        B    = "Black or African American"
        W    = "White";
run;

/***********************************
| SAS Program End
***********************************/
