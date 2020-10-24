{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>Lists in Python</h1>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><strong>Welcome!</strong> This notebook will teach you about the lists in the Python Programming Language. By the end of this lab, you'll know the basics list operations in Python, including indexing, list operations and copy/clone list.</p> "
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
    "<h2 id=\"list\">Lists</h2>"
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
    "We are going to take a look at lists in Python. A list is a sequenced collection of different objects such as integers, strings, and other lists as well. The address of each element within a list is called an <b>index</b>. An index is used to access and refer to items within a list."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " To create a list, type the list within square brackets <b>[ ]</b>, with your content inside the parenthesis and separated by commas. Let’s try it!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "# Create a list\n",
    "\n",
    "L = [\"Michael Jackson\", 10.1, 1982]\n",
    "L"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can use negative and regular indexing with a list :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "# Print the elements on each index\n",
    "\n",
    "print('the same element using negative and positive indexing:\\n Postive:',L[0],\n",
    "'\\n Negative:' , L[-3]  )\n",
    "print('the same element using negative and positive indexing:\\n Postive:',L[1],\n",
    "'\\n Negative:' , L[-2]  )\n",
    "print('the same element using negative and positive indexing:\\n Postive:',L[2],\n",
    "'\\n Negative:' , L[-1]  )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"content\">List Content</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lists can contain strings, floats, and integers. We can nest other lists, and we can also nest tuples and other data structures. The same indexing conventions apply for nesting:    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "# Sample List\n",
    "\n",
    "[\"Michael Jackson\", 10.1, 1982, [1, 2], (\"A\", 1)]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"op\">List Operations</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " We can also perform slicing in lists. For example, if we want the last two elements, we use the following command:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "# Sample List\n",
    "\n",
    "L = [\"Michael Jackson\", 10.1,1982,\"MJ\",1]\n",
    "L"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "# List slicing\n",
    "\n",
    "L[3:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can use the method <code>extend</code> to add new elements to the list:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Michael Jackson', 10.2, 'pop', 10]"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use extend to add elements to list\n",
    "\n",
    "L = [ \"Michael Jackson\", 10.2]\n",
    "L.extend(['pop', 10])\n",
    "L"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Another similar method is <code>append</code>. If we apply <code>append</code> instead of <code>extend</code>, we add one element to the list:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Michael Jackson', 10.2, ['pop', 10]]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use append to add elements to list\n",
    "\n",
    "L = [ \"Michael Jackson\", 10.2]\n",
    "L.append(['pop', 10])\n",
    "L"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " Each time we apply a method, the list changes. If we apply <code>extend</code> we add two new elements to the list. The list <code>L</code> is then modified by adding two new elements:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Michael Jackson', 10.2, 'pop', 10]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use extend to add elements to list\n",
    "\n",
    "L = [ \"Michael Jackson\", 10.2]\n",
    "L.extend(['pop', 10])\n",
    "L"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If we append the list  <code>['a','b']</code> we have one new element consisting of a nested list:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Michael Jackson', 10.2, 'pop', 10, ['a', 'b']]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use append to add elements to list\n",
    "\n",
    "L.append(['a','b'])\n",
    "L"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As lists are mutable, we can change them. For example, we can change the first element as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "# Change the element based on the index\n",
    "\n",
    "A = [\"disco\", 10, 1.2]\n",
    "print('Before change:', A)\n",
    "A[0] = 'hard rock'\n",
    "print('After change:', A)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " We can also delete an element of a list using the <code>del</code> command:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "# Delete the element based on the index\n",
    "\n",
    "print('Before change:', A)\n",
    "del(A[0])\n",
    "print('After change:', A)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can convert a string to a list using <code>split</code>.  For example, the method <code>split</code> translates every group of characters separated by a space into an element in a list:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "# Split the string, default is by space\n",
    "\n",
    "'hard rock'.split()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can use the split function to separate strings on a specific character. We pass the character we would like to split on into the argument, which in this case is a comma.  The result is a list, and each element corresponds to a set of characters that have been separated by a comma: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "# Split the string by comma\n",
    "\n",
    "'A,B,C,D'.split(',')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"co\">Copy and Clone List</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "When we set one variable <b>B</b> equal to <b>A</b>; both <b>A</b> and <b>B</b> are referencing the same list in memory:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A: ['hard rock', 10, 1.2]\n",
      "B: ['hard rock', 10, 1.2]\n"
     ]
    }
   ],
   "source": [
    "# Copy (copy by reference) the list A\n",
    "\n",
    "A = [\"hard rock\", 10, 1.2]\n",
    "B = A\n",
    "print('A:', A)\n",
    "print('B:', B)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Initially, the value of the first element in <b>B</b> is set as hard rock. If we change the first element in <b>A</b> to <b>banana</b>, we get an unexpected side effect.  As <b>A</b> and <b>B</b> are referencing the same list, if we change list <b>A</b>, then list <b>B</b> also changes. If we check the first element of <b>B</b> we get banana instead of hard rock:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "B[0]: hard rock\n",
      "B[0]: banana\n"
     ]
    }
   ],
   "source": [
    "# Examine the copy by reference\n",
    "\n",
    "print('B[0]:', B[0])\n",
    "A[0] = \"banana\"\n",
    "print('B[0]:', B[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is demonstrated in the following figure: "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can clone list  **A** by using  the following syntax:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['banana', 10, 1.2]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Clone (clone by value) the list A\n",
    "\n",
    "B = A[:]\n",
    "B"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " Variable **B** references a new copy or clone of the original list; this is demonstrated in the following figure:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now if you change <b>A</b>, <b>B</b> will not change: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "B[0]: banana\n",
      "B[0]: banana\n"
     ]
    }
   ],
   "source": [
    "print('B[0]:', B[0])\n",
    "A[0] = \"hard rock\"\n",
    "print('B[0]:', B[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 id=\"quiz\">Quiz on List</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a list <code>a_list</code>, with the following elements <code>1</code>, <code>hello</code>, <code>[1,2,3]</code> and <code>True</code>. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "# Write your code below and press Shift+Enter to execute"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Find the value stored at index 1 of <code>a_list</code>."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "# Write your code below and press Shift+Enter to execute"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Retrieve the elements stored at index 1, 2 and 3 of <code>a_list</code>."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "# Write your code below and press Shift+Enter to execute"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Concatenate the following lists <code>A = [1, 'a']</code> and <code>B = [2, 1, 'd']</code>:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
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
 "nbformat_minor": 4
}
