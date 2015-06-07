
angular.module('Sistema-cfe', [])
    .controller('competenciasCtrl', function ($scope, $http) {


      $scope.competencias = [];
    function get_existentes(){
      $scope.competencias_existentes = [];
      $http.post('/get_competencias/existentes', 
      { 
        colega : $scope.colega,
        tipo : 'Existentes'
      }).success(function (response){
        $scope.competencias_existentes = response;
      });

     
    }

    function get_inexistentes(){
      $scope.competencias_inexistentes = [];
      $http.post('/get_competencias/inexistentes', 
      { 
        colega : $scope.colega,
        tipo : 'Inexistentes'
      }).success(function (response){
        $scope.competencias_inexistentes = response;

      });
    }
    function get_neutras(){

      $scope.competencias_neutras = [];
      $http.post('/get_competencias/neutras', 
      {
        colega: $scope.colega,
        tipo :'Neutras'

      }).success(function (response) {
        $scope.competencias_neutras = response; 
        
        for(i=0 ; i < $scope.competencias_neutras.length; i++){
          for(j=0; j< $scope.competencias.length; j++){
            if($scope.competencias_neutras[i].nombre==$scope.competencias[j].nombre){
              $scope.competencias.splice(j,1);
            }
          }
        }
      });
    }
    $http.get('/get_colegas_evaluar').success(function(response){
      $scope.colegas = response;

    });
    function getCompetencias(){
    $http.get('/get_competencias').success(function(response){

      $scope.competencias = response;


    });
  }

    $http.get('/usuario').success(function(response){
      $scope.usuario = response;
    })
    
    function borrarTitulo(guardar){
            guardar = guardar || "Competencias";
         $('#competencia-menu h1').empty();
         $('#competencia-menu h1').append(guardar);
    }

    $scope.remove = function($index) { 
      var guardar = $scope.competencias[$index];
      if ($scope.colega == null){
        alert('Selecciona a un colega para evaluar primero!');

      }
      else{
        $scope.competencia_actual = guardar;
        $scope.competencias.splice($index, 1);
          borrarTitulo(guardar.nombre);
      }
    }
    
    $scope.si = function(){
        var comp = $('h1').html();
        $http.post('/evaluando', {
          colega : $scope.colega,
          competencia : $scope.competencia_actual,
          tipo : 'Existentes'
        }).success(function(response){
          console.log(response);
        });

        $scope.competencias_existentes.push(comp);
        borrarTitulo()
        get_existentes();
    }
    
    
    $scope.no = function(){
        var comp = $('h1').html();
        $http.post('/evaluando', {
          colega : $scope.colega,
          competencia : $scope.competencia_actual,
          tipo : 'Inexistentes'
        }).success(function(response){
          console.log(response);
        });

        $scope.competencias_inexistentes.push(comp);
        borrarTitulo()
        get_inexistentes();
        
    }

    $scope.selectedValue = function(value){
      $scope.colega = value;

      getCompetencias();
      get_existentes(value);
      get_inexistentes(value);
      get_neutras(value);

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
}).filter('ordenar', function (){
  return function(string,key){
    try {
      var res = string.split(' ');
      if (res.length > 3){
        var output = res[res.length-2] + " " + res[res.length-1] +" " + res[0] + " " + res[1];
      } 
      else{
        var output = res[res.length-1]+" " + res[1] + " " + res[2];
      }
      return output;
    }
    catch (err) {
      console.log('');
    }
    return null;
    
  }
}).controller('graficaCtrl', function($scope){


}).controller('colegas', function($scope,$http,$window){
  
  $http.get('/usuario').success(function(response){
    $scope.usuario = response;
  });

  $http.get('/colegas').success(function(response){
    $scope.colegas =  response;
  });

  $http.get('/get_superiores').success(function(response){
    $scope.superiores =  response;
  });

  $http.get('/get_subordinados').success(function(response){
    $scope.subordinados =  response;
  });

  $scope.submit = function(colega){
    var index = $scope.colegas.indexOf(colega);
    $http.post('/puede_evaluarme', colega).success(function(response){
      evaluador = '#' +colega.rpe;
      
      $scope.colegas.splice(index, 1);
      $(evaluador).remove();
    });


  }
  $scope.continuar = function(){
    $window.location.href = '/sistema';
  }

});

