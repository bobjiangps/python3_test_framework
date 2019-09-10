# python3_autotest_framework


### python3 autotest framework to test:


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
| | Devices managed by OpenSTF | √ |
| | Simulator | √ |
| | Emulator | √ |
| Windows | Desktop app | √ |
| API | Rest | √ |
| | Thrift | TBD |
| | SOAP | TBD |


Todo List:
- running by commandline, by config file --> Done
- pytest --> Done
- select any test case or test suite to run, or make your own group, not run something,etc --> Done
- run by tag or keyword or marker --> Done
- logging --> Done
- rerun failures, set times  --> Done
- screenshot  --> Done
- video during test  --> Done (ffmpeg)
- statistics for test results  --> Done
- email  --> Done
- page object  --> Done
- opencv to compare picutures or find some elements to easy to operate (if you don't want to use xpath,id,name) --> Done
- selenium webdriver  --> Done
- appium  --> Done
- integrate with openstf --> Done (currently android)
- automate restful api --> Done
- automate windows desktop application --> Done
- db for mysql, mongodb, redis -> mysql Done,
- activemq or else
- data driven --> Done
- link to jira and testlink
- multiple process --> Done
- distributed
- history storage
- web UI page to run test / show statistics by many kinds of types(module, time, etc)/show trend/give warning prompt  --> implement in another project


Environment:
> * run "pip install -r requirement.txt" to install python libraries


Note:
> * allure is beautiful but not choose it to show report. because it is not a single file, cannot send in email; the report is able to view by starting a server, but I don't think this is good for distributed test. I have a another web server to show same data and charts.
