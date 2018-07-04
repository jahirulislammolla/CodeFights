function sudoku2(grid) {
   var i=0,j=0,count=0,m=0,n=0;
   var arr1=[],arr2=[],arr3=[];
   var length=grid.length;
   for(i=0;i<length;i++)
   {
   	arr1=[];
   	arr2=[];
   	m=0,n=0;
   	for(j=0;j<length;j++){
   		if(grid[count][j] != ".")
	     {
	     	arr1[m]=grid[count][j];
	     	m++;
	     }
	     if(grid[j][count] != ".")
	     {
	     	arr2[n]=grid[j][count];
	     	n++;
	     }
   	}

   	if(m>=1)
   	{
	   arr1.sort();
	  //console.log(arr1);
	   for(j=0;j<m-1;j++)
	   {
	   	if(arr1[j]==arr1[j+1])
	   	{//console.log('false');
	   		return false;
	   		
	   	}
	   }
   	}
   	if(n>=1)
   	{
	   arr2.sort();
	//   console.log(arr2);
	   for(j=0;j<n-1;j++)
	   {
	   	if(arr2[j]==arr2[j+1])
	   	{console.log('false');
	   		return false;
	   		//console.log('flase');
	   	}
	   }
   	}
     count++;
   }
   var s=0;
    s=check(0,0,grid);   
    if(s==1)
    {
    	return false;
    }
    s=check(0,3,grid);   
    if(s==1)
    {
    	return false;
    }
    s=check(0,6,grid);   
    if(s==1)
    {
    	return false;
    }
    s=check(3,0,grid);   
    if(s==1)
    {
    	return false;
    }
    s=check(3,3,grid);   
    if(s==1)
    {
    	return false;
    }
    s=check(3,6,grid);   
    if(s==1)
    {
    	return false;
    }
    s=check(6,0,grid);   
    if(s==1)
    {
    	return false;
    }
    s=check(6,3,grid);   
    if(s==1)
    {
    	return false;
    }
    s=check(6,6,grid);   
    if(s==1)
    {
    	return false;
    }
    return true;
 }
 function check(first,second,grid)
 {
 	var i=0,j=0,m=0;
 	var arr1=[];
 	for(i=first;i<first+3;i++)
 	{
 		for(j=second;j<second+3;j++)
 		{
 		if(grid[i][j] != ".")
	     {
	     	arr1[m]=grid[i][j];
	     	m++;
	     }
 		}
 	}
	if(m>0)
	{
	 arr1.sort();
	 // console.log(arr1);
	   for(j=0;j<m-1;j++)
	   {
	   	if(arr1[j]==arr1[j+1])
	   	{//console.log('false');
	   		return 1;
	   		
	   	}
	   }
	}
	return 0;

 }
