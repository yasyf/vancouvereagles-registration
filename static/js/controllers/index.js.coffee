VancouverEagles.controller 'IndexCtrl', ['$scope', '$rootScope', 'User', '$location', '$timeout',
 ($scope, $rootScope, User, $location, $timeout) ->

  $rootScope.title = 'Registrations'
  $scope.registrations = []

  User.get 'registrations', []
  .then (registrations) ->
    $timeout -> $scope.registrations = registrations

  $scope.goTo = (action, registrationId) ->
    console.log "/#{action}/#{registrationId}"
    $location.path "/#{action}/#{registrationId}"
]
