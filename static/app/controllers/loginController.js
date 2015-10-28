cfe.controller('loginCtrl', ['$http', '$scope', function($http, $scope){
	$scope.formData = {};
    $scope.submit = function(){
	    $http.post('/iniciar_sesion', $scope.formData)
	    .success(function (response) {
	    	console.log(response);
	    });
    }



}]);