# Python Selenium 自动化测试框架

基于 Python + Selenium + Pytest + Allure 的 UI 自动化测试框架，采用 Page Object Model 设计模式。

## 项目结构
├── pages/ # 页面对象
│ ├── base_page.py
│ └── baidu_page.py
├── tests/ # 测试用例
│ └── test_baidu_search.py
├── utils/ # 工具模块
│ └── logger.py
├── data/ # 测试数据
│ └── test_data.json
├── reports/ # 测试报告
├── conftest.py # pytest fixture 和钩子
├── pytest.ini # pytest 配置（可选）
└── README.md

text

## 环境要求

- Python 3.8+
- Selenium
- Pytest
- allure-pytest

## 安装依赖
pip install selenium pytest allure-pytest

text

## 运行测试
pytest tests/test_baidu_search.py -v --alluredir=allure-results

text

## 生成 Allure 报告
allure generate allure-results -o allure-report --clean
allure open allure-report

text

## 说明

- 百度首页搜索框存在交互限制，统一使用 `execute_script` 操作。
- 默认超时时间为 30 秒，因练习环境可能弹出人机验证。
- 测试执行后自动截图并附加到 Allure 报告。

## 技术栈

- Python 3.11
- Selenium
- Pytest
- Allure
- POM 设计模式