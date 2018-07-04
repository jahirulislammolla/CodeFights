function firstNotRepeatingCharacter(s) {
     // var s="abacabad";
      var i=0;
      var p=0;
     
    for(i=0;i<s.length;i++)
    {
      var first_index=s.indexOf(s[i]);
      var last_index=s.lastIndexOf(s[i]);
      if(first_index==last_index)
      {
         p=s[i];
        return s[i];
      }
    }
    return "_";
    // console.log(p);
  //   console.log(s);
}
