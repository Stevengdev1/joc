Writing Files Practice

1. Write a python program that reads in a text file and prints all the lines back out with a 
dash in front. 

Example program run: 
> python3 read_file.py 

Input File contents: 
hello 
goodbye 
1234 

Outputs: 
-hello 
-goodbye 
-1234 

2. Write a python program that asks the user for the name of a file, and then repeatedly 
asks the user to enter a number, entering the number 'O' when finished. Output each of these numbers to the file on a separate line. 

Example program run: 
> python3 write_numbers.py 

User inputs: 
out.txt 
25 
34 
14 
0 

Output file out.txt created with the following contents: 
25 
34 
14 

3. Write a python program that reads 3 files called test1.txt, text2.txt, and text3.txt, counts the number of lines in each file, and prints out the number of lines to a file counts.txt. 
Example program run: 
> python3 read3_files.py

text1.txt:       |    text2.txt:         |    text3.txt: 
Hello            |    Goodbye            |    End of semester approaches!
how are you?     |    Number 5           |
Good.            |    Nice knowing you   |
See you later.   |

 Output file counts.txt created with the following contents:
 
text1.txt : 4 
text2.txt : 3 
text3.txt : 2

Hint: How to be DRY & not copy/paste the code 3 times? There are 2 approaches: 
a. Create a function with the filename as a parameter & call it 3 times 
b. Create a list of the file names and loop over the file names

4. Create a program similar to above that counts the number of words in the files as well. 
After printing out information about each file, this program should also print the total number of lines & words in all 3 files. You can use the string split function to split a line of input into a list of words by splitting the line on spaces. 
Example program run:

> python3 read3_files2.py 

text1.txt:        |      text2.txt:           |       text3.txt:
Hello             |      Goodbye              |       End of semester approaches!
how are you?      |      Number 5             |
Good.             |      Nice knowing you     |
See you later.    |

Output file counts.txt created with the following contents:
 
text1.txt : 4 lines, 8 words 
text2.txt : 3 lines, 6 words 
text3.txt : 2 lines, 4 words 
TOTAL: 9 lines, 18 words

