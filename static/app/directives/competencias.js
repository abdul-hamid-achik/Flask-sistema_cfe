cfe.directive('competencias', function(){
	var restrict = 'EA';
	var template = '<div class="cuadro_competencias"><ol><li ng-repeat="competencia in competencias"><a href="/api/competencias/{{ competencia.id }}">{{ competencia.nombre }}</a></li></ol></div>';
	var controller = ['$scope', '$http', function($scope, $http){

		$http.get('/api/competencias/todas').success(function (respuesta){
			$scope.competencias = respuesta;
		});

	}];

	var link = function(scope, element, attributes){};

	return {
		restrict: restrict,
    	template: template,
    	controller: controller,
    	link: link
	}
});