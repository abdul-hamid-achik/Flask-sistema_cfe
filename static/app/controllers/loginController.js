cfe.controller('loginCtrl', ['$http', '$scope', '$window', function($http, $scope, $window){
	$scope.formData = {};
  $scope.form = { url: '/api/sesiones/entrar', entrar: "Entrar", registrarse : "Registrarse", bandera: false, mensaje: "Eres nuevo?" };
  $scope.registrarUsuario = function(){
    $scope.form.bandera = $scope.form.bandera == false ? 
    $scope.form = { url: '/api/usuarios/nuevo', entrar: "Registrarse", registrarse : "Entrar", bandera: true, mensaje: "Ya tienes cuenta?" }: 
    $scope.form = { url: '/api/sesiones/entrar', entrar: "Entrar", registrarse : "Registrarse", bandera: false, mensaje: "Eres nuevo?" };
  }

  $scope.enviar = function(){
    alert("asd");
      $http.post($scope.form.url, JSON.stringify($scope.formData), {headers: {'Content-Type': 'application/json'}})
      .success(function (respuesta){
        $window.location.href = '/#/sistema';
      }).error(function (respuesta){
        $scope.formData = {};
        $scope.form.entrar = "Intentar de nuevo?"
      });

  };

}]);


 