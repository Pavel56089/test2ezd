# test to ezd

The script transfers the grades received by students for the Google Form (test option) to the Electronic Journal of Moscow dnevnik.mos.ru (homework).

Python libraries
- selenium
- pygsheets

# How to use?

In the Estimate field, insert a formula like =IFS(B2 >7; "5"; B2 > 5; "4"; 1; "3") and extend it over the entire range
Leave the EJD field empty. This is where the script will write Yes - the grade is posted or No - there is a problem and the grade is not posted.

Run the local virtual env environment
 
[Generate Google key](https://pygsheets.readthedocs.io/en/latest/authorization.html)

Rename data_example to data and enter:

  - EJD login and password
  - link to google table (with editing rights)
  - links to class's journal (e.g. if several classes are in the same grade)
  - ids of days that you get grades for


Done!


License
----

MIT


**Free Software, Hell Yeah!**
