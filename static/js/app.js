
angular.module('Sistema-cfe', [])
    .controller('competenciasCtrl', function ($scope, $http) {
    function get_existentes(){
      $scope.competencias_existentes = [];
      $http.post('/get_competencias/existentes', 
      { 
        colega : $scope.colega,
        tipo : 'Existente'
      }).success(function(response){
        $scope.competencias_existentes = response;
         
      });

     
    }

    function get_inexistentes(){
      $scope.competencias_inexistentes = [];
      $http.post('/get_competencias/inexistentes', 
      { 
        colega : $scope.colega,
        tipo : 'Inexistente'
      }).success(function(response){
        $scope.competencias_inexistentes = response;
        $scope.com = response.length + $scope.competencias_existentes.length;
        $scope.lista = [];
        for(var y = 0; y < $scope.competencias_inexistentes.length; y++){
          $scope.lista.push($scope.competencias_inexistentes[x]);
          console.log($scope.competencias_inexistentes);
        } 
        for(var x = 0; x < $scope.competencias_existentes.length; x++){
          $scope.lista.push($scope.competencias_existentes[x]);

          console.log($scope.competencias_existentes[x]);
        } 
        console.log($scope.lista);
         for(var i = 0; i <= $scope.competencias.length;  i++){
          for(var j = 0; j <= $scope.com; j++){
            console.log($scope.competencias[i]['nombre'] + " " + $scope.competencias_inexistentes[j]['nombre']);
              if($scope.competencias[i]['nombre'] == $scope.lista[j]['nombre']){
                $scope.competencias.splice(i,1);
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

        alert(comp);
        $http.post('/evaluando', {
          colega : $scope.colega,
          competencia : $scope.competencia_actual,
          tipo : 'Existente'
        }).success(function(response){
          console.log(response);
        });

        $scope.competencias_existentes.push(comp);
        borrarTitulo()
        get_existentes();
    }
    
    
    $scope.no = function(){
        var comp = $('h1').html();
        alert(comp);
        $http.post('/evaluando', {
          colega : $scope.colega,
          competencia : $scope.competencia_actual,
          tipo : 'Inexistente'
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

