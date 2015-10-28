var cfe = angular.module('cfe', ['ngRoute']);

//rutas del app

cfe.config(function ($routeProvider){
  $routeProvider
  .when('/', {
    templateUrl: 'static/views/login.html',
    controller: 'loginCtrl'
  })
  .when('/seleccionar_colegas', {
    templateUrl: 'static/views/seleccionar_colegas.html',
    controller: 'colegasCtrl'
  })
  .when('/sistema', {
    templateUrl: 'static/views/sistema.html',
    controller: 'competenciasCtrl'
  })
  .when('/auto_evaluacion', {
    templateUrl: 'static/views/auto_evaluacion.html',
    controller: 'autoevalCtrl'
  })
  .when('/resultados', {
    templateUrl: 'static/views/reportes.html',
    controller: 'reportesCtrl'
  });

});