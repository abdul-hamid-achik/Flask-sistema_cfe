cfe.controller('autoevalCtrl', function ($scope, $http){

  $http.get('/get_competencias').success(function(response){
    $scope.competencias = response;
  }); 

  $scope.selectedValue = function(competencia){
    $scope.competencia = competencia;
    $http.post('/get_preguntas', $scope.competencia
    ).success(function(response){
      $scope.preguntas = response;
    });
  }
  $scope.respuesta = function(value){
    $scope.respuesta = value;
  }

});