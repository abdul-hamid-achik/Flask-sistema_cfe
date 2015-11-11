cfe.controller('loginCtrl', ['$http', '$scope', function($http, $scope){
	$scope.formData = {};



    $scope.submit = function(){

	    $http.post('/iniciar_sesion', $scope.formData)
	    .success(function (response) {
      console.log(response);

      if(!response.success){
          $scope.errorEmail = response.errors.correo;
          $scope.errorRpe = response.errors.rpe;
        } else {
          $scope.message = response.message;
        }


       }
     }

      $scope.crearUsuario = function() {
        // $http.post('/iniciar_sesion', $scope.formData)
        return {
          templateUrl: 'registrarUsuario.html'
        };
      
    }
  


     $scope.registrarUsuario = function(){
    	$http.post('/registrarUsuario', $scope.formData)
	    .success(function (response) {
	    	console.log(response);

        if(!response.success){
          $scope.ErrorNombre = response.errors.nombre;
          $scope.ErrorPuesto = response.errors.puesto;
          $scope.ErrorDepartamento = response.errors.departamento;
          $scope.ErrorEmail = response.errors.correo;
          $scope.ErrorZona = response.errors.zona;
          $scope.ErrorRpe = response.errors.rpe;

        } else {
          $scope.message = response.message;
        }


        }
  }

  }

}]);


 