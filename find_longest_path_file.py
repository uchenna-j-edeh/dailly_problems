"""
Author: Uchenna Edeh
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
represents:

dir 
	subdir1
	subdir2
		file.ext

The dire dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.txt\n\t\tsubdir1\n\tsubdir2\n\t\tsubdir2\n\t\t\tfile2.ext"
represents:

dir
	subdir1
		file1.ext
		subsubdir1
	subdir2
		subsubdir2
		file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty 
second-level sub directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext\

we are interested in finding the longest(number of characters) absolute path to a file within our file syste. 
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext" and its length is 32 (
not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system.
If there is no file in the system, return 0.
Note:
The name of a file contains at least a period and an extention.

Algorithm:
First parse the string into tree data structure.
Second do a tree transversal (since all dir node must be visted, it does not matter which transversal we use)
Detailed Algorithm:
1. create the root node and assigned the value to 'dir'
2. decend one level (use # of '\t' to keep tract of level number)
3. add the next level to list of childred. if level has a file name, calculate the running # of string of parent name and the chid name. if level has directory count the # of '\t' to see if it will be a sibling or a child
"""
