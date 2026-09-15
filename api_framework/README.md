# 接口自动化测试框架

基于 Python + Requests + Pytest + Allure 的接口自动化测试框架，支持多环境配置、数据驱动、请求重试和日志记录。

## 项目结构
api_framework/
├── config/ # 配置文件
│ ├── config_dev.json # 开发环境
│ └── config_prod.json # 生产环境
├── core/ # 核心模块
│ ├── config_manager.py # 配置管理
│ ├── logger.py # 日志封装
│ ├── request_client.py # 请求客户端
│ └── assert_utils.py # 断言工具
├── testcases/ # 测试用例
│ ├── test_github_users.py
│ └── test_github_users_data.py
├── data/ # 测试数据
│ └── users.json
├── logs/ # 日志输出
├── reports/ # 报告输出
├── conftest.py # 全局 fixture
└── README.md


## 技术栈

- Python 3.11
- Requests：HTTP 请求
- Pytest：测试框架
- Allure：测试报告
- JSON：配置与数据管理

## 核心特性

- **多环境配置**：通过环境变量 `TEST_ENV` 切换 `dev` / `prod`
- **请求封装**：统一处理 base_url、headers、timeout、重试、日志
- **断言工具**：状态码、字段存在性、值比较、类型检查
- **数据驱动**：从 JSON 读取测试数据，`@pytest.mark.parametrize` 驱动
- **Allure 报告**：feature/story/step 分层展示，请求响应自动附加
- **日志记录**：控制台输出 + 文件保存

## 安装依赖
pip install requests pytest allure-pytest



## 运行测试
cd api_framework
pytest testcases/ -v --alluredir=allure-results


## 切换环境
默认 dev 环境
pytest testcases/ -v

切换到 prod
$env:TEST_ENV="prod"
pytest testcases/ -v
Remove-Item Env:\TEST_ENV


## 生成 Allure 报告
allure serve allure-results


## 架构设计
┌─────────────────────────────────────────────┐
│ 测试用例层 │
│ testcases/test_.py │
│ （只关注业务逻辑，不关心底层实现） │
└──────────────────┬──────────────────────────┘
│ 依赖注入
▼
┌─────────────────────────────────────────────┐
│ 核心层 core/ │
│ ┌────────────┐ ┌────────────┐ │
│ │ RequestClient│ │ AssertUtils │ │
│ │ 请求封装 │ │ 断言工具 │ │
│ │ 重试/日志 │ │ 失败信息 │ │
│ └──────┬──────┘ └────────────┘ │
│ │ │
│ ┌──────▼──────┐ ┌────────────┐ │
│ │ConfigManager│ │ Logger │ │
│ │ 配置管理 │ │ 日志记录 │ │
│ └─────────────┘ └────────────┘ │
└──────────────────┬──────────────────────────┘
│ 读取
▼
┌─────────────────────────────────────────────┐
│ 资源层 │
│ config/.json data/*.json logs/ │
│ 环境配置 测试数据 日志输出 │
└─────────────────────────────────────────────┘


## 设计思路

1. **分层解耦**：测试用例层、核心层、资源层各司其职，修改配置不影响用例
2. **配置外置**：所有可变内容放在 JSON，代码只读不改
3. **请求复用**：所有请求走统一的 RequestClient，避免重复代码
4. **日志追踪**：每次请求和响应都有日志，出问题可回溯
5. **断言封装**：失败信息带期望值和实际值，定位更快
6. **可扩展**：新增测试只需在 testcases 下建文件，写用例，无需改核心代码

## 后续规划

- 支持 token 自动获取和刷新
- 增加 JSON Schema 校验
- 支持 CI/CD 集成（GitHub Actions）
- 增加数据库校验模块