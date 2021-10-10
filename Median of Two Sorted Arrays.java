class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
         ArrayList<Integer>arrayList=new ArrayList<>();
         double result=Integer.MIN_VALUE;
         int advindex=0;
        
        
        for(Integer r:nums1){
            arrayList.add(r);
        }
        for(Integer r:nums2){
            arrayList.add(r);
        }
        
        Collections.sort(arrayList);
        int index=0;

        if(arrayList.size()%2!=0){
            index=arrayList.size()/2;
            result=arrayList.get(index);
        }
        else {
          index=arrayList.size()/2;
          advindex=index-1;
          index=arrayList.get(index);
          advindex=arrayList.get(advindex);
          result=(double)(index+advindex)/2; 
            return result;
        }
      
        return result;
    }
}
