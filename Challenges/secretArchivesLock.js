
function secretArchivesLock(lock, actions) {

var length=lock.length;
if(length==0)
{
	return lock;
}
var len=lock[0].length;
var i=0,j=0,k=0,m=0;
for(m=0;m<actions.length;m++)
{
	//console.log(actions);
	if(actions[m]=="R")
	{
		for(i=0;i<length;i++)
		{
			var x=lock[i];
			//console.log(x);
			count=0;
		var	fast="";
		var ar=[];
		var sum="";
		var second="";
			//console.log(x);
			for(j=0;j<len;j++)
			{
				if(x[j]!=".")
				{
					//console.log(x[j]);
				  ar.push(x[j]);
				}	
				else
				{
					count++;
				}

			}
			for(j=0;j<count;j++)
			{
				fast=fast+".";
			}
			for(j=0;j<ar.length;j++)
			{
				second=second+ar[j];
			}
			//console.log(fast);
			//console.log(ar);
			sum=fast+second;
			//console.log(sum);
			lock[i]=sum;
		}
		//console.log(lock);
	}
	if(actions[m]=="L")
	{
		for(i=0;i<length;i++)
		{
			var x=lock[i];
			//console.log(x);
			count=0;
		var	fast="";
		var ar=[];
		var sum="";
		var second="";
			//console.log(x);
			for(j=0;j<len;j++)
			{
				if(x[j]!=".")
				{
					//console.log(x[j]);
				  ar.push(x[j]);
				}	
				else
				{
					count++;
				}

			}
			for(j=0;j<count;j++)
			{
				fast=fast+".";
			}
			for(j=0;j<ar.length;j++)
			{
				second=second+ar[j];
			}
			//console.log(fast);
		//	console.log(ar);
			sum=second+fast;
			//console.log(sum);
			lock[i]=sum;
		}

	//console.log(lock);
	}
	if(actions[m]=="D")
	{
	var sum=[];
	var check=0;
	for(k=0;k<len;k++)
	{
		var ar=[];
		var count=0;
		for(i=0;i<length;i++)
		{	
			var x=lock[i];

			if(x[check]==".")
			{
				count++;
			}
			else{
				ar.push(x[check]);
			}

		}
	//	console.log(ar);
		for(j=0;j<count;j++)
		{
			sum.push(".");
		}
		for(j=0;j<ar.length;j++)
		{
			sum.push(ar[j]);
		}
		check++;
		
	}
	var arr2=[],val="";
	for(i=0;i<length;i++)
	{
		val="";
		var n=i;
		for(j=0;j<len;j++)
		{
			val=val+sum[n];
			n=n+length;
		}
		lock[i]=val;
		//console.log(val);
	}
//console.log(lock);
	}
//console.log(sum);
	if(actions[m]=="U")
	{
	var x;

	var sum=[];

	var check=0;
	for(k=0;k<len;k++)
	{
		var ar=[];
		var count=0;
		for(i=0;i<length;i++)
		{
			
			x=lock[i];
			if(x[check]==".")
			{
				count++;
			}
			else{
				ar.push(x[check]);
			}

		}
		for(j=0;j<ar.length;j++)
		{
			sum.push(ar[j]);
		}
		for(j=0;j<count;j++)
		{
			sum.push(".");
		}
		check++;
		//console.log(ar);
	}
	var arr2=[],val="";
		for(i=0;i<length;i++)
		{
			val="";
			var n=i;
			for(j=0;j<len;j++)
			{
				val=val+sum[n];
				n=n+length;
			}
			lock[i]=val;
			//console.log(val);
		}
//	console.log(lock);
	}
}
return lock;
//console.log(sum);
}
