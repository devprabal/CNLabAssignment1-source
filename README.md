# How to use python files ?

>The python source code files which provide automation include
  - Q1_ping_automation_draft.py
  - add_column_names.py
>Other python / ipython files are my approach to the assignment questions. They provide the code for the content(solutions) of the markdown in this [repo](https://github.com/devprabal/CNLabAssignment1-solutions).

## Q1_ping_automation_draft.py

This file provides code for scrapping data from the website mentioned in the first question of the Assignment - [http://www.spfld.com/ping.html]

### First things first
Things to keep in mind while using the file:
  - Install all required libraries beforehand. Either do a pip install or manually install them in the appropriate environment if using [Anaconda](https://www.anaconda.com/download/) (recommended).
  - [Selenium](https://pypi.org/project/selenium/) is the most important package to be installed.
  - Install [geckodriver](https://github.com/mozilla/geckodriver/releases) for firefox and export it to PATH.
  - Copy the source code py file to a fresh directory and execute from that directory.

### Changes to be made to code

 - ```host_name``` should be changed to whatever host you wish to ping.
 - Similarly,  ```packet_size``` must also be changed if you wish to use other than 64 bytes, which is default.
```sh
host_name = "no-reverse-dns-configured.com"
packet_size = str(64)
```
 - The range in for loop is set to iterate 20 times, as per question.
```sh
for x in range (20):
```
 - Change the file name when writing to .csv file for a host other than the one used previously. This is to provide convenience and better manageability. However, it is not compulsory.
```sh
with open(r'data_host2.csv', 'a', newline='') as csvfile:
```

## add_column_names.py

This file provides code for adding the header to the csv files generated from **Q1_ping_automation_draft.py**
### Changes to be made to code

 - Change the file name at both occurences to the file-name.csv which was generated for a particular host from previous code. You can manually check the working directory for the presence of csv files.
```sh
with open(r'data_host5.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open(r'data_host2.csv','w',newline='') as f:
```
# TO DO

- Put a method/ line of code for header row to csv file generated in **Q1_ping_automation_draft.py** so that there is no need for **add_column_names.py**
- Add ```time.sleep()``` in **Q1_ping_automation_draft.py** so as to fully automate the process for different times of the day.
- Make a list of all hosts to be pinged so as to remove the pain of manually changing ```host_name``` every time a new host has to be pinged. Iterate over that list.
- Add ```if...else``` or ```try...except``` clause to handle the condition when packet loss is 100%
- Write code to automatic change the ```file-name.csv``` when the ```host_name``` is changed.
- Check why does webdriver stops sometimes on fewer than 20 iterations.
- Add geographical location information to the dictionary ```dict_ping_details``` by scrapping the website - [https://check-host.net]
