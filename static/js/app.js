
angular.module('Sistema-cfe', [])
    .controller('competenciasCtrl', function ($scope, $http) {
    $scope.usuarios = [];
    
    
    function borrarTitulo(guardar){
            guardar = guardar || "Competencias"
         $('#competencia-menu h1').empty();
         $('#competencia-menu h1').append(guardar);
    }

    
    $scope.remove = function($index) { 
      var guardar = $scope.usuario.competencias.neutras[$index];
      $scope.usuario.competencias.neutras.splice($index, 1);
        borrarTitulo(guardar);
    }
    
    $scope.si = function(){
        var comp = $('h1').html();
        $scope.usuario.competencias.existentes.push(comp);
        borrarTitulo()
        
    }
    
    
    $scope.no = function(){
        var comp = $('h1').html();  
        $scope.usuario.competencias.inexistentes.push(comp);
        borrarTitulo();
        
        
    }
    $scope.selectedValue = function(value){
    }

    $scope.submit = function(event){
        var form = $('form');
        var values = {};
        $.each(form.serializeArray(), function(i, field){
            values[field.name] = field.value;
        });
        data = JSON.stringify(values);
        console.log(data);
        $http.post('/iniciar_sesion', values).success(function () {
          alert('success');
        });   
    }
    
}).filter('unique', function() {
   return function(collection, keyname) {
      var output = [], 
          keys = [];

      angular.forEach(collection, function(item) {
          var key = item[keyname];
          if(keys.indexOf(key) === -1) {
              keys.push(key);
              output.push(item);
          }
      });

      return output;
   }
}).controller('graficaCtrl', function($scope){


}).controller('colegas', function($scope,$http,$window){
  $http.get('/colegas').success(function(response){
    $scope.colegas =  response;
  });



  $scope.submit = function(colega){
    $http.post('/puede_evaluarme', colega).success(function(response){
      evaluador = '#' +colega.rpe 
      console.log(evaluador);
      $scope.colegas.splice(colega.id,1);
      $(evaluador).remove();
    });
  }
  $scope.continuar = function(){
    $window.location.href = '/sistema';
  }

});

