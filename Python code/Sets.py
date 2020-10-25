{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>Sets in Python</h1>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><strong>Welcome!</strong> This notebook will teach you about the sets in the Python Programming Language. By the end of this lab, you'll know the basics set operations in Python, including what it is, operations and logic operations.</p> "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 id=\"set\">Sets</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"content\">Set Content</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A set is a unique collection of objects in Python. You can denote a set with a curly bracket <b>{}</b>. Python will automatically remove duplicate items:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a set\n",
    "\n",
    "set1 = {\"pop\", \"rock\", \"soul\", \"hard rock\", \"rock\", \"R&B\", \"rock\", \"disco\"}\n",
    "set1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The process of mapping is illustrated in the figure:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " You can also  create a set from a list as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Convert list to set\n",
    "\n",
    "album_list = [ \"Michael Jackson\", \"Thriller\", 1982, \"00:42:19\", \\\n",
    "              \"Pop, Rock, R&B\", 46.0, 65, \"30-Nov-82\", None, 10.0]\n",
    "album_set = set(album_list)             \n",
    "album_set"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let us create a set of  genres:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert list to set\n",
    "\n",
    "music_genres = set([\"pop\", \"pop\", \"rock\", \"folk rock\", \"hard rock\", \"soul\", \\\n",
    "                    \"progressive rock\", \"soft rock\", \"R&B\", \"disco\"])\n",
    "music_genres"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"op\">Set Operations</h3> "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let us go over set operations, as these can be used to change the set. Consider the set <b>A</b>:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sample set\n",
    "\n",
    "A = set([\"Thriller\", \"Back in Black\", \"AC/DC\"])\n",
    "A"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " We can add an element to a set using the <code>add()</code> method: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add element to set\n",
    "\n",
    "A.add(\"NSYNC\")\n",
    "A"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " If we add the same element twice, nothing will happen as there can be no duplicates in a set:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Try to add duplicate element to the set\n",
    "\n",
    "A.add(\"NSYNC\")\n",
    "A"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " We can remove an item from a set using the <code>remove</code> method:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Remove the element from set\n",
    "\n",
    "A.remove(\"NSYNC\")\n",
    "A"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " We can verify if an element is in the set using the <code>in</code> command:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Verify if the element is in the set\n",
    "\n",
    "\"AC/DC\" in A"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"logic\">Sets Logic Operations</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Remember that with sets you can check the difference between sets, as well as the symmetric difference, intersection, and union:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " Consider the following two sets:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sample Sets\n",
    "\n",
    "album_set1 = set([\"Thriller\", 'AC/DC', 'Back in Black'])\n",
    "album_set2 = set([ \"AC/DC\", \"Back in Black\", \"The Dark Side of the Moon\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Print two sets\n",
    "\n",
    "album_set1, album_set2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As both sets contain <b>AC/DC</b> and <b>Back in Black</b> we represent these common elements with the intersection of two circles."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can find the intersect of two sets as follow using <code>&</code>:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find the intersections\n",
    "\n",
    "intersection = album_set1 & album_set2\n",
    "intersection"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can find all the elements that are only contained in <code>album_set1</code> using the <code>difference</code> method:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find the difference in set1 but not set2\n",
    "\n",
    "album_set1.difference(album_set2)  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You only need to consider elements in <code>album_set1</code>; all the elements in <code>album_set2</code>, including the intersection, are not included."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The elements in <code>album_set2</code> but not in <code>album_set1</code> is given by:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "album_set2.difference(album_set1)  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can also find the intersection of <code>album_list1</code> and <code>album_list2</code>, using the <code>intersection</code> method:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use intersection method to find the intersection of album_list1 and album_list2\n",
    "\n",
    "album_set1.intersection(album_set2)   "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " This corresponds to the intersection of the two circles:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The union corresponds to all the elements in both sets, which is represented by coloring both circles:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " The union is given by:"
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
    "# Find the union of two sets\n",
    "\n",
    "album_set1.union(album_set2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And you can check if a set is a superset or subset of another set, respectively, like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Check if superset\n",
    "\n",
    "set(album_set1).issuperset(album_set2)   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Check if subset\n",
    "\n",
    "set(album_set2).issubset(album_set1)     "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Here is an example where <code>issubset()</code> and <code>issuperset()</code> return true:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Check if subset\n",
    "\n",
    "set({\"Back in Black\", \"AC/DC\"}).issubset(album_set1) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Check if superset\n",
    "\n",
    "album_set1.issuperset({\"Back in Black\", \"AC/DC\"})   "
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
    "<h2 id=\"quiz\">Quiz on Sets</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Convert the list <code>['rap','house','electronic music', 'rap']</code> to a set:"
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
    "Consider the list <code>A = [1, 2, 2, 1]</code> and set <code>B = set([1, 2, 2, 1])</code>, does <code>sum(A) = sum(B)</code> "
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
    "Create a new set <code>album_set3</code> that is the union of <code>album_set1</code> and <code>album_set2</code>:"
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
    "album_set1 = set([\"Thriller\", 'AC/DC', 'Back in Black'])\n",
    "album_set2 = set([ \"AC/DC\", \"Back in Black\", \"The Dark Side of the Moon\"])"
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
    "Find out if <code>album_set1</code> is a subset of <code>album_set3</code>:"
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
