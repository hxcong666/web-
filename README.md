# Python UI 自动化测试项目（Pytest + Selenium + Allure）

## 1. 项目背景
随着金融业务数字化转型的加速，系统功能迭代频繁，传统的手工测试已无法满足快速交付和质量保障的需求。为提高测试效率、降低人力成本、确保核心业务流程的稳定性，本项目应运而生。

本项目针对金融系统的核心业务场景（用户注册、登录、账户开通、额度申请与审核等），构建了一套基于 Page Object Model 设计模式的 Web UI 自动化测试框架，实现：
- **回归测试自动化**：覆盖前后台关键业务流程，支持快速回归验证
- **测试数据管理**：通过 JSON + Faker 实现测试数据的灵活配置与随机生成
- **问题快速定位**：集成日志记录、失败截图、Allure 报告，便于问题追溯
- **可维护性提升**：采用 POM 模式分离页面元素与业务逻辑，降低维护成本

---

## 2. 项目简介
本项目是一个基于 **Pytest + Selenium WebDriver + Page Object Model（POM）** 的 Web UI 自动化测试实践项目，覆盖了前台与后台的核心业务流程。

已覆盖的典型场景包括：
- 用户登录
- 用户注册
- 开通托管账户
- 额度申请
- 后台登录
- 后台额度审核

项目支持：
- 用例执行（Pytest）
- 日志记录（TimedRotatingFileHandler）
- 测试报告（Allure）
- 基础测试数据管理（JSON + Faker）

---

## 3. 技术栈
- Python 3.x
- Selenium
- Pytest
- Allure（allure-pytest + allure 命令行）
- Faker

---

## 4. 项目结构
```text
pythonProject8/
├─ base/                  # 页面基类（元素定位、点击、输入、截图、切窗、切 frame、下拉选择）
├─ data/                  # 测试数据
├─ img/                   # 失败或调试截图
├─ log/                   # 运行日志
├─ lx/                    # 练习脚本/示例脚本
├─ new_report/            # Allure HTML 报告输出目录
├─ page/                  # 页面对象层（POM）
├─ report/                # Allure 原始结果目录（pytest --alluredir 输出）
├─ script/                # 测试用例层
├─ cmd_allure.py          # 一键生成 Allure 报告脚本
├─ config.py              # 全局配置（环境地址、随机用户信息）
├─ conftest.py            # Pytest fixtures（浏览器与页面对象）
├─ pytest.ini             # Pytest 配置
└─ tools.py               # 工具类（驱动管理、日志工具、JSON 读取）
```

---

## 5. 运行前准备
### 5.1 安装依赖
建议先创建并激活虚拟环境，再安装依赖：

```bash
pip install pytest selenium allure-pytest faker
```

### 5.2 安装浏览器与驱动
项目默认使用 Chrome，并在以下文件中写死了驱动路径：
- `conftest.py`
- `tools.py`

默认路径为：
```text
D:/chromedriver-win64/chromedriver.exe
```

请根据本机环境修改为实际路径，或改造成环境变量读取。

### 5.3 安装 Allure 命令行
本项目生成 HTML 报告需要本机安装 allure 命令（非 Python 包）。
安装后在终端执行以下命令验证：

```bash
allure --version
```

---

## 6. 配置说明
### 6.1 测试环境地址
在 `config.py` 中维护：
- `BASE_URL`：前台地址
- `BACK_URL`：后台地址

### 6.2 Pytest 默认配置
`pytest.ini` 关键配置：
- 默认附加参数：`-s --alluredir report --clean-alluredir`
- 用例目录：`./script`
- 用例命名规范：`test*.py`、`Test*`、`test*`

---

## 7. 执行测试
在项目根目录执行：

```bash
pytest
```

如果仅执行某一个测试文件：

```bash
pytest script/test_01_login.py
```

---

## 8. 生成并查看 Allure 报告
### 8.1 方式一：使用脚本

```bash
python cmd_allure.py
```

脚本会执行：

```bash
allure generate ./report -o ./new_report --clean
```

### 8.2 方式二：手动命令

```bash
allure generate ./report -o ./new_report --clean
```

生成后可直接打开：
- `new_report/index.html`

---

## 9. 主要用例说明
- `script/test_01_login.py`：前台登录（成功/失败）
- `script/test_02_register.py`：前台注册
- `script/test_03_open_account.py`：开通托管账户
- `script/test_04_credit_application.py`：额度申请
- `script/test_05_back_login.py`：后台登录
- `script/test_06_credit_review.py`：后台额度审核

---

## 10. 常见问题
1. **浏览器驱动启动失败**
   - 检查 Chrome 与 chromedriver 版本是否匹配
   - 检查驱动路径是否正确

2. **allure 命令不可用**
   - 确认已安装 Allure Commandline
   - 确认 allure 已加入系统 PATH

3. **元素定位超时**
   - 检查测试环境是否可访问
   - 检查页面元素定位是否变化
   - 查看 `log/` 下日志与 `img/` 截图定位失败原因

---

## 11. 后续可优化方向
- 将驱动路径、账号、验证码等改为配置化（环境变量/.env）
- 增加 `requirements.txt` 或 `pyproject.toml` 管理依赖
- 增加测试分层标记（如 smoke/regression）
- 引入 CI 流水线（自动执行 + 自动产出报告）
