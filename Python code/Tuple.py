{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>Tuples in Python</h1>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><strong>Welcome!</strong> This notebook will teach you about the tuples in the Python Programming Language. By the end of this lab, you'll know the basics tuple operations in Python, including indexing, slicing and sorting.</p> "
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
    "<h2 id=\"tuple\">Tuples</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In Python, there are different data types: string, integer and float. These data types can all be contained in a tuple as follows:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, let us create your first tuple with string, integer and float."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create your first tuple\n",
    "\n",
    "tuple1 = (\"disco\",10,1.2 )\n",
    "tuple1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The type of variable is a **tuple**. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the type of the tuple you created\n",
    "\n",
    "type(tuple1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"index\">Indexing</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " Each element of a tuple can be accessed via an index. The following table represents the relationship between the index and the items in the tuple. Each element can be obtained by the name of the tuple followed by a square bracket with the index number:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can print out each value in the tuple:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the variable on each index\n",
    "\n",
    "print(tuple1[0])\n",
    "print(tuple1[1])\n",
    "print(tuple1[2])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can print out the **type** of each value in the tuple:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the type of value on each index\n",
    "\n",
    "print(type(tuple1[0]))\n",
    "print(type(tuple1[1]))\n",
    "print(type(tuple1[2]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can also use negative indexing. We use the same table above with corresponding negative values:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can obtain the last element as follows (this time we will not use the print statement to display the values):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use negative index to get the value of the last element\n",
    "\n",
    "tuple1[-1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can display the next two elements as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use negative index to get the value of the second last element\n",
    "\n",
    "tuple1[-2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use negative index to get the value of the third last element\n",
    "\n",
    "tuple1[-3]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"concate\">Concatenate Tuples</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can concatenate or combine tuples by using the **+** sign:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Concatenate two tuples\n",
    "\n",
    "tuple2 = tuple1 + (\"hard rock\", 10)\n",
    "tuple2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can slice tuples obtaining multiple values as demonstrated by the figure below:"
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
    "We can slice tuples, obtaining new tuples with the corresponding elements: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Slice from index 0 to index 2\n",
    "\n",
    "tuple2[0:3]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can obtain the last two elements of the tuple:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Slice from index 3 to index 4\n",
    "\n",
    "tuple2[3:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can obtain the length of a tuple using the length command: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get the length of tuple\n",
    "\n",
    "len(tuple2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This figure shows the number of elements:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"sort\">Sorting</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " Consider the following tuple:"
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
    "# A sample tuple\n",
    "\n",
    "Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can sort the values in a tuple and save it to a new tuple: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sort the tuple\n",
    "\n",
    "RatingsSorted = sorted(Ratings)\n",
    "RatingsSorted"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"nest\">Nested Tuple</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A tuple can contain another tuple as well as other more complex data types. This process is called 'nesting'. Consider the following tuple with several elements: "
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
    "# Create a nest tuple\n",
    "\n",
    "NestedT =(1, 2, (\"pop\", \"rock\") ,(3,4),(\"disco\",(1,2)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Each element in the tuple including other tuples can be obtained via an index as shown in the figure:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print element on each index\n",
    "\n",
    "print(\"Element 0 of Tuple: \", NestedT[0])\n",
    "print(\"Element 1 of Tuple: \", NestedT[1])\n",
    "print(\"Element 2 of Tuple: \", NestedT[2])\n",
    "print(\"Element 3 of Tuple: \", NestedT[3])\n",
    "print(\"Element 4 of Tuple: \", NestedT[4])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can use the second index to access other tuples as demonstrated in the figure:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " We can access the nested tuples :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print element on each index, including nest indexes\n",
    "\n",
    "print(\"Element 2, 0 of Tuple: \",   NestedT[2][0])\n",
    "print(\"Element 2, 1 of Tuple: \",   NestedT[2][1])\n",
    "print(\"Element 3, 0 of Tuple: \",   NestedT[3][0])\n",
    "print(\"Element 3, 1 of Tuple: \",   NestedT[3][1])\n",
    "print(\"Element 4, 0 of Tuple: \",   NestedT[4][0])\n",
    "print(\"Element 4, 1 of Tuple: \",   NestedT[4][1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can access strings in the second nested tuples using a third index:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the first element in the second nested tuples\n",
    "\n",
    "NestedT[2][1][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the second element in the second nested tuples\n",
    "\n",
    "NestedT[2][1][1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " We can use a tree to visualise the process. Each new index corresponds to a deeper level in the tree:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Similarly, we can access elements nested deeper in the tree with a fourth index:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the first element in the second nested tuples\n",
    "\n",
    "NestedT[4][1][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the second element in the second nested tuples\n",
    "\n",
    "NestedT[4][1][1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The following figure shows the relationship of the tree and the element <code>NestedT[4][1][1]</code>:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 id=\"quiz\">Quiz on Tuples</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Consider the following tuple:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# sample tuple\n",
    "\n",
    "genres_tuple = (\"pop\", \"rock\", \"soul\", \"hard rock\", \"soft rock\", \\\n",
    "                \"R&B\", \"progressive rock\", \"disco\") \n",
    "genres_tuple"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Find the length of the tuple, <code>genres_tuple</code>:"
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
    "Access the element, with respect to index 3: "
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
    "Use slicing to obtain indexes 3, 4 and 5:"
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
    "Find the first two elements of the tuple <code>genres_tuple</code>:"
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
    "Find the first index of <code>\"disco\"</code>:"
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
    "Generate a sorted List from the Tuple <code>C_tuple=(-5, 1, -3)</code>:"
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
    "<p>Copyright &copy; 2018 IBM Developer Skills Network. This notebook and its source code are released under the terms of the <a href=\"https://cognitiveclass.ai/mit-license/\">MIT License</a>.</p>"
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
