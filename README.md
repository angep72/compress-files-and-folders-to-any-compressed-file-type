Description
Below is a Python program that compresses files and folders into various formats such as .zip, .tar, and .tgz. The program offers a straightforward command-line interface where users can choose the folder to compress and the desired compression type. If the user opts for .tgz compression, the program automatically names the compressed file using the format: "name_of_the_folder_date_month_year.tgz".


Requirements
Python 3.x
Required libraries: os, shutil, tarfile, zipfile
Usage
Clone or download this repository to your local machine.
Navigate to the directory containing the folder_compressor.py file using the command line.
Run the program by executing the following command:
python main.py
Follow the prompts to provide the path of the folder you want to compress and select the desired compression type.
Example
Suppose you have a folder named MyFolder located at C:\Users\Username\Documents\MyFolder. You want to compress this folder into a .tgz file. Here's how you would use the program:

Run the program by executing python main.py.
Enter the path C:\Users\Username\Documents\MyFolder when prompted for the folder path.
Choose tgz as the compression type.
The compressed file will be saved as MyFolder_<current_date>.tgz in the same directory where the program is run.

Author 
p.umunyana@alustudent.com