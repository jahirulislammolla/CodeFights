def removeDuplicateCharacters(str):
    x={}
    for i in str:
        if i not in x:
            x[i]=0
        x[i]+=1
    y=''
    for i in x:
        if x[i]==1:
            y+=i
    for i in str:
        if i in y:
            d+=i
    
#............
function removeDuplicateCharacters(str) {
    var a = str.split("");
    var o = [];
    for (var i = 0; i < a.length; i ++){
        if (a.indexOf(a[i]) === a.lastIndexOf(a[i])){
            o.push(a[i])
        }
    }
    return o.join("")
}

