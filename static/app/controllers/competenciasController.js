 cfe.controller('competenciasCtrl', function ($scope, $http) {

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
    for (i = 0; i < $scope.colegas.length; i++){
      if(confirm('Deseas enviar la evaluacion de '+ $scope.colegas[i].nombre)){
          $http.post('/evaluando_neutras',{
            competencias:  $scope.competencias,
            colega : $scope.colegas[i],
            tipo : 'Neutras'
         });
        }
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

});