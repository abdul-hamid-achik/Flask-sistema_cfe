cfe.controller('loginCtrl', ['$http', '$scope', function($http, $scope){
	$scope.formData = {};
  $scope.form = { url: '/api/sesiones/entrar', entrar: "Entrar", registrarse : "Registrarse", bandera: false, mensaje: "Eres nuevo?" };
  $scope.registrarUsuario = function(){
    $scope.form.bandera = $scope.form.bandera == false ? 
    $scope.form = { url: '/api/usuarios/nuevo', entrar: "Registrarse", registrarse : "Entrar", bandera: true, mensaje: "Ya tienes cuenta?" }: 
    $scope.form = { url: '/api/sesiones/entrar', entrar: "Entrar", registrarse : "Registrarse", bandera: false, mensaje: "Eres nuevo?" };
  }

  $scope.enviar = function(){
      $http.post($scope.form.url, $scope.formData)
      .success(function (respuesta){
        $window.location.href = '/sistema';
      }).error(function (respuesta){
        $scope.formData = {};
        $scope.form.entrar = "Intentar de nuevo?"
      });

  };

}]);


 