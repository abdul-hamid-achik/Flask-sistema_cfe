cfe.controller('loginCtrl', ['$http', '$scope', function($http, $scope){
	$scope.formData = {};
    $scope.submit = function(){

	    $http.post('/iniciar_sesion', $scope.formData)
	    .success(function (response) {
	    	console.log(response);
	    });

    }


  }

    $scope.nuevoUsuario = function(){
    	$http.post('/registrarUsuario', $scope.formData)
	    .success(function (response) {
	    	console.log(response);
  }




<input type="text" placeholder="nombre" id="nombre" name="nombre" ng-model="formData.nombre">
        <input type="text" placeholder="puesto" id="puesto" name="puesto" ng-model="formData.puesto">
        <input type="text" placeholder="departamento" id="departamento" name="departamento" ng-model="formData.departamento"> 
        <input type="email" placeholder="correo" id="correo" name="correo" ng-model="formData.correo">
        <input type="text" placeholder="zona" id="zona" name="zona" ng-model="formData.zona">
        <input type="password" placeholder="rpe" id="password" name="password" ng-model="formData.password">




  }


  }


}]);