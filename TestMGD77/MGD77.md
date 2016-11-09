> NATIONAL GEOPHYSICAL DATA CENTER
>
> NATIONAL OCEANIC AND ATMOSPHERIC ADMINISTRATION
>
> U.S. DEPARTMENT OF COMMERCE
-----------
> THE MARINE GEOPHYSICAL DATA EXCHANGE FORMAT - MGD77 / MGD77T
    (Bathymetry, Magnetics, Gravity and Seismics Navigation)

KEY TO GEOPHYSICAL RECORDS DOCUMENTATION NO. 10 (REVISED)

COMPILED BY THE MGD77 TASK GROUP
Allen M. Hittelman, Chairman
Robert C. Groman
Richard T. Haworth
Troy L. Holcombe
Graig McHendrie
Stuart M. Smith

National Geophysical Data Center
Boulder, Colorado
September 1977
December 1981 (Revised by Dan R. Metzger)
February 1989 (Revised by Dan R. Metzger)
January 1993 (Revised by Dan R. Metzger)
October 1995 (Revised by Dan R. Metzger)
August   1998 (Revised by Dan R. Metzger)
February  2010 (Revised by Dan Metzger to introduce MGD77T)



INTRODUCTION                I

GENERAL DESCRIPTION         II

THE HEADER RECORD - MGD77T  III

THE DATA RECORD - MGD77T    IV

THE HEADER RECORD -  MGD77  V

THE DATA RECORD -  MGD77    VI

10-DEGREE IDENTIFIER CODES  APPENDIX A

NGDC CONTACTS               APPENDIX B







# I.   INTRODUCTION

In January of 1977, a group of 24 geophysical data managers
from academia, government, industry and foreign countries
participated in a workshop at the National Geophysical Data
Center (NGDC) in Boulder, Colorado.  The "Workshop for Marine
Geophysical Data Formats" established the basic outline of a new
format for the exchange of digital underway geophysics data.  A
six member task force was formed to work with NGDC in
implementing the decisions of the workshop into the new format.
By the end of 1977 the "MGD77" format was being disseminated by
NGDC as its standard exchange format.

The "MGD77" format has experienced much success over the
past 30 years.  It has been sanctioned by the Intergovernmental
Oceanographic Commission (IOC) as an accepted standard for
international data exchange, and it has been translated into
French, Japanese, and Russian.  Most contributors of data to NGDC
now send transfer data over the internet in the "MGD77" format.

This newest revision adds a tab-delimited version of the
format: "MGD77T".  This allows expanded field lengths, space
savings, and easier import into spread sheets, DBMS databases,
and various low-level programs.



# II.   GENERAL DESCRIPTION
The digital format presented, and referred to as "MGD77" or
"MGD77T", is an exchange format for marine geophysical data
(bathymetry, magnetics, gravity and seismic navigation).  The
format is intended to be used for the transmission of data to and
from a data center and may be useful for the exchange of data
between marine institutions, and to be used by various software
programs as an import or export format.  Data is to be exchanged
as files, generally a header (documentation) file and a data file
for each survey operation.  Generally each survey operation is a
port-to-port operation of a survey vessel, but in some cases
several port-to-port operations of the same vessel are combined
into a single survey operation, especially if this is the manner
of organizing the data at the contributing institution.  Data may
be exchanged via the Internet or on various mass storage devices
such as magnetic tapes, removable disks and DVDs.  The National
Geophysical Data Center uses the World Wide Web as its chief
method of distribution of these data.

