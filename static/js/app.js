
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

    function borrarTitulo(guardar, descripcion){
            guardar = guardar || "Competencias";
         $('#competencia-menu h1').empty();
         $('#competencia-descripcion p').empty();
         $('#competencia-menu h1').html(guardar);
         $('#competencia-descripcion p').html(descripcion)
    }

    $scope.remove = function($index) {
      var guardar = $scope.competencias[$index];
      if ($scope.colega == null){
        alert('Selecciona a un colega para evaluar primero!');

      }
      else{
        $scope.competencia_actual = guardar;
        $scope.competencias.splice($index, 1);
          borrarTitulo(guardar.nombre, guardar.descripcion);
      }
    }


  $scope.reportes = function(){
      $http.post('/evaluando_neutras',{
      competencias:  $scope.competencias,
      colega : $scope.colega,
      tipo : 'Neutras'
     }).success( function (response) {
        console.log(response);
      });


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
        borrarTitulo();
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
}).controller('colegas', function($scope,$http,$window){

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


    //else {
    //  var resultado = 10 - $scope.suma;
    //  console.log(resultado);
    //  alert("te falta seleccionar: " + resultado + " para continuar.");
   // }
  }

}).controller('reporte', function($scope,$http,$window)
{
  $http.get('/reporte').success(function(response){
    $scope.datos = response;
  });


});

