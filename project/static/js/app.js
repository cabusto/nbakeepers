
// changes {{ }} to [[ ]] for angular injection (so as not to interfer with flask)
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
	
	app.filter('avgByKey', function () {
    	return function (data, key) {
        if (typeof (data) === 'undefined' || typeof (key) === 'undefined') {
            return 0;
        }

        var sum = 0;
        for (var i = data.length - 1; i >= 0; i--) {
            sum += parseFloat(data[i][key]);
        }
		console.log("sum " + sum);
			
        return (sum / data.length).toFixed(2);
			
		};
    });
    
	// CONTROLLERS
	// playerController
	app.controller('PlayerController', [ '$http', '$scope', function($http, $scope){
		
		var rotoevil = this;
		rotoevil.players = [ ];
		rotoevil.myteamList = [ ];
		
		$scope.add = function(player) {
			// add to team list
            console.log("Adding " + player.name);	
			rotoevil.myteamList.push(player);
			console.log("Team size " + rotoevil.myteamList.length);
			// remove from player pool list
			$scope.remove(player, rotoevil.players);
		};
		
		$scope.remove = function(player, playerlist) {
			// if playerlist doesn't exist, we are removing from myteamList.
			// we will need to add back to player pool
			if (typeof playerlist === 'undefined') {
				playerlist = rotoevil.myteamList;
				rotoevil.players.splice(player.rank-1, 0, player);
			}
			// search for player in myTeamList
			var index = -1;
			for (var i = 0; i < playerlist.length; i++) {
				if (playerlist[i].name === player.name) {
					index = i;
					break;
				}
			}
			// at position index, remove 1 item
			playerlist.splice(index, 1);
			
			// add back to main list
		};
		
		$http.get('/rotoevil/players').success(function(data) {
			rotoevil.players = data.players;
			console.log(data.players[0]);
			
		});
		
	}]);
	
    
	app.controller('PanelController', function() {
		this.tab = 1;

		this.selectTab = function(setTab) {
			this.tab = setTab;
		}

		this.isSelected = function(checkTab) {
			return this.tab === checkTab;
		}
	});

})();