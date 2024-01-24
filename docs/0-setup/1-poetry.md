# Setup Project With Poetry

- Init Project
- Add Dep
- Build and Publish

## 1. Poetry Install

安装命令: 

```sh
pip install pipx -U
pipx install poetry
pipx ensurepath
```

## 2. Poetry 新建项目

```sh
poetry new pyqa-30min

```

## 3. 不同的代码folder结构:

- 没有src目录:
```
poetry-demo
├── pyproject.toml
├── README.md
├── poetry_demo
│   └── __init__.py
└── tests
    └── __init__.py
```
指定打包内容：
```sh
packages = [{include = "poetry_demo"}]
```

- 有src目录结构:

```sh
poetry-demo
├── pyproject.toml
├── README.md
├── src
│   ├── poetry_demo
│       └── __init__.py
└── tests
    └── __init__.py
```

```sh
packages = [{include = "poetry_demo"，from="src"}]
```

## 2. 安装依赖和依赖组(Dependency groups)

```sh
[tool.poetry.dependencies]  # main dependency group
httpx = "*"
pendulum = "*"
[tool.poetry.group.test.dependencies]
pytest = "^6.0.0"
pytest-mock = "*"
[tool.poetry.group.dev.dependencies]
pytest = "^6.0.0"
pytest-mock = "*"
```

- 安装依赖

```sh
poetry add httpx pendulum
```
- 安装分组依赖

```sh
poetry add pytest pytest-mock --group test
poetry add pytest pytest-mock --group dev

```
- 安装/删除分组
```sh
poetry install --without test,docs
poetry install --only main
poetry install --with docs
poetry remove mkdocs --group docs
```
- poetry.lock 文件: 锁定安装的依赖版本

>  Dependency synchronization ensures that the locked dependencies in the poetry.lock

```sh
poetry install --sync
```

## 3.poetry build and publish

```sh
poetry build
poetry publish
poetry publish -r my-repository
```
如何设置publish [credentials](https://python-poetry.org/docs/master/repositories/#configuring-credentials)

## 4. Poetry 常用命令

- 使用python
```sh
poetry env use /full/path/to/python
```
- 创建虚拟环境和获取环境信息
```sh
poetry shell
poetry env info

```
- 添加依赖

```sh
poetry add httpx
poetry add "httpx[all]"
```
- 安装

```sh
poetry install -vvv
```

- build和发布

```sh
poetry build
poetry install
```

## 4. 额外

- 添加github 依赖

```sh
[tool.poetry.dependencies]
python = ">=3.10,<3.12"
fluentpy = { git = "git@github.com:qa/fluentpy.git", branch = "main" }
```

- 其他详细内容参考官方网站

[python-poetry](https://python-poetry.org/)




