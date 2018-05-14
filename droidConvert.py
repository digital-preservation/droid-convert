import pandas as pd
import os

#This script is to take a DROID csv export and transform it into the structure required for digital transfer to TNA, it will populate default fields where possible. It gives you the option to select whether your metadata has 
#descriptions or not and populate the standard columns as appropriate, these are the default metadata columns, your collections may require additional metadata which should be agreed with the Digital Transfer Team.
#The script also allows you to state whether all the files in the collection are open or not, if they are open it will populate them with the closure fields for open records. If they are not all open it will leave these to be 
#entered manually.

#The script should be run using the droidConvert.bat file, to run it requires Python 3 with the pandas module included. It has been tested using Python 3.5.4, Python 3.6.4 and pandas 0.20.3, pandas 0.21.1
#a version of python including pandas can be installed using anaconda https://www.anaconda.com/download/

csvraw = input("Enter filepath of DROID csv to convert: ") #first input for filepath of DROID csv export
csvraw = csvraw.strip('"')#will strip speech marks which get added if you drag the file into the cmd window, input adds these anyway so otherwise will cause the file to not be found.
csvraw2 = input("Metadata includes descriptions y/n?") #second input for user to state if descriptions are needed
csvraw3 = input("All files are open y/n?") #third input to state if all files are open
droidname = os.path.basename(csvraw) #this takes the filename of the original DROID csv export to use later when saving the output
columns_needed = ['URI','NAME','TYPE','LAST_MODIFIED','SHA256_HASH'] #this states which columns are to be taken from original csv
csv = pd.read_csv(csvraw, usecols=columns_needed) #this will take the first input line and load the csv into pandas, it will only take the columsn needed as otherwise files with multiple identifications which have created
#additional columns causes errors in parsing the csv
add_csv = csv.rename(columns={'URI':'identifier','NAME':'file_name','TYPE':'file_name','TYPE':'folder','LAST_MODIFIED':'date_last_modified','SHA256_HASH':'checksum'})#this renames the columns to required names for digital
#transfer metadata

def add_columns_desc(): #will add columns in for metadata with descriptions and populate default fields
    add_csv ['closure_type'] = ''
    add_csv ['closure_period'] = ''
    add_csv ['closure_start_date'] = ''
    add_csv ['foi_exemption_code'] = ''
    add_csv ['foi_exemption_asserted'] = ''
    add_csv ['title_public'] = ''
    add_csv ['title_alternate'] =''
    add_csv ['description_public'] =''
    add_csv ['description_alternate'] =''
    add_csv ['rights_copyright'] = 'Crown Copyright'
    add_csv ['legal_status'] = 'Public Record(s)'
    add_csv ['held_by'] = 'The National Archives, Kew'
    add_csv ['description'] = ''
    
def add_columns_nodesc(): #will add columns in for metadata without descriptions and populate default fields
    add_csv ['closure_type'] = ''
    add_csv ['closure_period'] = ''
    add_csv ['closure_start_date'] = ''
    add_csv ['foi_exemption_code'] = ''
    add_csv ['foi_exemption_asserted'] = ''
    add_csv ['title_public'] = ''
    add_csv ['title_alternate'] =''
    add_csv ['rights_copyright'] = 'Crown Copyright'
    add_csv ['legal_status'] = 'Public Record(s)'
    add_csv ['held_by'] = 'The National Archives, Kew'
    
def open_closure_desc(): #if files are open populates these fields for metadata with descriptions
    add_csv ['closure_type'] = 'open_on_transfer'
    add_csv ['closure_period'] = '0'
    add_csv ['foi_exemption_code'] = 'open'
    add_csv ['title_public'] = 'TRUE'
    add_csv ['description_public'] = 'TRUE'

def open_closure_nodesc(): # if files are open populates these fields for metadata without descriptions
    add_csv ['closure_type'] = 'open_on_transfer'
    add_csv ['closure_period'] = '0'
    add_csv ['foi_exemption_code'] = 'open'
    add_csv ['title_public'] = 'TRUE'
    

if csvraw2 == ('y'): # if files have descriptions will run add_columns_desc
    add_columns_desc()
    add_csv = add_csv[['identifier','file_name','folder','description','date_last_modified','checksum','closure_type','closure_period','closure_start_date','foi_exemption_code','foi_exemption_asserted','title_public','title_alternate','description_public','description_alternate','rights_copyright','legal_status','held_by']] #reorders column once description has been added

elif csvraw2 == ('n'): # if files have not got descriptions will run add_columns_nodesc
    add_columns_nodesc()


else:
    print ("Please enter y or n for if metadata includes description") # if a value which is not y or n is entered it will prompt to try again
    exit(0)
    
if csvraw3 == ('y'): # if files are all open will run the open_closure functions depending on whether it includes descriptions or not
    if csvraw2 == ('y'):
        open_closure_desc()
    elif csvraw2 == ('n'):
        open_closure_nodesc()

elif csvraw3 == ('n'):
    pass # if files are not all open it will move on to the next stage without doing anything
else:
    print ("Please enter y or n for if all files are open") # if a value which is not y or n is entered it will prompt to try again
    exit(0)

#the add_columns function allows you to insert a column and then insert standard text to populate it, can add more columns if needed or change text

add_csv['folder'] = add_csv['folder'].replace('Folder', 'folder')# This changes both of these to lowercase as this is required for ingest
add_csv['folder'] = add_csv['folder'].replace('File', 'file')

add_csv.to_csv('DroidConvertoutput_'+droidname, index=False)#Index is set to false to stop python adding an index column, this writes changes to dataframe to a new csv file using original names as part of the filename
