# Generative AI 环境搭建

1. environment.yml文件声明环境

```shell
name: gen-ai
channels:
 - defaults
dependencies:
- python=3.11
- openai
- python-dotenv
```
2. 使用conda 创建环境

```shell
conda env create --name qpy30min --file .devcontainer/environment.yml

```
3. 激活环境

```shell
conda activate qpy30min
```

4. 配合Poetry 一起使用

```shell
poetry install
```