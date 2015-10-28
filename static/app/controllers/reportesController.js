cfe.controller('reportesCtrl', function ($scope, $http, $window){

  $http.get('/reportes').success(function(response){
    $scope.datos = response;
  }); 

});