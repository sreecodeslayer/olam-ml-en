var pApp = angular.module('MalEng', [], function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
});

pApp.controller('MainController',['$scope', '$http', '$location', '$window',function($scope,$http,$location,$window){

	$scope.search = function(){
		$http({
			url:'/search',
			method:'GET',
			params:{'text':$scope.text},
			headers:{'Content-Type':'application/json'}
		})
		.then(function onSuccess(response){
			$scope.results = response.data.results;
			$scope.text = '';
			console.log($scope.results);
		},function onError(){

		});
	}

}]);