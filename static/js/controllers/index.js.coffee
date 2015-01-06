VancouverEagles.controller 'IndexCtrl', ['$scope', '$rootScope', 'User', '$location', '$timeout',
 ($scope, $rootScope, User, $location, $timeout) ->

  $rootScope.title = 'Registrations'
  $scope.registrations = []

  User.get 'registrations', []
  .then (registrations) ->
    $timeout -> $scope.registrations = registrations

  $scope.goTo = (registrationId) ->
    $location.path "/registration/#{registrationId}"
]
