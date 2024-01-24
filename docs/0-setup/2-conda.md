# Conda 设置环境

Conda也是常用管理虚拟环境的一个工具，主要用在Python数字分析相关项目中

## 创建环境

```bash
 conda env create --name pyqa-30min --file .devcontainer/environment.yml
```

environment.yml 内容:

```yaml
name: pyqa-30min
channels:
 - defaults
dependencies:
- python=3.11
```

所有的dependencies都可以加在dependencies中,这里只表示是python 3.11版本，依赖都可以添加.


## 激活环境

```shell
conda activate pyqa-30min
```

## 查看所有的虚拟环境

```shell
conda env list
```

## 详细Conda命令

可以使用tldr查看比较详细的Conda命令

```shell
tldr conda
```

```shell
❯ tldr conda 

  conda

  Package, dependency and environment management for any programming language.
  Some subcommands such as conda create have their own usage documentation.
  More information: https://github.com/conda/conda.

  - Create a new environment, installing named packages into it:
    conda create --name environment_name python=3.9 matplotlib

  - List all environments:
    conda info --envs

  - Load an environment:
    conda activate environment_name

  - Unload an environment:
    conda deactivate

  - Delete an environment (remove all packages):
    conda remove --name environment_name --all

  - Install packages into the current environment:
    conda install python=3.4 numpy

  - List currently installed packages in current environment:
    conda list

  - Delete unused packages and caches:
    conda clean --all

```

## Conda+Poetry

poetry会自动使用conda的包管理器，所以poetry和conda可以同时使用。activate conda环境之后，运行poetry命令
可以进行依赖的安装等操作而没有任何影响.