## Data Exchange

     1. For exchange of MGD77/MGD77T data participants shall
     establish type and format of the media to be exchanged and
     method of distribution.
     
     2. Ideally, for both MGD77 and MGD77T, the Header Record(s)
     and the data records will be contained in separate files.
     Optionally the data records can be in one of the two formats
     with the header in the other format.
     
     3. Each survey operation shall have one MGD77 Header
     consisting of 24 80-character logical records (thus 24 end-
     of-record characters) or one MGD77T tab-delimited Header
     record with a tab following header fields (and thus a single
     end-of-record character).  For MGD77 unspecified fields are
     filled with spaces.  For MGD77T unspecified fields will
     contain zero characters (field-ending tab follows previous
     tab immediately).  Tabs are generally omitted for any
     trailing unspecified fields, including the tab for the last
     specified field..
     
     4. The MGD77/MGD77T data records are sequentially and
     chronologically organized until the end of the file.  The
     data records are 120 logical characters for MGD77, or
     varying length for MGD77T with a tab following the data
     fields.  (Each record is followed by an end-of-record
     character.)  For MGD77 unspecified fields are 9's filled.
     For MGD77T unspecified fields will be nil (tab immediately
     follows previous field's delimiting tab)). Tabs will
     generally be omitted for any trailing unspecified fields,
     including the tab for the last specified field (software
     read statements must be prepared for this).
     
     5. A survey is defined as all observations that conveniently
     constitute a survey operation (e.g., a port-to-port survey
     or in some cases several surveys).  A survey file ideally
     should not span two media or 2 file sets.
     
__________________________________
# III. THE HEADER RECORD - MGD77T

The purpose of the (survey) Header Record is to document the 
content of the geophysical data contained within the survey data 
records.  In general, documentation that is constant throughout the 
survey will be in the Header Record, while data that is variable 
will be in the Data Records.

The Header Record contains fields which are numeric and
freely formatted text.  Each field is followed by a tab
character. Unspecified or unused fields are nil (a tab
immediately follows the previous field). Tabs are generally
omitted for any trailing unspecified fields, including the tab
for the last specified field.

MGD77T headers for groups of surveys can be contained in a
single file or in separate files (one file per survey).
Generally the grouping method will be the same as that of the
MGD77T data files.

The MGD77T survey header(s) file may optionally have a
heading record of field identifiers as the first record of the
file, followed by the actual survey header(s).  The field
identifier names offered in this format description below are not
to be considered as the "official" field identifier names.  Users
may offer their own field id names, or not insert a heading
record in the survey header(s) file.  However, the use of name
"FORMAT_77" as the second field identifier of the first record of
the file will make it easy for applications to determine that
this record is a heading record for a MGD77T survey header(s)
file in the same way that "MGD77T" in the second field of a
record identifies the record as a MGD77T survey header record.

Format Conventions for the MGD77T Header Record:

     1. For floating pt numbers, all decimal points are explicit
     (e.g. 123.456 signifies a value of +123.456)
     
     2. Leading zeros and blanks are discouraged in numeric
     fields. Trailing blanks in numeric fields are not allowed.
     
     3. Where floating pt values are whole numbers, the decimal
     part/decimal pt are not required.
     
     4. In floating pt values, trailing zeros after the last
     significant digit past the decimal are not required.
     
     5. Unspecified fields are nil (tab immediately follows
     previous field's delimiting tab).
     
     6. All plain language fields should be trimmed of beginning
     and ending blanks.
     
     7. All "corrections", (such as gravity tare and drift) are
     understood to be added.
     
     8. An End-of-Line (End-of-Record) character follows the last
     field.  Embedded End-of-Line characters within fields  are
     not allowed.
     

The following is a detailed description of the Header Record
for MGD77T.  Fields can be of type integer, floating point or
character.  Fields that always represent whole numbers are
designated as integers.  Fields that may contain a decimal
component are float, and fields that are alphanumeric are
character.



 [#]    Type  FIELD_ID     Description
 _____________________________________________________

 [1]    char  SURVEY_ID    SURVEY IDENTIFIER
                            Identifier supplied by the contributing organization,
                            else given by NGDC in a manner which represents the
                            data.  Identical to same in data record.
 
 [2]    char  FORMAT_77    FORMAT ACRONYM - Set to "MGD77T"

 [3]    char  CENTER_ID    DATA CENTER FILE NUMBER
                            Survey identifier bestowed by the data center.

 [4]    char  PARAMS_CO    PARAMETERS SURVEYED CODES
                            Status of geophysical parameters for this survey.
                            This field must be nil, or exactly 5 characters.
                            
                            nil - entire field unspecified
                            
                            COL. PARAMETER SURVEYED
                            1 - bathymetry
                            2 - magnetics
                            3 - gravity
                            4 - high-resolution seismics
                            5 - deep penetration seismics
                            _________________________________
                            CODE - (for columns 27-31)
                            0 - unspecified
                            1 - Parameter NOT surveyed
                            3 - Parameter surveyed, not in file
                            5 - Parameter surveyed, in file

 [5]    int   DATE_CREAT   FILE CREATION DATE - YYYYMMDD
                            Date data records were last altered/assimilated

 [6]    char  INST_SRC     SOURCE INSTITUTION
                            Organization which collected the data, or contributor
                            if collector not definitive.

 [7]    char  COUNTRY      COUNTRY

 [8]    char  PLATFORM     PLATFORM NAME

 [9]    int   PLAT_TYPCO   PLATFORM TYPE CODE
                            nil - Unspecified
                            1 - Surface ship
                            2 - Submersible ship
                            3 - Aircraft
                            4 - Buoy
                            5 - Mobile land
                            6 - Fixed land
                            7 - Deep tow
                            8 - Anchored seafloor instrument
                            9 - Other, specify in next
                            field

 [10]   char  PLAT_TYP     PLATFORM TYPE
                            e.g., "Ship","Plane", "Submarine", etc.

 [11]   char  CHIEF        CHIEF SCIENTIST(S)

 [12]   char  PROJECT      PROJECT, CRUISE, LEG
                            e.g., "Survops 6-69", "Indopac, Leg3"

 [13]   char  FUNDING      FUNDING
                            i.e. agency or institution

 [14]   int   DATE_DEP     SURVEY DEPARTURE DATE - YYYYMMDD

 [15]   char  PORT_DEP     PORT OF DEPARTURE
                            i.e. city, country

 [16]   int   DATE_ARR     SURVEY ARRIVAL DATE - YYYYMMDD

 [17]   char  PORT_ARR     PORT OF ARRIVAL
                            i.e. city, country

 [18]   char  NAV_INSTR    NAVIGATION INSTRUMENTATION
                            e.g. "Sat/LORAN A/Sextant"

 [19]   char POS_INFO     POSITION DETERMINATION METHOD/GEODETIC DATUM
                            e.g. "WGS84/Primary-Satellite, Secondary-LORAN A"

 [20]   char  BATH_INSTR   BATHYMETRY INSTRUMENTATION
                            Include information such as frequency, beam width, and
                            sweep speed of recorder.

 [21]   char  BATH_ADD     ADDITIONAL FORMS OF BATHYMETRY
                            e.g., "Microfilm","Analog records"

 [22]   char  MAG_INSTR    MAGNETICS INSTRUMENTATION
                            e.g., "Proton Precession Mag-GEOMETRICS G-801"

 [23]   char  MAG_ADD      ADDITIONAL FORMS OF MAGNETICS
                            e.g., "punch tape","analog records"

 [24]   char  GRAV_INSTR   GRAVITY INSTRUMENTATION
                            e.g., "L&R S-26"

 [25]   char  GRAV_ADD     ADDITIONAL FORMS OF GRAVITY DATA
                            e.g., "Microfilm","Analog records "

 [26]   char  SEIS_INSTR   SEISMIC INSTRUMENTATION
                            Include the size of the sound source, the recording 
                            frequency filters, and then number of channels
                            e.g. "1700 cu. in., Airgun, 8-62 Hz, 36 Channels"

 [27]   char  SEIS_FRMTS   FORMATS OF SEISMIC DATA
                            e.g., "Digital SEG-Y", "Mylar
                            Sections", etc.

 [28]   float LAT_TOP      NORTHBOUND LATITUDE OF SURVEY

 [29]   float LAT_BOTTOM   SOUTHBOUND LATITUDE OF SURVEY

 [30]   float LON_LEFT     WESTBOUND LONGITUDE OF SURVEY

 [31]   float LON_RIGHT    EASTBOUND LONGITUDE OF SURVEY

 [32]   float BATH_DRATE   GENERAL DIGITIZING RATE OF BATHYMETRY
                            In (tenths of minutes)/minutes.
                            The rate which is present within the data records;
                            the data records; e.g., if values were coded
                            every 30 seconds, set to (050)/0.5

 [33]   char  BATH_SRATE   GENERAL SAMPLING RATE OF BATHYMETRY
                            This rate is instrumentationdependent; 
                            e.g., "1/Second"

 [34]   float SOUND_VEL    ASSUMED SOUND VELOCITY
                            In meters per second. Historically, in the U.S.,
                            this speed has been 800 fathoms/sec, which equals
                            1463 meters/sec; currentrecorders generally have a
                            calibration of 1500 meters/sec; e.g. 1500

 [35]   int   VDATUM_CO    BATHYMETRIC VERTICAL DATUM CODE -
                            00 - No correction applied
                            01 - Lowest normal low water
                            02 - Mean lower low water
                            03 - Lowest low water
                            04 - Mean lower low water spring
                            05 - Indian spring low water
                            06 - Mean low water spring
                            07 - Mean sea level
                            08 - Mean low water
                            09 - Equatorial spring low water
                            10 - Tropic lower low water
                            11 - Lowest astronomical tide
                            88 - Other, specify in Add.

 [36]   char  BATH_INTBP   INTERPOLATION SCHEME
                            This field allows for a description of the
                            interpolation scheme used, should some of the data
                            records contain interpolated values; e.g., 
                            "5-minute intervals and peaks and troughs"

 [37]   float MAG_DRATE    GENERAL DIGITIZING RATE OF MAGNETICS
                            In minutes. The rate which is present within the data
                            the data records.

 [38]   float MAG_SRATE    GENERAL SAMPLING RATE OF MAGNETICS
                            In seconds.  This rate is instrumentation dependent
                            e.g., if the pulse rate is every 3 sec, set to 3

 [39]   float MAG_TOWDST   MAGNETIC SENSOR TOW DISTANCE
                            In meters.  The distance from the navigation reference
                            to the leading sensor.

 [40]   float MAG_SNSDEP   SENSOR DEPTH
                            In meters. This is theestimated depth of the 
                            lead agnetic sensor.

 [41]   float MAG_SNSSEP   HORIZONTAL SENSOR SEPARATION
                            In meters. Where two sensors are used.

 [42]   int   M_REFFL_CO   REFERENCE FIELD CODE
                            This is the reference field used to etermine 
                            the residual magnetics:
                            00 - Unused
                            01 - AWC 70
                            02 - AWC 75
                            03 - IGRF-65
                            04 - IGRF-75
                            05 - GSFC-1266
                            06 - GSFC (POGO) 0674
                            07 - UK 75
                            08 - POGO 0368
                            09 - POGO 1068
                            10 - POGO 0869
                            11 - IGRF-80
                            12 - IGRF-85
                            13 - IGRF-90
                            14 - IGRF-95
                            15 - IGRF-00
                            16 - IGRF-05
                            17 - IGRF-10
                            18 - IGRF-11
                            88 - Other, specify
                            nil - Unspecified reference field code

 [43]   char  MAG_REFFLD   REFERENCE FIELD
                           e.g., "IGRF-85"

 [44]   char  MAG_RF_MTH   METHOD OF APPLYING RESIDUAL FIELD
                            The procedure used in applying this reduction to
                            the data; e.g., "Linear Interp. in 60-mile Square"

 [45]   float GRAV_DRATE   GENERAL DIGITIZING RATE OF GRAVITY
                            In minutes. The rate present within the data records

 [46]   float GRAV_SRATE   GENERAL SAMPLING RATE OF GRAVITY
                            In seconds.  This rate is instrumentation dependent.
                            If recording is continuous, set to 0

 [47]   int   G_FORMU_CO   THEORETICAL GRAVITY FORMULA CODE
                            1 - Heiskanen 1924
                            2 - International 1930
                            3 - IAG System 1967
                            4 - IAG System 1980
                            8 - Other, specify

 [48]   char  GRAV_FORMU   THEORETICAL GRAVITY FORMULA
                            e.g., "International '30", "IAG System 1967", etc.

 [49]   int   G_RFSYS_CO   REFERENCE SYSTEM CODE
                            Identifies the reference field:
                            1 - Local system, specify
                            2 - Potsdam system
                            3 - System IGSN 71
                            9 - Other, specify

 [50]   char  GRAV_RFSYS   REFERENCE SYSTEM
                            e.g., "Potsdam System", "System IGSN 71", etc.

 [51]   char  GRAV_CORR    CORRECTIONS APPLIED
                            Drift, tare and bias corrections applied; 
                            e.g. "+0.075 mgal per day

 [52]   float G_ST_DEP_G   DEPARTURE BASE STATION GRAVITY
                            In milligals.  At sea level -Network value preferred.

 [53]   char  G_ST_DEP     DEPARTURE BASE STATION DESCRIPTION
                            Indicates name and number of station

 [54]   float G_ST_ARR_G   ARRIVAL BASE STATION GRAVITY
                            In milligals.  At sea level - Network value preferred.

 [55]   char  G_ST_ARR     ARRIVAL BASE STATION DESCRIPTION
                            Indicates name and number of
                            station

 [56]   int   IDS_10_NUM   NUMBER OF 10-DEGREE IDENTIFIERS
                            This is the number of 4-digit 10-degree identifiers which
                            will follow this field, excluding the "9999" flag.
                            (see APPENDIX A)

 [57]   char  IDS_10DEG    10-DEGREE IDENTIFIERS
                            A series of 4-digit codes, separated by commas, which
                            identify the 10-degree squares through which the
                            survey collected data (see APPENDIX A). Code "9999"
                            after last identifier.

 [58]   char  ADD_DOC      ADDITIONAL DOCUMENTATION
                            Information concerning this survey not contained in other
                            header fields.
                            Embedded End-of-Line characters are NOT ALLOWED.
___________________



IV. THE DATA RECORD - MGD77T
     The data record presents underway marine geophysical data in
a correlative manner.  Geophysical data (bathymetry, magnetics,
and gravity) and seismic/segment identification (e.g. seismic
line and shot-point ids) are presented with a corresponding time
and position.  Documentation that is variable throughout the
survey also is included within each data record.  If primary
navigation exists at a juncture where no geophysical data are
present, this record should be included with the data parameter
fields left unspecified (nil).

     MGD77T data files for groups of surveys can be contained in
a single file, or in separate files (one file per survey).
Generally the grouping method will be the same as that of the
MGD77T header files.


Format Conventions for the MGD77T Data Record:



     1. For floating pt numbers, all decimal points are explicit
     (e.g. 123.456 signifies a value of +123.456)
     
     2. Leading zeros and blanks are discouraged in numeric
     fields. Trailing blanks in numeric fields are not allowed.
     
     3. Where float values are whole numbers, the decimal
     part/decimal pt are not required.
     
     4. In floats, trailing zeros after the last significant
     digit past the decimal are not required.
     
     5. Unspecified fields are nil (tab immediately follows
     previous field's delimiting tab).
     
     6. All character fields should be trimmed of beginning and
     ending blanks.
     
     7. Trailing tabs (trailing unspecified values) are generally
     omitted, including the tab for the last specified (used)
     field.
     
     8. All "corrections", such as time zone, diurnal magnetics,
     and Eotvos, are understood to be added (e.g., time-zone
     correction is the number of hours which must be added to the
     recorded time to determine GMT).
     
     The following is a detailed description of the MGD77T Data
Record.  Fields can be of type integer, floating point, or
character.  Fields that always represent whole numbers are
described as type int; fields that may contain a decimal
component are float, and fields that are alphanumeric are char.


 [Field #]   Type    Description
 ____________________________________________________________
 
 [1]         char    SURVEY IDENTIFIER
                     Identifier supplied by the contributing
                     organization, else given by NGDC in a manner
                     which represents the data. Identical to that
                     in MGD77/MGD77T header record.

 [2]         float   TIME-ZONE CORRECTION
                     In hours. Corrects time (in fields 3-4)
                     to GMT when added: equals zero when time is
                     GMT.  Time-zone normally falls between -13
                     and +12 inclusively.

 [3]         int     DATE (YYYYMMDD)
                     e.g. 19720530

 [4]         float   TIME
                     Hours and decimal minutes
                     i.e. 11:59:40pm = 2359.6667

 [5]         float   LATITUDE
                     in decimal degrees
                     + = North; - = South
                     Between -90 and 90 degrees

 [6]         float   LONGITUDE
                     in decimal degrees
                     + = East; - = West
                     Between -180 and 180 degrees

 [7]         int     POSITION TYPE CODE
                     Indicates how lat/lon was obtained:
                     1 = Observed fix
                     3 = Interpolated
                     nil = Unspecified

 [8]         int     QUALITY CODE FOR NAVIGATION
                     1 - good
                     2 - fair
                     3 - poor
                     4 - bad                    5 - Suspected, by the originating institution
                     6 - Suspected, by the Data Center
                     nil - Unspecified
                     (Note: - Institution will most frequently nil
                     this field; however, should they have reason
                     to code a "5", the data center will not
                     contradict.)

 [9]         float   BATHYMETRY, 2- WAY TRAVELTIME
                     In seconds
                     Corrected for transducer depth and other such
                     corrections, especially in shallow water

 [10]        float   BATHYMETRY, CORRECTED DEPTH
                     In (positive) meters. e.g. 1234.56

 [11]        int     BATHYMETRIC CORRECTION CODE
                     This code details the procedure used for determining
                     the sound velocity correction to depth:
                     01-55 - Matthews' Zones with zone
                     59 - Matthews' Zones, no zone specified
                     60 - S. Kuwahara Formula
                     61 - Wilson Formula
                     62 - Del Grosso Formula
                     63 - Carter's Tables
                     88 - Other (see Add. Doc.)
                     97 - Computed using 1500 meters/sec
                     98 - Unknown if Corrected
                     nil - Unspecified

 [12]        int     BATHYMETRIC TYPE CODE
                     Indicates how the bathymetric value was obtained:
                     1 - Observed
                     3 - Interpolated
                     nil - Unspecified

 [13]        int     QUALITY CODE FOR BATHYMETRY
                     1 - good
                     2 - fair
                     3 - poor
                     4 - bad
                     5 - Suspected bad by Contributor
                     6 - Suspected bad by Data Center
                     nil - Unspecified

 [14]        float   MAGNETICS TOTAL FIELD, 1ST SENSOR
                     In nanoteslas; for leading sensor. Use this
                     field for single sensor.

 [15]        float   MAGNETICS TOTAL FIELD, 2ND SENSOR
                     In nanoteslas; for trailing sensor.

 [16]        float   MAGNETICS RESIDUAL FIELD
                     In nanoteslas; (reference field used is in Header)

 [17]        int     SENSOR FOR RESIDUAL FIELD
                     1 - 1st or leading sensor
                     2 - 2nd or trailing sensor
                     nil - Unspecified (or single sensor)

 [18]        float   MAGNETICS DIURNAL CORRECTION -
                     In nanoteslas (gammas). If nil, total and
                     residual fields are assumed to beuncorrected;
                     if used, total and residuals are assumed to 
                     have been already corrected with diurnal.

 [19]        int     DEPTH/ALTITUDE OF MAGNETICS SENSOR
                     In meters. + = Below sea-level, - = Above sea-level

 [20]                QUALITY CODE FOR MAGNETICS
                     1 - good
                     2 - fair
                     3 - poor
                     4 - bad
                     5 - Suspected bad by Contributor
                     6 - Suspected bad by Data Center
                     nil - Unspecified

 [21]        float   OBSERVED GRAVITY
                     In milligals
                     Corrected for Eotvos, drift, and tares

 [22]        float   EOTVOS CORRECTION
                     In milligals
                     E = 7.5 V cos(phi) * sin(alpha) + 0.0042 V*V

 [23]        float   FREE-AIR ANOMALY
                     In milligals
                     Free-air Anomaly = G(observed) minus
                     G(theoretical)

 [24]                QUALITY CODE FOR GRAVITY
                     1 - good
                     2 - fair
                     3 - poor
                     4 - bad
                     5 - Suspected bad by Contributor
                     6 - Suspected bad by Data Center
                     nil - Unspecified

 [25]        char    LINE/TRACK/SEGMENT ID
                     Used, for example, to cross reference with
                     seismic data.
   
 [26]       char     SEISMIC SHOT-POINT NUMBER/POINT ID
_____________________________________



V.   THE HEADER RECORD - Legacy MGD77


     The purpose of the Header Record is to document both the
content and structure of the geophysical data contained within
subsequent data records.  In general, documentation that is
constant throughout the survey will be in the Header Record,
while documentation that is variable will be in the Data Records.

     The Header Record contains fields which are both fixed and
freely formatted.  For MGD77, the Header consists of a "sequence"
of twenty four 80-character images.

     
Format Conventions for the MGD77 Header Record:



     1. For MGD77, all decimal points are implied (e.g. 1234 in
     10ths of units signifies a value of 123.4); for MGD77T, all
     decimal points are explicit (e.g. 123.456 signifies a value
     of 123.456)
     
     2. Leading zeros and blanks are equivalent in numeric
     fields.
     
     3. Unspecified (unknown or unused) fields are to be blank
     filled.
     
     4. All plain language fields should be left justified.
     
     5. All "corrections", such as gravity tare and drift, are
     understood to be added
     

     The following is a detailed description of the Header Record
for (legacy) MGD77.  Fields can be of type integer, floating
point or character.  Fields that represent whole numbers are
integers.  Fields that may contain a decimal component are float,
and fields that are alphanumeric are char.


Character          Length
Nos.      of Field  Type     Description
_____________________________________________________

Sequence No. 1


1           1       int      RECORD TYPE - Set to "4"

2-9         8       char     SURVEY IDENTIFIER
                             Identifier supplied by the
                             contributing organization, else
                             given by NGDC in a manner which
                             represents the data. Identical to
                             that in data record.
                             
10-14       5       char     FORMAT ACRONYM - Set to"MGD77"

15-22       8       char     DATA CENTER FILE NUMBER
                             Survey identifier bestowed by the
                             data center. First 2 chars indicate
                             the source, first 4 indicate
                             platform.
                             
                             
27-31       5       int      PARAMETERS SURVEYED CODE
                             Status of geophysical parameters for
                             this survey.
                             
                             COLUMN  PARAMETER SURVEYED
                              27     bathymetry
                              28     magnetics
                              29     gravity
                              30     high-resolution seismics
                              31     deep penetration seismics
                           _________________________________
                           
                             CODE - (for columns 27-31)

                             0 or blank - unspecified
                             1 - Parameter NOT surveyed
                             3 - Parameter surveyed, not in file
                             5 - Parameter surveyed, in file

32-39       8       int      FILE CREATION DATE (YYYYMMDD)
                             Date data records were last altered
                             (including century).
                             
40-78       39      char     SOURCE INSTITUTION
                             Organization which collected the
                             data. Include contributor if
                             different from collector.
                             
79-80       2       int      SEQUENCE NUMBER - Set to "01"


Sequence No. 2


1-18        18      char     COUNTRY

19-39       21      char     PLATFORM NAME

40          1       int      PLATFORM TYPE CODE
                             0 - Unspecified
                             1 - Surface ship
                             2 - Submersible ship
                             3 - Aircraft
                             4 - Buoy
                             5 - Mobile land
                             6 - Fixed land
                             7 - Deep tow
                             8 - Anchored seafloor instrument
                             9 - Other, specify

41-46       6       char     PLATFORM TYPE
                             (e.g., "SHIP","PLANE", "SUB", etc.)
                             
47-78       32      char     CHIEF SCIENTIST(S)

79-80       2       int      SEQUENCE NUMBER - Set to "02"


Sequence No. 3


1-58        58      char     PROJECT
                             (e.g., "SURVOPS 6-69", "INDOPAC,
                             Leg3")
                             
59-78       20      char     FUNDING
                             (i.e. agency or institution)
                             
79-80       2       int      SEQUENCE NUMBER - Set to "03"


Sequence No. 4


1-8         8       int      SURVEY DEPARTURE DATE (YYYYMMDD)

9-40        32      char     PORT OF DEPARTURE
                             (i.e. city, country)
                             
41-48       8       int      SURVEY ARRIVAL DATE (YYYYMMDD)

49-78       30      char     PORT OF ARRIVAL
                             (i.e. city, country)
                             
79-80       2       int      SEQUENCE NUMBER - Set to "04"


Sequence No. 5


1-40        40      char     NAVIGATION INSTRUMENTATION
                             (e.g. "SAT/LORAN A/SEXTANT")
                             
41-78       38      char     GEODETIC DATUM/POSITION
                             DETERMINATION METHOD
                             (e.g. "WGS84/PRIM - SATELLITE, SEC-
                             LORAN A")
                             
79-80       2       int      SEQUENCE NUMBER - Set to "05"


Sequence No. 6


1-40        40      char     BATHYMETRY INSTRUMENTATION
                             Include information such as
                             frequency, beam width, and sweep
                             speed of recorder.
                             
41-78       38      char     ADDITIONAL FORMS OF BATHYMETRIC
                             DATA
                             (e.g., "MICROFILM","ANALOG RECORDS")
                             
79-80       2       int      SEQUENCE NUMBER - Set to "06"


Sequence No. 7


1-40        40      char     MAGNETICS INSTRUMENTATION
                             (e.g., "PROTON PRECESSION MAG-
                             GEOMETRICS G-801")
                             
41-78       38      char     ADDITIONAL FORMS OF MAGNETICS DATA
                             (e.g., "PUNCH TAPE","ANALOG
                             RECORDS")
                             
79-80       2       int      SEQUENCE NUMBER - Set to "07"


Sequence No. 8


1-40        40      char     GRAVITY INSTRUMENTATION
                             (e.g., "L and R S-26")
                             
41-78       38      char     ADDITIONAL FORMS OF GRAVITY DATA
                             (e.g., "MICROFILM", "ANALOG
                             RECORDS")
                             
79-80       2       int      SEQUENCE NUMBER - Set to "08"


Sequence No. 9


1-40        40      char     SEISMIC INSTRUMENTATION
                             Include the size of the sound
                             source, the recording frequency
                             filters, and the number of channels
                             (e.g., "1700 cu. in., AIRGUN, 8-62
                             Hz, 36 CHANNELS")
                             
41-78       38      char     FORMATS OF SEISMIC DATA
                             (e.g., "DIGITAL", "MICROFILM",
                             "NEGATIVES", etc.)
                             
79-80       2       int      SEQUENCE NUMBER - Set to "09"


Sequence No. 10


1           1       char     FORMAT TYPE
                             Set to "A", which means format
                             contains integers, floating points,
                             and alphanumerics
                             
2-76        75      char     FORMAT DESCRIPTION
                             This is one method of reading (not
                             writing) the data in FORTRAN. Set to
                             the following:
                             "(I1,A8,I3,I4,3I2,F5.3,F8.5,F9.5,I1,
                             F6.4,
                             F6.1,I2,I1,3F6.1,I1,F5.1,F6.0,F7.1,"
                             (NOTE: continued in sequence no. 11)
                             
79-80       2       int      SEQUENCE NUMBER - Set to "10"


Sequence No. 11


1-19        19      char     FORMAT DESCRIPTION
                             Continued, set to following:
                             "F6.1,F5.1,A5,A6,I1)"
                             
41-43       3       int      NORTHBOUND LATITUDE OF SURVEY **
                             (to next whole degree)

44-46       3       int      SOUTHBOUND LATITUDE

47-50       4       int      WESTBOUND LONGITUDE

51-54       4       int      EASTBOUND LONGITUDE

79-80       2       int      SEQUENCE NUMBER - Set to "11"


Sequence No. 12


1-3         3       float    GENERAL DIGITIZING RATE OF
                             BATHYMETRY
                             In tenths of minutes.
                             The rate which is present within the
                             data records (e.g., if values were
                             coded every 5 minutes, set to "050")
                             
4-15        12      char     GENERAL SAMPLING RATE OF
                             BATHYMETRY
                             This rate is instrumentation
                             dependent (e.g., "1/SECOND")
                             
16-20       5       float    ASSUMED SOUND VELOCITY
                             In tenths of meters per second.
                             Historically, in the U.S., this
                             speed has been 800 fathoms/sec,
                             which equals 1463.0 meters/sec.;
                             however, some recorders have a
                             calibration of 1500 meters/sec
                             (e.g., "14630")
                             
21-22       2       int      BATHYMETRIC DATUM CODE -
                             00 - No correction applied
                             01 - Lowest normal low water
                             02 - Mean lower low water
                             03 - Lowest low water
                             04 - Mean lower low water spring
                             05 - Indian spring low water
                             06 - Mean low water spring
                             07 - Mean sea level
                             08 - Mean low water
                             09 - Equatorial spring low water
                             10 - Tropic lower low water
                             11 - Lowest astronomical tide
                             88 - Other, specify in Add. Doc.

23-78       56      char     INTERPOLATION SCHEME
                             This field allows for a description
                             of the interpolation scheme used,
                             should some of the data records
                             contain interpolated values (e.g.,
                             "5-MINUTE INTERVALS AND PEAKS AND
                             TROUGHS").
                             
79-80       2       int      SEQUENCE NUMBER - Set to "12"


Sequence No. 13


1-3         3       float    GENERAL DIGITIZING RATE OF
                             MAGNETICS
                             In tenths of minutes.
                             The rate which is present within the
                             data records.

4-5         2       int      GENERAL SAMPLING RATE OF
                             MAGNETICS
                             In seconds.
                             This rate is instrumentation
                             dependent (e.g., if the pulse rate
                             is every 3 sec, set to "03")
                             
6-9         4       int      MAGNETIC SENSOR TOW DISTANCE
                             In meters.
                             The distance from the navigation
                             reference to the leading sensor.
                             
10-14       5       float    SENSOR DEPTH
                             In tenths of meters.
                             This is the estimated depth of the
                             lead magnetic sensor.
                             
15-17       3       int      HORIZONTAL SENSOR SEPARATION
                             In meters.  Where two sensors are
                             used.
                             
18-19       2       int      REFERENCE FIELD CODE
                             This is the reference field used to
                             determine the residual magnetics:
                             00 - Unused
                             01 - AWC 70
                             02 - AWC 75
                             03 - IGRF-65
                             04 - IGRF-75
                             05 - GSFC-1266
                             06 - GSFC (POGO) 0674
                             07 - UK 75
                             08 - POGO 0368
                             09 - POGO 1068
                             10 - POGO 0869
                             11 - IGRF-80
                             12 - IGRF-85
                             13 - IGRF-90
                             14 - IGRF-95
                             15 - IGRF-00
                             16 - IGRF-05
                             17 - IGRF-10
                             18 - IGRF-11
                             88 - Other, specify
                             
20-31       16      char     REFERENCE FIELD
                             (e.g., "IGRF-85")

32-78       47      char     METHOD OF APPLYING RESIDUAL FIELD
                             The procedure used in applying this
                             reduction to the data (e.g., "LINEAR
                             INTERP. in 60-mile SQUARE")
                             
79-80       2       int      SEQUENCE NUMBER - Set to "13"


Sequence No. 14


1-3         3       float    GENERAL DIGITIZING RATE OF GRAVITY
                             In tenths of minutes.
                             The rate present within the data
                             records
                             
4-5         2       int      GENERAL SAMPLING RATE OF GRAVITY
                             In seconds.
                             This rate is instrumentation
                             dependent. If recording is
                             continuous, set to "00"
                             
6           1       int      THEORETICAL GRAVITY FORMULA CODE
                             1 - Heiskanen 1924
                             2 - International 1930
                             3 - IAG System 1967
                             4 - IAG System 1980
                             8 - Other, specify

7-23        17      char     THEORETICAL GRAVITY FORMULA
                             (e.g., "INTERNATIONAL '30", "IAG
                             SYSTEM (1967)", etc.)
                             
24          1       int      REFERENCE SYSTEM CODE
                             Identifies the reference field:
                             1 - Local system, specify
                             2 - Potsdam system
                             3 - System IGSN 71
                             9 - Other, specify

25-40       16      char     REFERENCE SYSTEM
                             (e.g., "POTSDAM SYSTEM", "SYSTEM
                             IGSN 71", etc.)
                             
41-78       38      char     CORRECTIONS APPLIED
                             Drift, tare and bias corrections
                             applied. (e.g., "+0.075 MGAL PER
                             DAY")
                             
79-80       2       int      SEQUENCE NUMBER - Set to "14"


Sequence No. 15


1-7         7       float    DEPARTURE BASE STATION GRAVITY
                             In tenths of milligals.
                             At sea level (Network value
                             preferred.)
                             
8-40        33      char     DEPARTURE BASE STATION DESCRIPTION
                             Indicates name and number of station
                             
41-47       7       float    ARRIVAL BASE STATION GRAVITY
                             In tenths of milligals.
                             At sea level (Network value
                             preferred.)
                             
48-78       31      char     ARRIVAL BASE STATION DESCRIPTION
                             Indicates name and number of station
                             
79-80       2       int      SEQUENCE NUMBER - Set to "15"


Sequence No. 16


1-2         2       int      NUMBER OF 10-DEGREE IDENTIFIERS **
                             This is the number of 4-digit 10-
                             degree identifiers, excluding the
                             "9999" flag, which will follow this
                             field. (see APPENDIX A)
                             
                             
4-78        75      int      10-DEGREE IDENTIFIERS
                             A series of 4-digit codes,separated
                             by commas, which identify the 10-
                             degree squares through which the
                             survey collected data (see APPENDIX
                             A). Code "9999" after last
                             identifier.
                             
79-80       2       int      SEQUENCE NUMBER - Set to "16"

Sequence No. 17


1-75        75      int      10-DEGREE IDENTIFIERS
                             Continued

79-80       2       int      SEQUENCE NUMBER - Set to "17"


Sequence Nos. 18-24


1-78        78      char     ADDITIONAL DOCUMENTATION
                             information concerning this survey
                             not contained in header fields.
                             
79-80       2       int      SEQUENCE NUMBER ("18" thru "24")




______________

** Fields 41-54 in sequence Number 11 and Fields 1-78 in sequence
numbers 16 and 17 may be blank filled by the contributing
institution.  The data center can determine these numbers by a
computer search of the latitudes and longitudes within the MGD77
file.
___________________




VI.   THE DATA RECORD - MGD77
     The data record presents underway marine geophysical data in
a correlative manner.  Geophysical data (bathymetry, magnetics,
and gravity) and seismic/semgnt identification (e.g. shot-point
identification) are presented with a corresponding time and
position.  Documentation that is variable throughout the survey
also is included within each data record.  If primary navigation
exists at a juncture where no geophysical data are present, this
record should be included with the data parameter fields left
unused (9s filled).

     The logical record length is 120 characters a.


Format Conventions for the MGD77 Data Record:



     1. All decimal points are implied (e.g. 1234 in 10ths of
     units signifies a value of 123.4)
     
     2. Leading zeros and blanks are equivalent.
     
     3. Unknown or unused fields are to be 9's filled.
     
     4. All "corrections", such as time zone, diurnal magnetics,
     and Eotvos, are understood to be added (e.g., time-zone
     correction is the number of hours which must be added to the
     recorded time to determine GMT).

     The following is a detailed description of the Data Record.
Fields can be of type integer, floating point or character.
Fields that represent whole numbers are integers.  Fields that
contain a decimal component are float, and fields that are
alphanumeric are character.


Character   Length
Nos.        of Field         Type  Description
____________________________________________________________

1           1       int      DATA RECORD TYPE
                             Set to "5" (data record.)

2-9         8       char     SURVEY IDENTIFIER
                             Identifier supplied by the
                             contributing organization, else
                             given by NGDC in a manner which
                             represents the data. Identical to
                             that in header record.
                             
                             
                             
10-12       3       int      TIME-ZONE CORRECTION
                             In hours. Corrects time (in
                             fields 3-4) to GMT when added:
                             equals zero when time is GMT.
                             Timezone normally falls between -13
                             and +12 inclusively.
                             
13-16       4       int      YEAR
                             including century (e.g. 1972)
                             
17-18       2       int      MONTH
                             (e.g. May is represented as 05)
                             
19-20       2       int      DAY
                             Day of month
                             
21-22       2       int      HOUR
                             Hour of day
                             
23-27       5       float    MINUTES X 1000

28-35       8       float    LATITUDE X 100000
                             + = North; - = South
                             Between -90 and 90 degrees
                             
36-44       9       float    LONGITUDE X 100000
                             + = East; - = West
                             Between -180 and 180 degrees
                             
45          1       int      POSITION TYPE CODE
                             Indicates how lat/lon was obtained:
                             1 = Observed fix
                             3 = Interpolated
                             9 = Unspecified

46-51       6       float    BATHYMETRY, 2- WAY TRAVELTIME
                             In ten-thousandths of seconds.
                             Corrected for transducer depth and
                             other such corrections, especially
                             in shallow water
                             
52-57       6       float    BATHYMETRY, CORRECTED DEPTH
                             In tenths of meters.
                             
58-59       2       int      BATHYMETRIC CORRECTION CODE
                             This code details the procedure used
                             for determining the sound velocity
                             correction to depth:

                             01-55 Matthews' Zones with zone
                             59    Matthews' Zones, no zone
specified
                             60    S. Kuwahara Formula
                             61    Wilson Formula
                             62    Del Grosso Formula
                             63    Carter's Tables
                             88    Other (see Add. Doc.)
                             97    Computed using 1500 meters/sec
                             98    Unknown if Corrected
                             99    Unspecified

60          1       int      BATHYMETRIC TYPE CODE
                             Indicates how the bathymetric value
                             was obtained:
                             1 - Observed
                             3 - Interpolated (Header Seq. 12)
                             9 - Unspecified

61-66       6       float    MAGNETICS TOTAL FIELD, 1ST SENSOR
                             In tenths of nanoteslas (gammas).
                             For leading sensor. Use this field
                             for single sensor.
                             
67-72       6       float    MAGNETICS TOTAL FIELD, 2ND SENSOR
                             In tenths of nanoteslas (gammas).
                             For trailing sensor.
                             
73-78       6       float    MAGNETICS RESIDUAL FIELD
                             In tenths of nanoteslas (gammas).
                             The reference field used is in
                             Header Seq. 13.
                             
79          1       int      SENSOR FOR RESIDUAL FIELD
                             1 - 1st or leading sensor
                             2 - 2nd or trailing sensor
                             9 - Unspecified

80-84       5       float    MAGNETICS DIURNAL CORRECTION -
                             In tenths of nanoteslas (gammas).
                             If  9-filled (i.e., set to "+9999"),
                             total and residual fields are
                             assumed to be uncorrected; if used,
                             total and residuals are assumed to
                             have been already corrected.
                             
85-90       6       int      DEPTH/ALTITUDE OF MAGNETICS SENSOR
                             In meters.
                             + = Below sealevel
                             - = Above sealevel

91-97       7       float    OBSERVED GRAVITY
                             In tenths of milligals.
                             Corrected for Eotvos, drift, and
                             tares
                             
98-103      6       float    EOTVOS CORRECTION
                             In tenths of milligals.
                             E = 7.5 V cos(phi) * sin(alpha) +
                             0.0042 V*V
                             
104-108     5       float    FREE-AIR ANOMALY
                             In tenths of milligals.
                             Free-air Anomaly = G(observed) minus
                             G(theoretical)
                             
109-113     5       char     LINE/TRACK/SEGMENT ID
                             Used, for example, to cross
                             reference with seismic data.
                             
114-119    6        char     SEISMIC SHOT-POINT NUMBER/POINT ID

120        1        int      QUALITY CODE FOR NAVIGATION -
                             5 - Suspected, by the contributor
                             6 - Suspected, by the data center
                             9 - No identifiable problem found
                             (NOTE - Institution will most
                             frequently 9-fill this field;
                             however, should they wish to code a
                             "5", the data center will not
                             contradict.  The data center's
                             quality control program, which
                             performs (among other checks) a
                             vectorial analysis of the
                             navigation, is available in a
                             printout form upon request.)
                             
____________________________________________________________




APPENDIX A   10-DEGREE-SQUARE IDENTIFIER CODE

A 10-degree-square area can be easily identified by constructing
a four-digit number.  The components of this number, in order of
their construction are described as follows:

Quadrant - A one-digit number identifies the quadrant of the
world with the following significance to each digit:

   1st digit = Quadrant number

   Qc Code         Latitude        Longitude
   _______         ________        _________
      1            North           East
      3            South           East
      5            South           West
      7            North           West

10-Degree Square - The next three digits identify a unique 10-
degree square; thus the significant digits consist of:

           2nd digit = Tens digit of degrees latitude
           3rd digit = Hundreds digit of degrees longitude
           4th digit = Tens digit of degrees longitude

                    10-DEGREE SQ IDENT. CODE
                    ________________________
                    
Example                  Quad Lat  Long Long
37 deg 48'S, 4 deg 13'E   3    3   0     0
21.6 deg S, 14.3 deg W    5    2   0     1
34 deg 28'N, 143 deg 27'W 7    3   1     4
75 deg N, 43 deg E        1    7   0     4

___________________________________________________________




APPENDIX B   NGDC CONTACTS


Dan R. Metzger: (303) 497-6542  Dan.R.Metzger@noaa.gov
     or
John G. Campagnoli : (303) 497-3158  John.G.Campagnoli@noaa.gov

National Geophysical Data Center
NOAA, E/GC3
325 Broadway
Boulder, CO 80305

TELEX 592811 NOAA MASC BDR
FAX (303) 497-6513

____________________________________________________________

