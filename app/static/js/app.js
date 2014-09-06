(function() {
	var app = angular.module('roto', []).
  		config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  });

	// FILTERS
	// Create the instant search filter
	app.filter('searchFor', function(){

		// All filters must return a function. The first parameter
		// is the data that is to be filtered, and the second is an
		// argument that may be passed with a colon (searchFor:searchString)

		return function(arr, searchString){

			if(!searchString){
				return arr;
			}

			var result = [];
			searchString = searchString.toLowerCase();

			// Using the forEach helper method to loop through the array
			angular.forEach(arr, function(player){
				if(player.name.toLowerCase().indexOf(searchString) !== -1){
					result.push(player);
				}
			});
			return result;
		};
	});
	
	// CONTROLLERS
	// playerController
	app.controller('PlayerController', [ '$http', function($http){
		
		var rotoevil = this;
		rotoevil.players = [ ];
		
		$http.get('/rotoevil/players').success(function(data) {
			rotoevil.players = data.players;
			console.log(data.players[0]);
			
		});
	}]);
})();