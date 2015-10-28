cfe.filter('ordenar', function (){
  return function(string,key){
    try {
      var res = string.split(' ');
      if (res.length > 3){
        var output = res[res.length-2] + " " + res[res.length-1] +" " + res[0] + " " + res[1];
      }
      else{
        var output = res[res.length-1]+" " + res[0] + " " + res[1];
      }
      return output;
    }
    catch (err) {
      console.log('');
    }
    return null;

  }
});