{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>String Operations</h1>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 id=\"strings\">What are Strings?</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The following example shows a string contained within 2 quotation marks:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use quotation marks for defining string\n",
    "\n",
    "\"Michael Jackson\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can also use single quotation marks:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use single quotation marks for defining string\n",
    "\n",
    "'Michael Jackson'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A string can be a combination of spaces and digits: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Digitals and spaces in string\n",
    "\n",
    "'1 2 3 4 5 6 '"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A string can also be a combination of special characters : "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Special characters in string\n",
    "\n",
    "'@#2_#]&*^%$'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can print our string using the print statement:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the string\n",
    "\n",
    "print(\"hello!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can bind or assign a string to another variable:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Michael Jackson'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Assign string to variable\n",
    "\n",
    "Name = \"Michael Jackson\"\n",
    "Name"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 id=\"index\">Indexing</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It is helpful to think of a string as an ordered sequence. Each element in the sequence can be accessed using an index represented by the array of numbers:  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " The first index can be accessed as follows:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr/>\n",
    "<div class=\"alert alert-success alertsuccess\" style=\"margin-top: 20px\">\n",
    "[Tip]: Because indexing starts at 0, it means the first index is on the index 0.\n",
    "</div>\n",
    "<hr/>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the first element in the string\n",
    "\n",
    "print(Name[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " We can access index 6:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the element on index 6 in the string\n",
    "\n",
    "print(Name[6])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Moreover, we can access the 13th index:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the element on the 13th index in the string\n",
    "\n",
    "print(Name[13])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"neg\">Negative Indexing</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " We can also use negative indexing with strings:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Negative index can help us to count the element from the end of the string."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The last element is given by the index -1: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the last element in the string\n",
    "\n",
    "print(Name[-1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " The first element can be obtained by  index -15:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the first element in the string\n",
    "\n",
    "print(Name[-15])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can find the number of characters in a string by using <code>len</code>, short for length:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find the length of string\n",
    "\n",
    "len(\"Michael Jackson\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"slice\">Slicing</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can obtain multiple characters from a string using slicing, we can obtain the 0 to 4th and 8th to the 12th element:  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Take the slice on variable Name with only index 0 to index 3\n",
    "\n",
    "Name[0:4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Take the slice on variable Name with only index 8 to index 11\n",
    "\n",
    "Name[8:12]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"concat\">Concatenate Strings</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can concatenate or combine strings by using the addition symbols, and the result is a new string that is a combination of both:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Concatenate two strings\n",
    "\n",
    "Statement = Name + \"is the best\"\n",
    "Statement"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To replicate values of a string we simply multiply the string by the number of times we would like to replicate it. In this case, the number is three. The result is a new string, and this new string consists of three copies of the original string:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the string for 3 times\n",
    "\n",
    "3 * \"Michael Jackson\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can create a new string by setting it to the original variable. Concatenated  with a new string, the result is a new string that changes from Michael Jackson to “Michael Jackson is the best\".\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Concatenate strings\n",
    "\n",
    "Name = \"Michael Jackson\"\n",
    "Name = Name + \" is the best\"\n",
    "Name"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 id=\"escape\">Escape Sequences</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Back slashes represent the beginning  of escape sequences. Escape sequences represent strings that may be difficult to input. For example, back slash \"n\" represents a new line. The output is given by a new line after the back slash \"n\" is encountered:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Michael Jackson \n",
      " is the best\n"
     ]
    }
   ],
   "source": [
    "# New line escape sequence\n",
    "\n",
    "print(\" Michael Jackson \\n is the best\" )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Similarly, back slash  \"t\" represents a tab: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Michael Jackson \t is the best\n"
     ]
    }
   ],
   "source": [
    "# Tab escape sequence\n",
    "\n",
    "print(\" Michael Jackson \\t is the best\" )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " If you want to place a back slash in your string, use a double back slash:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Michael Jackson \\ is the best\n"
     ]
    }
   ],
   "source": [
    "# Include back slash in string\n",
    "\n",
    "print(\" Michael Jackson \\\\ is the best\" )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " We can also place an \"r\" before the string to display the backslash:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Michael Jackson \\ is the best\n"
     ]
    }
   ],
   "source": [
    "# r will tell python that string will be display as raw string\n",
    "\n",
    "print(r\" Michael Jackson \\ is the best\" )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 id=\"operations\">String Operations</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There are many string operation methods in Python that can be used to manipulate the data. We are going to use some basic string operations on the data. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's try with the method <code>upper</code>; this method converts lower case characters to upper case characters:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert all the characters in string to upper case\n",
    "\n",
    "A = \"Thriller is the sixth studio album\"\n",
    "print(\"before upper:\", A)\n",
    "B = A.upper()\n",
    "print(\"After upper:\", B)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The method <code>replace</code> replaces a segment of the string, i.e. a substring  with a new string. We input the part of the string we would like to change. The second argument is what we would like to exchange the segment with, and the result is a new string with the segment changed: \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Replace the old substring with the new target substring is the segment has been found in the string\n",
    "\n",
    "A = \"Michael Jackson is the best\"\n",
    "B = A.replace('Michael', 'Janet')\n",
    "B"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The method <code>find</code> finds a sub-string. The argument is the substring you would like to find, and the output is the first index of the sequence. We can find the sub-string <code>jack</code> or <code>el<code>.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find the substring in the string. Only the index of the first elment of substring in string will be the output\n",
    "\n",
    "Name = \"Michael Jackson\"\n",
    "Name.find('el')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find the substring in the string.\n",
    "\n",
    "Name.find('Jack')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If the  sub-string is not in the string then the output is a negative one. For example, the string 'Jasdfasdasdf' is not a substring:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# If cannot find the substring in the string\n",
    "\n",
    "Name.find('Jasdfasdasdf')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 id=\"quiz\">Quiz on Strings</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What is the value of the variable <code>A</code> after the following code is executed? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Write your code below and press Shift+Enter to execute \n",
    "\n",
    "A = \"1\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What is the value of the variable <code>B</code> after the following code is executed?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Write your code below and press Shift+Enter to execute\n",
    "\n",
    "B = \"2\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What is the value of the variable <code>C</code> after the following code is executed?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write your code below and press Shift+Enter to execute \n",
    "\n",
    "C = A + B"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Consider the variable <code>D</code> use slicing to print out the first three elements:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write your code below and press Shift+Enter to execute\n",
    "\n",
    "D = \"ABCDEFG\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use a stride value of 2 to print out every second character of the string <code>E</code>: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Write your code below and press Shift+Enter to execute\n",
    "\n",
    "E = 'clocrkr1e1c1t'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Print out a backslash:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write your code below and press Shift+Enter to execute"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Convert the variable <code>F</code> to uppercase:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write your code below and press Shift+Enter to execute\n",
    "\n",
    "F = \"You are wrong\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Consider the variable <code>G</code>, and find the first index of the sub-string <code>snow</code>:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write your code below and press Shift+Enter to execute\n",
    "\n",
    "G = \"Mary had a little lamb Little lamb, little lamb Mary had a little lamb \\\n",
    "Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \\\n",
    "Everywhere that Mary went The lamb was sure to go\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the variable <code>G</code>, replace the sub-string <code>Mary</code> with <code>Bob</code>:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write your code below and press Shift+Enter to execute"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
