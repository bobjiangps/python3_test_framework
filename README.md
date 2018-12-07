# python3_autotest_framework

几年前曾经用python2写过测试框架用于公司内使用，现在看来里面有些东西已经老旧了，于是打算用python3系列重新写一个，延续以前的一些功能，并修改一些不足的地方。
### python3 autotest framework to test with:


| Type | Option | Support |
| :------:| :------: | :------: |
| Web Browser | Chrome | √ |
| | Firefox | √ |
| | IE | √ |
| | Edge | √ |
| | Safari | √ |
| | Simulate mobile browser | √ |
| Mobile Application | iOS | √ |
| | Android | √ |
| Windows | Desktop app | √ |
| API | Rest | √ |
| | Thrift | TBD |
| | SOAP | TBD |


list:
- running by commandline, by config file
- pytest + allure
- select any test case or test suite to run, or make your own group, not run something,etc
- run by tag
- logging
- screenshot + video during test
- statistics for test results
- email
- page object
- opencv to compare picutures or find some elements to easy to operate (if you don't want to use xpath,id,name)
- selenium webdriver
- appium
- automate windows desktop application
- db for mysql, mongodb, redis
- activemq or else
- file handler
- text handler
- link to jira and testlink
- multiple process
- distributed
- web UI page to run test / show statistics by many kinds of types(module, time, etc)/show trend/give warning prompt
- resource control