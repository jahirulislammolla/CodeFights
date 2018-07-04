		function firstDuplicate(a) {	
     //  var a=[2, 3, 3, 1, 5, 2];
        var i=0;
			 var unsorted=[];
    		for(i=0;i<a.length;i++)
          {
            unsorted.push(a[i]);
          }
   				 var length=a.length;
   				 var new1=[];
   				var sorted=a.sort();
   				 var j=0;
   				 var index=0;
   				 var size=3*length;
   				 var count=0;
   				 var new_length=0;
   				 var m=0;
   				 var p=0;
         //  console.log(unsorted);
           //console.log(sorted);
   				 for(i=0;i<length-1;i++)
   				 {
   				 	if(sorted[i+1]==sorted[i])
   				 	{
   				 		new1.push(sorted[i]);
   				 	}
   				 }
   				 new_length=new1.length;
       //    console.log(unsorted);
   			//	 console.log(new1);
   				 if(new_length==0)
   				 {
   				 	return -1;
   				 }
   				 else if(new_length==1)
   				 {
   				 	return new1[0];
   				 }
   				 else
   				 {
   				 	for(i=0;i<new_length;i++)
   				 	{
   				 		count=0;
   				 	       m=0;
                     var index3=unsorted.indexOf(new1[i]);
   				 		for(j=index3+1;j<length;j++)
   				 		{
   				 			if(new1[i]==unsorted[j] && count<1)
   				 			{
   				 				m=m+j; 
                  //console.log(j+" "+m);

   				 				count++;
   				 				p=j;
   				 			}
   				 			if(count==1)
                           {
                              break;
                           }
   				 		}
   				 		if(m<=size)
   				 		{
   				 			size=m;
   				 			index=p;
   				 		}
   				 	}
   				 	return unsorted[index];

   				 }

		}
