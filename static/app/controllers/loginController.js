cfe.controller('loginCtrl', ['$http', '$scope', function($http, $scope){
	$scope.formData = {};
    $scope.submit = function(){
	    $http.post('/iniciar_sesion', $scope.formData)
	    .success(function (response) {
	    	console.log(response);
	    });

    }
$scope.salirSESION = function(){
    	$http.post('/cerrar_sesion', $scope.formData)
	    .success(function (response) {
	    	console.log(response);
  }

  }

    $scope.nuevoUsuario = function(){
    	$http.post('/nuevoUsuario', $scope.formData)
	    .success(function (response) {
	    	console.log(response);
  }

  }


}]);