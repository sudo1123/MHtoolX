# MHtoolX v2.5.1 / 多功能交互式数学工具

[English](#english) | [中文](#chinese)

<a id="chinese"></a>

## 中文文档

### 项目简介

MHtoolX v2.5.1 是一个基于 Python 的命令行交互式数学计算工具，支持 **36+** 种数学功能，涵盖从基础算术到高级数学模型的广泛领域。该工具提供 **交互式菜单导航** 与 **结果导出功能**，适合教学、科研及学习用途。

### 功能特性

#### 🔢 基础数学运算

  - `2` - 计算算术平方根（逐次逼近法/牛顿迭代法）
  - `4` - 求n次幂
  - `5` - 四则运算（加、减、乘、除）
  - `14` - 计算阶乘
  - `20` - 计算排列组合

#### 🔍 数论与整数运算

  - `1` - 生成质数表（普通方法/埃式筛法）
  - `17` - 质因数分解
  - `18` - 计算GCD与LCM
  - `23` - 质数检测
  - `6` - 生成斐波那契数列
  - `7` - 计算黄金分割率

#### 📊 统计与数据分析

  - `9` - 统计功能（平均值、加权平均值、方差、标准差、中位数、众数）
  - `11` - 考试成绩数据整理

#### 📐 几何与三角学

  - `15` - 极坐标转换
  - `24` - 向量模长计算
  - `25` - 计算任意三角形面积
  - `26` - 向量点乘
  - `21` - 计算三角函数值
  - `22` - 弧度角度制转换

#### 🧮 代数与方程求解

  - `13` - 求解二次方程
  - `28` - 计算整数系数多项式的有理数解
  - `36` - **方程求解（基于牛顿迭代法求数值解）**

#### ∫ 微积分与高级数学

  - `29` - 计算数值积分
  - `33` - 对数计算（自然对数和一般对数，使用泰勒展开法）
  - `34` - 计算数值导数

#### 📈 矩阵与线性代数

  - `30` - 三阶方阵行列式计算
  - `31` - 矩阵运算（加法、减法、乘法、转置）

#### 💰 金融与数学模型

  - `32` - 常见数学模型计算（复利计算、半衰期计算、人口增长模型）
  - `8` - 找零程序（贪心算法）

#### 🔄 进制与编码转换

  - `19` - 十进制转二进制
  - `27` - 十进制转十六进制

#### 🎨 图形绘制功能

  - `10` - 绘制函数图像（一次/二次函数）
  - `12` - 绘制三角函数图像（几何法/代数法）
  - `35` - 任意函数绘图（基于Matplotlib引擎）

#### 🔤 文本与文件操作

  - `16` - 字符串频数统计&定位

#### ⚙️ 系统与工具命令

  - `timer` - 启动计时器
  - `version` - 查看版本
  - `cs` - 清空屏幕
  - `menu` - 查看分页菜单
  - `amenu` - 查看所有功能列表
  - `language` - 修改语言
  - `exit` - 退出程序

#### 💾 数据管理命令

  - `rr` - 查看历史计算结果
  - `er` - 导出历史计算结果
  - `cr` - 清空历史计算结果
  - `rh` - 查看操作历史
  - `eh` - 导出操作历史
  - `ch` - 清空操作历史

### 运行环境

**Python 版本:** ≥ 3.8

**依赖模块**：

```python
turtle
math
decimal
json
time
random
os
sys
fractions
collections
curses/msvcrt
matplotlib
```

### 使用方法

#### 1️⃣ 下载程序

下载 `MHtoolX-v2.5.1.py` 和 `translation.json` 文件

#### 2️⃣ 运行程序

```bash
python MHtoolX-v2.5.1.py
```

#### 3️⃣ 使用交互命令

程序启动后会进行初始配置并自动检测版本记录。配置完成后，输入功能编号（如 `36`）或命令即可使用。

### 更新日志

#### v2.5.1 主要更新 (代码健壮性与逻辑重构):

  - **版本记录逻辑重构**：重新设计了 `version` 自动记录函数，采用标准的 JSON 列表操作（`append`）替代了旧版的字符串解析逻辑，彻底解决了可能导致数据文件结构损坏的问题。
  - **图形管理优化**：引入 `reset_turtle()` 机制，在每次调用绘图功能前重置 Turtle 状态，确保多次绘图时界面的稳定。
  - **异常处理增强**：优化了 `history` 和 `saved` 等文件操作函数，增加了对 JSON 解码错误和文件缺失的捕获，提升了程序在复杂环境下的存活率。

#### v2.5.0 主要更新 (新功能与自动化):

  - **新增方程求解功能**：添加功能 36，支持输入方程的左右两边表达式，通过牛顿迭代法求取指定初始值附近的数值解。
  - **版本自动登记**：新增启动时自动向 `history.json` 和 `result.json` 登记当前版本号的功能。



<a id="english"></a>

## English Documentation

### Project Introduction

MHtoolX v2.5.1 is a Python-based command-line interactive mathematical calculation tool supporting **36+** mathematical functions, covering a wide range from basic arithmetic to advanced mathematical models. The tool provides **interactive menu navigation** and **result export functionality**, suitable for teaching, research, and learning purposes.

### Features

#### 🔢 Basic Mathematical Operations

  - `2` - Calculate arithmetic square root (successive approximation / Newton's method)
  - `4` - Calculate nth power
  - `5` - Four arithmetic operations (addition, subtraction, multiplication, division)
  - `14` - Calculate factorial
  - `20` - Calculate permutations and combinations

#### 🔍 Number Theory & Integer Operations

  - `1` - Generate prime number table (general method / Sieve of Eratosthenes)
  - `17` - Prime factorization
  - `18` - Calculate GCD and LCM
  - `23` - Prime number detection
  - `6` - Generate Fibonacci sequence
  - `7` - Calculate golden ratio

#### 📊 Statistics & Data Analysis

  - `9` - Statistical functions (mean, weighted mean, variance, standard deviation, median, mode)
  - `11` - Exam score data processing

#### 📐 Geometry & Trigonometry

  - `15` - Polar coordinate conversion
  - `24` - Vector magnitude calculation
  - `25` - Calculate area of any triangle
  - `26` - Vector dot product
  - `21` - Calculate trigonometric function values
  - `22` - Radian-degree conversion

#### 🧮 Algebra & Equation Solving

  - `13` - Solve quadratic equations
  - `28` - Calculate rational solutions for integer-coefficient polynomials
  - `36` - **Equation Solving (Numerical solution via Newton's method)**

#### ∫ Calculus & Advanced Mathematics

  - `29` - Calculate numerical integration
  - `33` - Logarithm calculation (natural logarithm and general logarithm using Taylor expansion)
  - `34` - Calculate numerical derivative

#### 📈 Matrices & Linear Algebra

  - `30` - Calculate determinant of 3x3 matrix
  - `31` - Matrix operations (addition, subtraction, multiplication, transpose)

#### 💰 Financial & Mathematical Models

  - `32` - Common mathematical model calculations (compound interest calculation, half-life calculation, population growth model)
  - `8` - Change-making program (greedy algorithm)

#### 🔄 Base & Encoding Conversion

  - `19` - Decimal to binary conversion
  - `27` - Decimal to hexadecimal conversion

#### 🎨 Graphing Functions

  - `10` - Plot function graphs (linear/quadratic functions)
  - `12` - Plot trigonometric function graphs (geometric/algebraic method)
  - `35` - Arbitrary function plotting (based on Matplotlib engine)

#### 🔤 Text & File Operations

  - `16` - String frequency statistics & positioning

#### ⚙️ System & Tool Commands

  - `timer` - Start timer
  - `version` - View version
  - `cs` - Clear screen
  - `menu` - View paginated menu
  - `amenu` - View all function list
  - `language` - Change language
  - `exit` - Exit program

#### 💾 Data Management Commands

  - `rr` - View historical calculation results
  - `er` - Export historical calculation results
  - `cr` - Clear historical calculation results
  - `rh` - View operation history
  - `eh` - Export operation history
  - `ch` - Clear operation history

### Runtime Environment

**Python Version:** ≥ 3.8

**Dependency Modules:**

```python
turtle
math
decimal
json
time
random
os
sys
fractions
collections
curses/msvcrt
matplotlib
```

### Usage

#### 1️⃣ Download the Program

Download `MHtoolX-v2.5.1.py` and `translation.json` files

#### 2️⃣ Run the Program

```bash
python MHtoolX-v2.5.1.py
```

#### 3️⃣ Use Interactive Commands

After startup, the program will perform initial configuration and automatically detect version records. Once configuration is complete, enter a function number (e.g., `36`) or command to use.

### Update Log

#### v2.5.1 Major Updates (Code Robustness & Logic Refactoring):

  - **Version Tracking Refactor**: Redesigned the `version` auto-recording function using standard JSON list operations (`append`) instead of the old string parsing logic, thoroughly resolving issues that could lead to data file structure corruption.
  - **Graphics Optimization**: Introduced `reset_turtle()` mechanism to reset Turtle state before each plotting function call, ensuring interface stability during multiple plots.
  - **Enhanced Exception Handling**: Optimized `history` and `saved` file operation functions, adding catches for JSON decoding errors and missing files, improving program survivability in complex environments.

#### v2.5.0 Major Updates (New Features & Automation):

  - **New Equation Solver**: Added Function 36, supporting input of left and right side expressions of an equation to find numerical solutions near a specified initial value using Newton's method.
  - **Auto Version Logging**: Added functionality to automatically log the current version number to `history.json` and `result.json` upon startup.
