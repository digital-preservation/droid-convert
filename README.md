# droid-convert
Script to convert a DROID CSV export into the template required for transfer of digital material to The National Archives.
# About the script
This script takes a DROID csv export and transforms it into the structure required for digital transfer to The National Archives. 
It retains the five columns from the DROID CSV export which are required for the metadata and renames them to their appropriate names. 'URI' = ‘identifier’,  'NAME'=‘file_name’, 'TYPE'=’folder‘, 'LAST_MODIFIED'=’date_last_modified’, 'SHA256_HASH'=’checksum’.
It will then add in the additional columns required. It populates all possible fields with any default entries, for example ‘held_by = The National Archives, Kew’
It also gives you two options, the first option is to select whether your metadata needs a ‘description column’, and this is only needed if you have additional descriptive information which you want to add to the metadata, this will have to be entered manually. If selected the script will add a ‘description’ column as well as the appropriate closure columns used for this. 
The second option allows you to state whether all the files in the collection are open or not, if they are open it will populate them with the appropriate closure entries for open records. If they are not all open it will leave these to be entered manually.
The script only creates the default metadata columns, your metadata may still require further columns which should be agreed with the Digital Transfer Team.
# Software requirements
The script requires the two files – droidConvert.bat and droidConvert.py.
The script requires Python 3 with the pandas module included. It has been tested using Python 3.5.4, Python 3.6.4 and pandas 0.20.3, pandas 0.21.1
A version of python including pandas can be installed using anaconda https://www.anaconda.com/download/
It has been tested on a Windows 7 and Windows 10 environment.
An exe version of this file which does not require Python to be installed can be downloaded here - http://www.nationalarchives.gov.uk/documents/information-management/droid-convert.zip
# Running the script
1.	Click on the droidConvert.bat file to start the script.

2.	It will open a window with a prompt to enter the filepath of the DROID csv you want to convert. This can either typed in or you can drag the file into the window to add the filepath. Once added press Enter. 

3.	It will then ask if the metadata is going to include descriptions (if you wish to add any descriptive metadata in the ‘description’ column). If you want to add descriptions press ‘y’ or if not press ‘n’. Then press enter.

4.	It will then ask if all of the files in the collection are open. If they are press ‘y’ or if some or all of the files are closed press ‘n’. Once added press enter. If the majority of the files are open and only some are closed you may want to choose y and then change the metadata manually for the closed records.

5.	This will create the file which will be saved in the same directory that contains DroidConvert.py. It will be named the same as the DROID CSV export with ‘DroidConvertoutput_’ added to the beginning. 
 

6.	Press any key to exit the script. If there are any errors in running the script, error messages will display now. Common causes are listed below. If errors appear you will need to rerun the script with any necessary changes to get the output.
# Troubleshooting
1.	If an invalid DROID csv file is added it will return a ValueError, stating that the expected columns do not exist in the csv you are trying to convert. You will also get a ValueError if your DROID export did not have the preference set to include a SHA256 hash.  

2.	If you enter an incorrect filepath it will give you a FileNotFoundError.  

3.	The script will prompt you if you have not entered a correct ‘y’ or ‘n’ value for either of the options.  











