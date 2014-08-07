(function() {
	var app = angular.module('roto', []).
  		config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  });

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


	// playerController
	app.controller('PlayerController', [ '$scope', function($scope){
		this.players = playerList;
		this.myTeam = team;

		
		$scope.addPlayer = function(player, myteamlist, playerlist) {
    		myteamlist.push(player);
  		}
	}]);



	var playerList = [ 
		
		{
			rank: 1, name: 'Kevin Durant', price:	89, evilrank: 48.63
		},
		{
			rank: 2, name: 'LeBron James', price: 81.00, evilrank: 47.63
		},
		{
			rank: 3, name: 'Chris Paul', price: 74, evilrank: 46.76	
		},
		{
			rank: 4, name: 'Russell Westbrook', price: 55, evilrank: 44.38
		},
		{
			rank: 5, name: 'Deron Williams', price: 52, evilrank: 43.98	
		},
		{
			rank: 6, name: 'Kyrie Irving', price: 47, evilrank: 43.38
		},
		{
			rank: 7, name:	'Dwyane Wade', price:	44, evilrank: 42.91
		},
		{	
			rank: 8, name:	'Josh Smith', price:	43, evilrank:	42.76	
		},
		{
			rank: 9, name:	'Dwight Howard', price:	42, evilrank:	42.67	
		},
		{
			rank: 10, name:	'Kevin Love', price:	41, evilrank:	42.61	
		},
		{
			rank: 11, name:	'Kobe Bryant', price:	41, evilrank:	42.59	
		},
		{
			rank: 12, name:	'Carmelo Anthony', price:	41, evilrank:	42.5	
		},
		{
			rank: 13, name:	'DeMarcus Cousins', price:	41, evilrank:	42.49	
		},
		{
			rank: 14, name:	'Al Jefferson', price:	40, evilrank:	42.42	
		},
		{
			rank: 15, name:	'LaMarcus Aldridge', price:	38, evilrank:	42.17	
		},
		{
			rank: 16, name:	'Serge Ibaka', price: 37, evilrank:		42.07	
		},
		{
			rank: 17, name:	'Greg Monroe', price:	37, evilrank:	42.07	
		},
		{
			rank: 18, name:	'James Harden', price:	37, evilrank:	42.02	
		},
		{
			rank: 19, name:	'Ty Lawson', price:	36, evilrank:	41.97	
		},
		{
			rank: 20, name:	'Andrew Bynum', price:	36, evilrank:	41.87	
		}
	]
var team = [ 
			{
				rank: 1, name: 'Kevin Durant', price:	89, evilrank: 48.63
			}
		]
	
})();