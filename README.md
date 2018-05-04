# test automation framework

[![Python](https://img.shields.io/badge/python-3.5%2B-green.svg)]()
[![MIT license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/BranRoyal/automation_framework/blob/master/LICENSE)

selenium 实现简单的 web 自动化测试框架

## Preparation

1. install selenium

```shell
pip install selenium
```

2. download web drivers for Firefox, Google Chrome & IE Explorer, you can find them in folder \tools 

3. put the driver into the folder where python is installed on your computer

## Run
1. the project uses Firefox on default

2. download and import this project into pycharm IDE, then run it

## Usage

1. the test scripts will be written under folder \testsuites. script name better begins with test_
2. write the test functions in each script, function name must begin with test_, function setUp() and tearDown() don't need modification。
3. give the chinese text as the parameter of function homepage.send_textarea() and the corresponding rating number in try block
4. finally, add the test case in TestRunner.py, see the cases already written

```shell
suite.addTest(className('functionName'))
```

## Structure

```
.
├── LICENSE
├── README.md
├── .idea
├── .gitignore
├── .gitattributes
├── config
├── framework
├── logs
├── pageobjects
├── screenshots
├── test_report
├── testsuites
└── tools
```

## License

Licensed under the [MIT License](https://github.com/BranRoyal/automation_framework/blob/master/LICENSE).
