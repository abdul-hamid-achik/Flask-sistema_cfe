cfe.controller('loginCtrl', ['$http', '$scope', function($http, $scope){
	$scope.formData = {};



    $scope.submit = function(){

	    $http.post('/iniciar_sesion', $scope.formData)
	    .success(function (response) {
      console.log(response);

      if(!response.success){
          $scope.errorEmail = response.errors.email;
          $scope.errorRpe = response.errors.rpe;
        } else {
          $scope.message = response.message;
        }


       }
     }
     $scope.registrarUsuario = function(){
    	$http.post('/registrarUsuario', $scope.formData)
	    .success(function (response) {
	    	console.log(response);

        }
  }

  }
  }
 


}]);



