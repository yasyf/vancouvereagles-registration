VancouverEagles.controller 'LoginCtrl', ['$scope', '$rootScope', 'API', '$location', '$mdToast', '$timeout',
 ($scope, $rootScope, API, $location, $mdToast, $timeout) ->

  $rootScope.title = 'Login or Signup'
  $scope.data = {}
  $scope.submitting = false

  $scope.login = ->
    $scope.submitting = true
    API.post ['login', $scope.data.username], $scope.data
    .then (response) ->
      $mdToast.show($mdToast.simple().content(response.message))
      $scope.submitting = false
      unless response.error
        localStorage.setItem 'userId', response.userId
        $timeout ->
          $location.path '/register'
        , 500
]
