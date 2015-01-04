VancouverEagles.controller 'RegistrationCtrl', ['$scope', '$rootScope', 'User', '$timeout', '$routeParams', '$location',
 ($scope, $rootScope, User, $timeout, $routeParams, $location) ->

  index = parseInt($routeParams.registrationId, 10)
  $scope.data = {}

  if index
    $rootScope.title = 'Registration'
    $scope.formURL = '/form/readonly/registration'
    User.get 'registrations', []
    .then (registrations) ->
      $timeout -> $scope.data = registrations[index] or {}
  else
    $rootScope.title = 'New Registration'
    $scope.formURL = '/form/editable/registration'
    $scope.data = JSON.parse(localStorage.getItem('data') or '{}')

    deregister = $scope.$watch 'data', (data) ->
      localStorage.setItem('data', JSON.stringify(data))
    , true

    $scope.submit = ->
      deregister()
      User.add 'registrations', $scope.data
      .then (succeeded) ->
        $timeout -> $location.path '/registrations'
]
