var app = angular.module('smsViewerApp', []);

app.controller('mainCtrl', function ($scope, $http) {
    console.log("mainCtrl");

    $scope.smsList = [];

    $http.get("/api/sms/list").success(function (response) {
        $scope.smsList = response.data;
    });
});
