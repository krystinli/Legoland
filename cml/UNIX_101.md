## 00_Shell 
- primary purpose is to read commands and run other programs
- high action to keystrok ratio
- support automating repetitive tasks 
- can be used to access network machines 

### 01_Command keys
- `i=1` there're no space around in assignment statement; the statement will not work if those spaces are added. 
- `while [ $cnt -le 5 ] do xxx done` the space inside condition for while loop are mandatory. 
- `chmod a+w myfile` add access to myfile
-  `^Z` force quite
- `^C` kill the job
- `echo xxx` print xxx 
- `^A ^E` move the arrow to beginning of the line or end of the line
- `-le` for less than or equal to
- `-ge` greater or equal to 
- `-eq -ne` equal/not equal to 
- `cd ~/.` home dir
- `vi newfile.txt` create a new txt file  
- `chmod a+w myfile` add access w to myfile
- `chmod 755 myfile` same as above

### 01_Navigate_Through_Repos
- `.` - current direction
- `..` parent dir
- `~` home dir
- `-` last dir
- `~abc` visit someone else's home dir
- `ls -alF` list of all files and dir
- `ls -s -h` print size 
- `chmod a+w file_nm` add write access to file_nm 
- `ls -R` list of all files within subdir recursively
- `ls -t` list files in order of last change (time)
- `mv draft.txt draft2.txt` - rename a file  
- `cp draft.txt draft2.txt` - copy a draft to draft2  
- `rm draft.txt` - file deletion
- `rmdir dir_nm` - empty folder deletion
- `rm -r dir_nm` - non-empty folder deletion
- `mv * ..` move all files to parent dir
- `cp file1 file2 backup` - cp both files to backup folder 
- `ls -R` - list all the files within subfolders recursively 
- `ls -t` - list files in the order of last change (time) 

### 02_Files_Interaction 
- `mkdir foldr_nm`
- `vi draft.txt`, `:wq!`, `q!` 
- `mv draft.txt draft2.txt` rename a file
- `cp draft.txt draft2.txt` copy a draft to draft2
- `rm draft.txt`
- `rm -r dir_nm` non-empty folder deletion
- `mv * ..` move all files to the parent dir
- `cp file1 file2 backup` cp both files to a backup folder
- `wc *.txt` word count * files
- `*` is a wildcard
- `?` is also a wildcard, but only matches a single char 
- `wc -l *` num of lines per file
- `wc -l * > lengths` redirects the results into a file instead of printing on screen
- `cat lengths` cat stands for “concatenate”: it prints the contents of files one after another
- `sort -n lengths` numerical sort (otherwise it's alphabetical)
- `sed 's/^ *//' lengths | sort` sort and removing the leading space
- `head -1 lengths_sorted` print last line of the file
- `sort -n lengths | head -1` use the output of the command on the left as the input to the command on the right
- `wc -l *.pdb | sort -n | head -1` similar to above, but with word counts
- `uniq` removes adjacent duplicated lines from its input
- `head -5 animal.txt` top 5 * from the txt file
- `tail -5 animal.txt` 

### 03_Analytics
- `wc *.txt` word counts of all txt files 
- `*` is a wildcard
- `wc -l *` num of lines for each file
- `cat lengths` cat stands for concatenate. it prints the contents of the file one after another
- `sort -n lenths` numerical sort of all files (otherwise alphabetical)
- `sed 's/^ *//' lengths | sort` sort and removing the leading space
- `head -l lenths_sorted` print last line of the file
- `sort -n lenths | head -l` sort and output past line of file 
- `wc -l *.txt | sort -n | head -1` from left to right, use the output as input to the next action
- `uniq` remove adjacent duplicated lines 

### 04_Looping 
```
$ for filename in basilisk.dat unicorn.dat
> do
>    head -3 $filename
> done
```
- `filename` is a variable, being looped through in the above code 
- `$filename` we get the value by putting $ sign in front of the variable
- this loop prints out the first three lines of each data file in turn
```
$ for xxx in basilisk.dat unicorn.dat
> do
>    head -3 $xxx
> done
```
- quoting filename helps if there's a space in the filename:
```
for filename in *.dat
do
    head -100 "$filename" | tail -20
done
```
- change the file name for all files:
```
for filename in *.dat
do
    mv $filename original-$filename
done
```
- test run: print what will be ran:
```
for filename in *.dat
do
    echo mv $filename original-$filename
done
```
`--dry-run` prints commandas without actually running them 
-- pulling all filenames ending in A or B:
```
$ for datafile in *[AB].txt
> do
>     echo $datafile
> done
```
- multiple actions nested in one for loop:
```
$ for datafile in *[AB].txt; do echo $datafile; bash goostats $datafile stats-$datafile; done
```
### 05_while_loop 
- The while loop can be used to repeat a command(s) until the while condition becomes false.
- Be careful to make sure that the while condition does eventually become false!
- `cnt=1` there are no spaces around = in assignment statement. The statement will not work if those spaces are added.
```
$ count=1
$ while [ $count -le 5 ]
> do
>     echo Count has a value of $count
>     ((count++))
> done
```

### 06_logical_stmt 
- The `||` or `&&` can be used as conditionals that determine whether a second command is executed based on the success of the first command.
```
test_var='True'
if [[ $test_var == 'True']]
then xxxx
elif [[...]]
then yyyy
else 
zzzz 
fi 
```
- `&&` only run the part on the right if the part on the left ran successfully. 
- `$ [[ -f NENE01729A.txt ]] && wc -l NENE01729A.txt` we may want to check whether a file exists before we run a command against it, as shown here. If the file does not exist, then there is no reason to do the word count. 
- `-f` is a test to check whether a file exists.
- `||` With the double pipe, the second statement will only be executed if the first statement is false. 
- `$ [[ -f somefile.txt ]] || touch somefile.txt` we might want to create a file if it does not exist. 
- `touch` creates an empty file with the specified name.
- `cat filename.dat` print the data in the file
- `expr` arithematic calculation

### 07_scripts
- `$ echo "head -15 octane.pdb | tail -5" > middle.sh` it selects lines 11-15 of the file octane.pdb and putting the commands in a file.
- then we can run it by `bash middle.sh`
- `wc -l` lists the number of lines in the files
- `sort -n` sorts things numerically
  - combine into one `wc -l $* | sort -n > sorted.sh`
  - `$ bash sorted.sh *.pdb ../creatures/*.dat` special char $ means all of the command-line parameters to the shell script
- `history` prints all commands that run in this terminal in the chronological order and enumerates them.
- `#!/bin/bash`, which indicates that the script should be interpreted by `/bin/bash` - first line in shell script
- for a python script, you will use `#!/usr/bin/env python`

### 08_GREP
- `grep xxx filename` finding xxx in file
- `grep -r xxx .` find recursively in current dir 
