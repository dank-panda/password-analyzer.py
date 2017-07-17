# password-analyzer.py
A quick python script to analyze a given set of passwords and give you some statistics. Used for identifying the most effective hashcat rules and masks, based on observed password trends.

## Usage: #
python password-analyzer.py **_wordlist.txt_**

## Sample Output: #
------------------------------------------------------------
 Starting Characters
------------------------------------------------------------
 182 of the 258 passwords start with an uppercase letter
  [ ~ 70 % ] 

 37 of the 258 passwords start with a lowercase letter
  [ ~ 14 % ] 

 24 of the 258 passwords start with a number
  [ ~ 9 % ] 

 15 of the 258 passwords start with a special character
  [ ~ 5 % ] 

------------------------------------------------------------
 Ending Characters
------------------------------------------------------------
 40 of the 258 passwords end with a letter
  [ ~ 15 % ] 

 160 of the 258 passwords end with a number
  [ ~ 62 % ] 

 58 of the 258 passwords end with a special character
  [ ~ 22 % ] 

------------------------------------------------------------
 Word Length
------------------------------------------------------------
 0 of the 258 passwords have 5 or fewer letters
  [ ~ 0 % ] 

 0 of the 258 passwords have 6 letters
  [ ~ 0 % ] 

 0 of the 258 passwords have 7 letters
  [ ~ 0 % ] 

 3 of the 258 passwords have 8 letters
  [ ~ 1 % ] 

 60 of the 258 passwords have 9 letters
  [ ~ 23 % ] 

 53 of the 258 passwords have 10 letters
  [ ~ 20 % ] 

 53 of the 258 passwords have 11 letters
  [ ~ 20 % ] 

 89 of the 258 passwords have 12 or more letters
  [ ~ 34 % ] 

------------------------------------------------------------
 Client Name
------------------------------------------------------------
 0 of the 258 passwords have the client's name
  [ ~ 0 % ] 
