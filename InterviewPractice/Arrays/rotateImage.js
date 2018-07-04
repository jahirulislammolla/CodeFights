function rotateImage(a) {
   var  length=a.length;
   var new1=new Array();
   var m=0,p=0,j=0,i=0;
    for(i=0;i<length;i++)
    {
      new1[i]=new Array();
      m=length-1;
      for (j=0;j<length; j++) {
         p=a[m][i];
         new1[i][j]=p;
         m--;
       }

    }
    return new1;
}
