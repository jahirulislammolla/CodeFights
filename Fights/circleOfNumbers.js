function circleOfNumbers(n, firstNumber) {
   var m=n/2;
   var y=m+firstNumber;
   var count=firstNumber;
  for(i=firstNumber;i<y;i++)
   {
      if(i==n-1){
         count=0;
      }
      else{
         count++;
      }
   }
   return count;
}
