cfe.controller('colegasCtrl', function($scope,$http,$window){

  function buscarColega(seleccionado, lista, caso){
      console.log('buscar colega');
      for(i = 0; i <= lista.length; i++){
      try{
        if(seleccionado==lista[i].rpe){
            switch(caso){
              case "Colegas":
              try{

                  var index = $scope.colegas.indexOf(lista[i]);
                  if($scope.colegas_izq.length<3){
                    $scope.colegas_izq.push(lista[i]);
                  }
                  else{
                    $scope.colegas_der.push(lista[i]);
                  }

                  $scope.colegas.splice(index,1);
                }
                catch(err){
                }
              break;

              case "Subordinados":
                  $scope.subordinados_seleccionados.push(lista[i]);
                  var index = $scope.subordinados.indexOf(lista[i]);
                  $scope.subordinados.splice(index,1);
              break;

              case "Superiores":
                  $scope.superiores_seleccionados.push(lista[i]);
                  var index = $scope.superiores.indexOf(lista[i]);
                  $scope.superiores.splice(index,1);
              break;

            }
          }
      }
      catch(err){
      }
    }
  }

  $http.get('/numero_evaluadores').success(function(response){
    $scope.seleccionados = response.seleccionados;

  });
  $http.get('/usuario').success(function(response){
    $scope.usuario = response;
  });

  $http.get('/colegas').success(function(response){
    $scope.colegas =  response;
    for(j=0; j<$scope.seleccionados.length;j++){
        buscarColega($scope.seleccionados[j], $scope.colegas,"Colegas");
       }
  });

  $http.get('/get_superiores').success(function(response){

    $scope.superiores = response;
      for(j=0; j<$scope.seleccionados.length;j++){
        buscarColega($scope.seleccionados[j], $scope.superiores, "Superiores");
       }


  });

  $http.get('/get_subordinados').success(function(response){

    $scope.subordinados =  response;
    for(j=0; j<$scope.seleccionados.length;j++){
        buscarColega($scope.seleccionados[j], $scope.subordinados, "Subordinados");
       }

  });
  $http.get('/numero_evaluadores').success(function(response){
      $scope.suma = response.cantidad;
    });

  $scope.superiores_seleccionados = [];
  $scope.subordinados_seleccionados = [];
  $scope.colegas_izq=[];
  $scope.colegas_der=[];

  $scope.submit = function(colega, tipo){
    switch(tipo){

      case "colega":
        var index = $scope.colegas.indexOf(colega);
        $http.post('/puede_evaluarme', colega).success(function(response){
          evaluador = '#' +colega.rpe;
          $scope.colegas.splice(index, 1);
          if($scope.colegas_izq.length<3){
            $scope.colegas_izq.push(colega);
          }
          else{
            $scope.colegas_der.push(colega);
          }
          $(evaluador).remove();
        });

        break;

      case "superior":
        var index = $scope.superiores.indexOf(colega);
        $http.post('/puede_evaluarme', colega).success(function(response){
          evaluador = '#' +colega.rpe;
          $scope.superiores.splice(index, 1);
          $scope.superiores_seleccionados.push(colega);
          $(evaluador).remove();
        });
        break;

      case "subordinado":
        var index = $scope.subordinados.indexOf(colega);
        $http.post('/puede_evaluarme', colega).success(function(response){
          evaluador = '#' +colega.rpe;
          $scope.subordinados.splice(index, 1);
          $scope.subordinados_seleccionados.push(colega);
          $(evaluador).remove();
        });
        break;
  }

  }

  $scope.continuar = function(){
      $window.location.href = '/sistema';
  }

});