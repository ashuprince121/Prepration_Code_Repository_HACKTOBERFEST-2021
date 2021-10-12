private static int binarySearch(int[] array, int val)
{
	Arrays.sort(array);
	int start = 0;
	int end = array.length-1;
	int middle;
	while(start <= end)
	{
	  middle = (start + end) / 2;
	  if(array[middle] == val)
		return middle;
	  if(array[middle] < val)
	  {
	    start = middle +1;
	  }
	  else
	  {
	    end = middle -1;
	  }
    }
	return -1;
}