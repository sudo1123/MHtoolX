# MHtoolX v2.4.0 / 多功能交互式数学工具

[English](#english) | [中文](#chinese)

<a name="chinese"></a>

## 中文文档

### 项目简介

MHtoolX v2.4.0 是一个基于 Python 的命令行交互式数学计算工具，支持35+种数学功能，涵盖从基础算术到高级数学模型的广泛领域。该工具提供 **交互式菜单导航** 与 **结果导出功能**，适合教学、科研及学习用途。

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

>     - 若运行环境不支持 `turtle`，相关图形功能会自动禁用。
>     - `matplotlib` 为功能35的必需依赖，若未安装，使用该功能时会提示 `pip install matplotlib`。

### 使用方法

#### 1️⃣ 下载程序

下载 `MHtoolX-v2.4.0.py` 和 `translation.json` 文件

#### 2️⃣ 运行程序

```bash
python MHtoolX-v2.4.0.py
```

#### 3️⃣ 使用交互命令

程序启动后会提示进行初始配置：

  - 选择界面语言（中文/英文）
  - 是否保存操作历史
  - 是否启用计算结果保存功能
  - 是否启用图像保存功能
  - 是否启用number_saved计数功能

配置完成后，输入功能编号或命令即可使用相应功能。

### 数据与历史记录管理

程序自动在运行目录下生成以下配置文件：

| 文件名 | 功能说明 |
|--------|-----------|
| `result.json` | 保存历史计算结果 |
| `history.json` | 保存用户操作记录 |
| `number saved.json` | 已保存结果计数（可选启用） |
| `config.json` | 程序配置设置（历史保存、结果保存、图像保存等） |
| `translation.json` | 语言翻译字典 |

### 使用示例

#### 绘制任意函数图像（功能35）

```
请输入指令: 35
您正在使用任意函数绘图功能
请输入函数表达式，使用x作为变量(可包括常数和特定函数，输入cons可查看所有支持的科学常数，输入func可查看所有支持的函数)
示例：x**2 + 2*x + 1, math.sin(x), math.exp(x)
函数 f(x) = x**2
请设定 x 最小值: -10
请设定 x 最大值: 10
请设定 y 最小值: 0
请设定 y 最大值: 100
请选择坐标轴样式(1代表十字形，2代表框形): 1
请设定步长: 0.1
绘制中...
[弹窗显示 y = x**2 的函数图像]
```

#### 计算数值导数

```
请输入指令: 34
您正在使用计算数值导数功能
请输入函数表达式，使用x作为变量(可包括常数和特定函数，输入cons可查看所有支持的科学常数，输入func可查看所有支持的函数)
示例：x**2 + 2*x + 1, math.sin(x), math.exp(x)
函数 f(x) = x**2 + 2*x + 1
请输入待求数值导数的函数在 x 轴上的求导位置: 2
请输入您所需要的精度（10的倍数，越小越结果精确）: 1000
f'(2)=6.000000000000003
```

#### 修改语言

```
请输入指令: language
Select language / 选择语言 (1 for English, 2 for 中文): 1
Language changed / 语言已更改
```

### 文件结构

```
.
├── MHtoolX-v2.4.0.py    # 主程序文件
├── translation.json      # 语言翻译配置
├── config.json           # 程序配置（自动生成）
├── history.json          # 操作历史（自动生成）
├── result.json           # 计算结果（自动生成）
└── number saved.json     # 保存计数（可选生成）
```

### 许可证

MIT License © 2025-2026 QU QI

### 作者

**作者:** QU QI  
**版本:** MHtoolX v2.4.0  
**发布日期:** 20260412

### 更新日志

#### v2.4.0 主要更新 (新增功能与绘图引擎升级):

  - **新增任意函数绘图功能**：添加功能35，基于Matplotlib引擎实现高性能函数图像绘制，支持自定义定义域、值域、坐标轴样式与步长。
  - **函数解析增强**：优化 `function_calculation` 函数，增加对无穷大 (inf) 和非数字 (nan) 结果的异常处理，避免绘图引擎崩溃。
  - **绘图配置优化**：为Matplotlib绘图引擎添加网格线默认开启选项，提升图像可读性。
  - **菜单结构调整**：功能菜单扩展至5页以容纳新功能。

#### v2.3.0 主要更新 (错误修复与功能完善):

  - **拼写错误修复**：修正了功能菜单中 "language" 命令的拼写错误（从 "languange" 修正为 "language"）。
  - **彩蛋功能**：新增隐藏命令 "truth"，输入后显示二进制哲学答案 "101010"。
  - **翻译优化**：功能25（计算任意三角形面积）中，三边计算模式的精度提示现在使用专门的翻译键 "25_acc_recommendation"，提供更准确的翻译。
  - **图像保存配置修复**：修复了首次启动时选择禁用图像保存功能时写入错误配置文件的问题（从写入 `picture_choice.json` 修正为写入 `config.json`）。

#### v2.2.2 主要更新 (错误修复):

  - **正确性修复 (功能 9)**：修复了在统计功能(模式6)中，当数据包含多个众数且频率相同时（例如 [1, 1, 2, 2]），程序错误地报告"不存在众数"的问题。

#### v2.2.1 主要更新 (错误修复)：

  - **稳定性修复 (功能 31)**：修复了在矩阵运算（加、减、乘）后，因翻译键错误导致程序崩溃的问题。
  - **正确性修复 (功能 9)**：修复了在统计功能中，当数据个数为奇数时，中位数无法被正确打印或保存的错误。

#### v2.2.0 主要更新：

  - **新增数值导数计算功能**：添加功能34，使用中心差分法计算任意函数的数值导数。
  - **微积分工具完善**：与数值积分功能形成完整的微积分工具集。

#### v2.1.1 主要更新：

  - **跨平台计时器**：使用 `curses` 和 `msvcrt` 模块替代 `keyboard`，支持Linux、macOS和Windows。
  - **语言切换优化**：修改语言后无需重启程序，菜单即时刷新。
  - **翻译改进**：修复了翻译键的格式问题，提升多语言体验。

#### v2.1.0 主要更新：

  - **矩阵转置功能**：在功能31中新增矩阵转置运算。
  - **语言切换优化**：修改语言后自动提示重启程序。
  - **翻译更新**：同步更新了中英文翻译文件。

#### v2.0.0 主要更新：

  - **多语言支持**：添加完整的英文翻译系统。
  - **语言切换**：无需重启即可实时切换语言。

-----

<a name="english"></a>

## English Documentation

### Project Introduction

MHtoolX v2.4.0 is a comprehensive Python-based command-line interactive mathematical calculation tool supporting 35+ mathematical functions, covering a wide range from basic arithmetic to advanced mathematical models. The tool provides **interactive menu navigation** and **result export functionality**, suitable for teaching, research, and learning purposes.

### Features

#### 🔢 Basic Mathematical Operations

  - `2` - Calculate square root (successive approximation/Newton's method)
  - `4` - Calculate power
  - `5` - Arithmetic operations (addition, subtraction, multiplication, division)
  - `14` - Calculate factorial
  - `20` - Calculate permutations and combinations

#### 🔍 Number Theory & Integer Operations

  - `1` - Generate prime number table (normal method/sieve method)
  - `17` - Prime factorization
  - `18` - Calculate GCD and LCM
  - `23` - Prime number check
  - `6` - Generate Fibonacci sequence
  - `7` - Calculate golden ratio

#### 📊 Statistics & Data Analysis

  - `9` - Statistical functions (average, weighted average, variance, standard deviation, median, mode)
  - `11` - Exam score analysis

#### 📐 Geometry & Trigonometry

  - `15` - Polar coordinates conversion
  - `24` - Calculate vector magnitude
  - `25` - Calculate triangle area
  - `26` - Vector dot product
  - `21` - Calculate trigonometric values
  - `22` - Radian-degree conversion

#### 🧮 Algebra & Equation Solving

  - `13` - Solve quadratic equation
  - `28` - Find rational roots of polynomial

#### ∫ Calculus & Advanced Mathematics

  - `29` - Numerical integration
  - `33` - Logarithm calculation (natural and general logarithms using Taylor expansion)
  - `34` - Compute numerical derivatives

#### 📈 Matrix & Linear Algebra

  - `30` - Calculate 3x3 matrix determinant
  - `31` - Matrix operations (addition, subtraction, multiplication, transposition)

#### 💰 Finance & Mathematical Models

  - `32` - Mathematical models (compound interest, half-life, population growth)
  - `8` - Change making (greedy algorithm)

#### 🔄 Base & Encoding Conversion

  - `19` - Decimal to binary conversion
  - `27` - Decimal to hexadecimal conversion

#### 🎨 Graphing Functions

  - `10` - Draw function graphs (linear/quadratic)
  - `12` - Draw trigonometric function graphs (geometric/algebraic method)
  - `35` - Plot arbitrary function (Powered by Matplotlib engine)

#### 🔤 Text & File Operations

  - `16` - String frequency statistics & positioning

#### ⚙️ System & Utility Commands

  - `timer` - Start timer 
  - `version` - View version
  - `cs` - Clear screen
  - `menu` - View paged menu
  - `amenu` - View all functions list
  - `language` - Change language
  - `exit` - Exit program

#### 💾 Data Management Commands

  - `rr` - View calculation history results
  - `er` - Export calculation history
  - `cr` - Clear calculation history
  - `rh` - View operation history
  - `eh` - Export operation history
  - `ch` - Clear operation history

### Requirements

**Python Version:** ≥ 3.8

**Required Modules**:

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

>     - If the runtime environment doesn't support `turtle`, related graphics functions will be automatically disabled.
>     - `matplotlib` is a required dependency for function 35. If not installed, the program will prompt you to run `pip install matplotlib` when using this feature.

### Usage

#### 1️⃣ Download Program

Download `MHtoolX-v2.4.0.py` and `translation.json` files

#### 2️⃣ Run Program

```bash
python MHtoolX-v2.4.0.py
```

#### 3️⃣ Use Interactive Commands

After startup, the program will prompt for initial configuration:

  - Select interface language (Chinese/English)
  - Whether to save operation history
  - Whether to enable result saving
  - Whether to enable image saving
  - Whether to enable number_saved counting function

After configuration, enter function numbers or commands to use corresponding functions.

### Data & History Management

The program automatically generates the following configuration files in the running directory:

| File Name | Function Description |
|-----------|---------------------|
| `result.json` | Saves calculation history results |
| `history.json` | Saves user operation records |
| `number saved.json` | Saved results count (optional) |
| `config.json` | Program configuration settings (history saving, result saving, image saving, etc.) |
| `translation.json` | Language translation dictionary |

### Examples

#### Plot Arbitrary Function (Function 35)

```
Enter command: 35
You are using Plot arbitrary function function
Please enter function expression using x as variable (can include constants and specific functions, enter 'cons' to view supported constants, 'func' to view supported functions)
Example: x**2 + 2*x + 1, math.sin(x), math.exp(x)
Function f(x) = x**2
Set x-axis minimum: -10
Set x-axis maximum: 10
Set y-axis minimum: 0
Set y-axis maximum: 100
Select axes style (1 for cross, 2 for box): 1
Set step size: 0.1
Drawing...
[A window pops up showing the graph of y = x**2]
```

#### Compute Numerical Derivatives

```
Enter command: 34
You are using Computing numerical derivatives function
Please enter function expression using x as variable (can include constants and specific functions, enter 'cons' to view supported constants, 'func' to view supported functions)
Example: x**2 + 2*x + 1, math.sin(x), math.exp(x)
Function f(x) = x**2 + 2*x + 1
Please enter the differentiation point on the x-axis for the function whose numerical derivative is to be calculated: 2
Please enter the required precision (multiple of 10, smaller values yield more accurate results): 1000
f'(2)=6.000000000000003
```

#### Change Language

```
Enter command: language
Select language / 选择语言 (1 for English, 2 for 中文): 1
Language changed / 语言已更改
```

### File Structure

```
.
├── MHtoolX-v2.4.0.py    # Main program file
├── translation.json      # Language translation configuration
├── config.json           # Program configuration (auto-generated)
├── history.json          # Operation history (auto-generated)
├── result.json           # Calculation results (auto-generated)
└── number saved.json     # Save count (optional)
```

### License

MIT License © 2025-2026 QU QI

### Author

**Author:** QU QI  
**Version:** MHtoolX v2.4.0  
**Release Date:** 20260412

### Update Log

#### v2.4.0 Major Updates (New Feature & Graphics Engine Upgrade):

  - **New Arbitrary Function Plotting**: Added Function 35, implementing high-performance function graph drawing based on the Matplotlib engine. Supports custom domain, range, axis styles, and step size.
  - **Enhanced Function Parsing**: Optimized the `function_calculation` function by adding exception handling for infinite (inf) and non-numeric (nan) results to prevent crashes in the plotting engine.
  - **Plotting Configuration Optimization**: Enabled the default grid line option for the Matplotlib plotting engine to improve graph readability.
  - **Menu Structure Adjustment**: Expanded the function menu to 5 pages to accommodate the new feature.

#### v2.3.0 Major Updates (Bug Fixes & Feature Enhancement):

  - **Spelling Correction**: Fixed a typo in the function menu where the "language" command was misspelled as "languange".
  - **Easter Egg Feature**: Added a hidden command "truth" that displays the binary philosophical answer "101010".
  - **Translation Optimization**: In function 25 (calculate triangle area), the precision prompt for the three-sides calculation mode now uses the dedicated translation key "25_acc_recommendation" for more accurate translations.
  - **Image Saving Configuration Fix**: Fixed an issue where selecting to disable image saving during first launch wrote to the wrong configuration file (corrected from writing to `picture_choice.json` to writing to `config.json`).

#### v2.2.2 Major Updates (Bug Fix):

  - **Correctness Fix (Function 9)**: Fixed a bug in Statistics (mode 6) where the program incorrectly reported "No mode exists" for datasets with multiple modes of the same frequency (e.g., [1, 1, 2, 2]).

#### v2.2.1 Major Updates (Bug Fix):

  - **Stability Fix (Function 31)**: Fixed a crash in Matrix Operations (add, subtract, multiply) caused by a translation key error when printing results.
  - **Correctness Fix (Function 9)**: Fixed a bug in Statistics where the median would not print or save correctly for odd-numbered datasets.

#### v2.2.0 Major Updates:

  - **New Numerical Derivative Calculation**: Added function 34 for computing numerical derivatives of arbitrary functions using central difference method.
  - **Calculus Toolkit Enhancement**: Forms a complete calculus toolkit together with numerical integration function.

#### v2.1.1 Major Updates:

  - **Cross-platform Timer**: Replaced `keyboard` with `curses` and `msvcrt` modules, supporting Linux, macOS and Windows.
  - **Language Switching Optimization**: Language changes take effect immediately without program restart.
  - **Translation Improvements**: Fixed translation key formatting issues, enhanced multilingual experience.

#### v2.1.0 Major Updates:

  - **Matrix Transposition**: Added matrix transposition operation in function 31.
  - **Language Switching Optimization**: Automatic restart prompt after language change.
  - **Translation Updates**: Synchronized Chinese and English translation files.

#### v2.0.0 Major Updates:

  - **Multilingual Support**: Added complete English translation system.
  - **Language Switching**: Real-time language switching without restarting the program.
