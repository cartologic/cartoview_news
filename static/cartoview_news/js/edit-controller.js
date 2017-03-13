/**
 * Created by kamal on 8/3/16.
 */
newsEditApp.controller('newsEditController', function ($scope, $http, newsId,
                                                       AppInstance, urls, $element, $q, $mdDialog, $filter) {
    if (newsId) {
        AppInstance.get({instanceId: newsId}).$promise.then(function (appInstance) {
            $scope.news = appInstance;
            $scope.configObj = JSON.parse(appInstance.config);
        });
    }
    else {
        $scope.news = new AppInstance({
            title: "",
            abstract: "",
            config: ""
        });
        $scope.configObj = {
            subTitle: "",
        };
    }
    $scope.save = function () {
        $scope.news.config = JSON.stringify($scope.configObj);
        if (newsId) {
            $scope.news.$update(function (res) {
                console.debug(res)
            })
        }
        else {
            $http.post("create/", $scope.news).then(function (res) {
                if (res.data.id) {
                    window.location = "../" + res.data.id + "/edit/"
                }
            })
        }


    };
});
