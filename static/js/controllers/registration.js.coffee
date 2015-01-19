VancouverEagles.controller 'RegistrationCtrl', ['$scope', '$rootScope', 'User', '$timeout', '$routeParams', '$location', 'API',
 ($scope, $rootScope, User, $timeout, $routeParams, $location, API) ->

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
      API.post ['form', 'process', 'registration'],
        data: $scope.data
      .then (response) ->
        User.add 'registrations', response.data
      .then (succeeded) ->
        $timeout -> $location.path "/schedule/new"
]
