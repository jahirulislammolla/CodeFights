function minesweeper2(gameboard, opening, moves) {
	var x_len=gameboard.length;
	var y_len=gameboard[0].length;
	var moves_len=moves.length;
	for(i=0;i<moves_len;i++)
	{
		var m=moves[i];
		var j=m[0];
		var k=m[1];
		if(gameboard[j][k] == 9)
		{
			return [];
		}
		if(gameboard[j][k] !=0 )
		{
			opening[j][k]=true;
			return opening;
		}
		
		if(gameboard[j][k] == 0)
		{
			var arr=func_arry(gameboard,opening,j,k);
			//console.log(arr);
			var length_arr=arr.length;
			while(length_arr>0)
			{
				arr3=[];
				var count=0;
				//console.log(arr2);
				for(var l=0;l<length_arr;l++)
				{
					m=arr[l];
					j=m[0];
					k=m[1];
					//console.log(m);
					var n=func_arry(gameboard,opening,j,k);
					//console.log(n);
					if(n.length>0){
						m=n[0];
						arr3[count]=new Array();
						arr3[count].push(m[0]);
						arr3[count].push(m[1]);
						count++;
					}
				}
				length_arr=arr3.length;
			}
		}
		
	}
	return opening;
}
function func_arry(gameboard,opening,j,k)
	{
				var length=gameboard.length;
    			var len=gameboard[0].length;
    			var arr=new Array();
    			var i=0;
			    m=j-1;
            	n=k-1;
            	gameboard[j][k]=1;
            	opening[j][k]=true;
            	if(m>=0 && n>=0)
            	{
            		opening[m][n]=true;
            		if(gameboard[m][n]==0)
            		{
            			arr[i]=new Array();
            			arr[i].push(m);
            			arr[i].push(n);
            			i++;
            		}		

            	}
            	m=j-1;
            	n=k;
            	if(m>=0 && n>=0)
            	{
            		opening[m][n]=true;
            		if(gameboard[m][n]==0)
            		{
            			arr[i]=new Array();
            			arr[i].push(m);
            			arr[i].push(n);
            			i++;
            		}	
            	}
            	m=j-1;
            	n=k+1;
            	if(m>=0 && n>=0 && n<len)
            	{
            		opening[m][n]=true;
            		if(gameboard[m][n]==0)
            		{
            			arr[i]=new Array();
            			arr[i].push(m);
            			arr[i].push(n);
            			i++;
            		}		
            	}
            	m=j;
            	n=k-1;
            	if(m>=0 && n>=0)
            	{
            		opening[m][n]=true;
            		if(gameboard[m][n]==0)
            		{
            			arr[i]=new Array();
            			arr[i].push(m);
            			arr[i].push(n);
            			i++;
            		}		
            	}
            	m=j;
            	n=k+1;
            	if(m>=0 && n>=0 && n<len)
            	{
            		opening[m][n]=true;
            		if(gameboard[m][n]==0)
            		{
            			arr[i]=new Array();
            			arr[i].push(m);
            			arr[i].push(n);
            			i++;
            		}			
            	}
            	m=j+1;
            	n=k-1;
            	if(n>=0 && m<length)
            	{
            		opening[m][n]=true;
            		if(gameboard[m][n]==0)
            		{
            			arr[i]=new Array();
            			arr[i].push(m);
            			arr[i].push(n);
            			i++;
            		}		
            	}
            	m=j+1;
            	n=k;
            	if(n>=0 && m<length)
            	{
            		opening[m][n]=true;
            		if(gameboard[m][n]==0)
            		{
            			arr[i]=new Array();
            			arr[i].push(m);
            			arr[i].push(n);
            			i++;
            		}			
            	}
            	m=j+1;
            	n=k+1;
            	if(m<length && n<len)
            	{
            		opening[m][n]=true;
            		if(gameboard[m][n]==0)
            		{
            			arr[i]=new Array();
            			arr[i].push(m);
            			arr[i].push(n);
            			i++;
            		}			
            	}
            	return arr;
	}
