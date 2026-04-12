# -*- coding: UTF-8 -*-
# Copyright (c) 2025 QU QI
# MIT Licensed (https://opensource.org/licenses/MIT)
import os
import json
import decimal
import math
import sys
import warnings
os.system("")#解决转义序列不生效问题（原理玄学）
Version="MHtoolX v2.4.0"
#提高整数限制
try:
    import sys
    from unicodedata import digit
    sys.set_int_max_str_digits(1000000000)
except:
    pass
#初始化函数
def init_files():
    # 初始化文件列表及默认值
    files = {                                         
        "history.json": ["prepare done"],
        "result.json": [],
        "config.json":{"No_History":"0","Save_Result":"0","Save_Picture":"0","Enable_number_saved":"0","Language":"N/A"}
    }   
    # 遍历创建文件
    for filename, default in files.items():
        if not os.path.exists(filename):
            with open(filename, "w", encoding="UTF-8") as f:
                json.dump(default, f, ensure_ascii=False)
init_files()#初始化

# 语言配置
with open("config.json", "r") as config_file:
    config_data = json.load(config_file)
    current_language = config_data.get("Language")

# 加载翻译字典
with open ("translation.json","r",encoding="utf-8") as T:
    translations = json.load(T)

def t(key, *args):
    """翻译函数"""
    if current_language in translations and key in translations[current_language]:
        return translations[current_language][key].format(*args)
    elif key in translations["zh"]:
        return translations["zh"][key].format(*args)
    else:
        return key

# 语言选择
if config_data["Language"]=="N/A":
    lang_choice = input("Select language / 选择语言 (1 for English, 2 for 中文): ")
    if lang_choice == "1":
        current_language = "en"
    else:
        current_language = "zh"
    config_data["Language"] = current_language
    with open("config.json", "w") as config_file:
        json.dump(config_data, config_file, ensure_ascii=False)

#写入版本号函数
def version(version_code):
    INPUT="history"
    b=version_code
    Unit_length=len(b)
    with open(INPUT+".json","r") as OF:
        File=json.load(OF)
        Str_File=str(File)      
    number=0
    for i in range(len(Str_File)-Unit_length+1):
        if Str_File[i:i+Unit_length]==b:
            number=number+1
    if number ==0:
        kk=[]
        with open("history.json","r") as H:
            ee=json.load(H)
            kk.append(ee)
            kk.append(Version)
        with open("history.json","w") as f:
            json.dump(kk,f)
    INPUT="result"
    b=version_code
    Unit_length=len(b)
    with open(INPUT+".json","r") as OF:
        File=json.load(OF)
        Str_File=str(File)      
    number=0
    for i in range(len(Str_File)-Unit_length+1):
        if Str_File[i:i+Unit_length]==b:
            number=number+1
    if number ==0:
        kk=[]
        with open("result.json","r") as H:
            ee=json.load(H)
            kk.append(ee)
            kk.append(Version)
        with open("result.json","w") as f:
            json.dump(kk,f)
version(Version)  

#检验是否启用操作历史保存
import json
with open("config.json","r") as NH2:
    nh4=json.load(NH2)
    if nh4["No_History"]=="0":
        Choice=input(t("0_save_history"))
        with open("config.json","w") as NH3:
            WR=NH3
            if Choice=="2":
                nh4.update({"No_History":"2"})
                json.dump(nh4,WR)
            if Choice=="1":
                nh4.update({"No_History":"1"})
                json.dump(nh4,WR)
    else:
        pass

#检验是否启用number_saved功能
with open("config.json","r") as con1:
    config=json.load(con1)
    if config["Enable_number_saved"]=="1" and not os.path.exists("number saved.json"):
        with open("number saved.json", "w", encoding="UTF-8") as f:
                json.dump("0", f, ensure_ascii=False)

#保存结果函数
with open("config.json","r") as qu:
    qi=json.load(qu)
    if qi["Save_Result"]=="0":
        box=int(input(t("0_save_result")))
        if box==1:
            with open("config.json","w") as z:
                qi.update({"Save_Result":"1"})
                json.dump(qi,z)
        if box==2:
            with open("config.json","w") as z:
                qi.update({"Save_Result":"2"})
                json.dump(qi,z)
    if qi["Save_Result"] == "1":
        def saved(quqi, p):
            c12 = str(input(t("0_confirm_save")))
            if c12 == "1":
                # 确保reply.json内容为列表
                try:
                    with open("result.json", "r") as g:
                        ee = json.load(g)
                    if not isinstance(ee, list):  # 若非列表，重置为空列表
                        ee = []
                except (json.JSONDecodeError, FileNotFoundError):
                    ee = []            
                ee.extend([quqi, p])  # 追加结果
                with open("result.json", "w") as f:
                    json.dump(ee, f, ensure_ascii=False)
                print(t("0_save_done"))
                if config["Enable_number_saved"]=="1":
                    try:
                        with open("number saved.json", "r") as count_file:
                            current_count = int(json.load(count_file))
                    except (FileNotFoundError, json.JSONDecodeError):
                        current_count = 0
                    
                    current_count += 1  # 每次保存递增1
                    with open("number saved.json", "w") as zz:
                        json.dump(str(current_count), zz)
    if qi["Save_Result"]=="2":
        def saved(quqi,p):
            pass

#文件导出函数
def export_file(filename):
    import json
    with open(filename+".json", "r") as f:
        history_data = json.load(f)
    with open(filename+".txt", "w", encoding="UTF-8") as f:
        for entry in history_data:
            f.write(str(entry) + "\n")

#历史记录函数
with open("config.json","r")as NH:
    NO=json.load(NH)
    if NO["No_History"]=="1":
        def history(quqi):
            ww=[]
            with open("history.json","r") as g:
                ee=json.load(g)
                ww.append(ee)
                ww.append(quqi)
            with open("history.json","w") as f:
                json.dump(ww,f)
    else:
        def history(oo):
            pass

#turtle资源管理函数
try:
    import turtle
    def reset_turtle():
        try:
            import turtle
            # 关闭窗口（如果存在）
            if hasattr(turtle.Screen(), "_root") and turtle.Screen()._root:
                turtle.bye()
            # 清除所有画笔和画布
            turtle.clearscreen()
            # 强制重置模块内部状态
            turtle.TurtleScreen._RUNNING = False
            turtle.Turtle._pen = None
            turtle.Turtle._screen = None
        except (ImportError, AttributeError, turtle.Terminator):
            pass
except ImportError:
    def reset_turtle():
        pass

#保存图像函数
with open("config.json","r") as pic:
    pict=json.load(pic)
    if pict["Save_Picture"] !="3":
        try:
            import turtle
        except ImportError:
            with open("config.json","w") as o:
                pict.update({"Save_Picture":"3"})
                json.dump(pict,o)
                bre=input(t("0_graphics_error") + ", " + t("0_any_key"))
                exit()
    if pict["Save_Picture"]=="0":
        Inputs=input(t("0_enable_image"))
        if Inputs=="1":
            with open("config.json","w") as o:
                    pict.update({"Save_Picture":"1"})
                    json.dump(pict,o)
        if Inputs=="2":
            with open("config.json","w") as o:
                    pict.update({"Save_Picture":"2"})
                    json.dump(pict,o)
        Bre=input(t("0_restart") + ", " + t("0_any_key"))
        sys.exit()
    if pict["Save_Picture"]=="1":
        import time
        def saved_picture():
            Choice=input(t("0_save_image"))
            if Choice=="1":
                timestamp = time.time()
                canvas = turtle.getcanvas().postscript(file="MHtool_picture"+str(int(timestamp))+".eps")
                print(t("0_image_saved", "MHtool_picture"+str(int(timestamp))+".eps"))
            else:
                pass
    if pict["Save_Picture"]=="2":
        def saved_picture():
            pass
    if pict["Save_Picture"]=="3":
        try:
            import turtle
            with open("config.json","w") as o:
                pict.update({"Save_Picture":"0"})
                json.dump(pict,o)
                Input=input(t("0_graphics_error") + ", " + t("0_any_key"))
                exit()
        except ImportError:
            def saved_picture():
                pass

#用户操作提示函数
def reminder(te):
    print(t("0_function", te))

#牛顿法求平方根函数
def sqrt_newton(x, max_iter=1000, precision=1e-10):
    guess = x / 2  # 初始猜测值
    for _ in range(max_iter):
        guess = (guess + x / guess) / 2
        if abs(guess * guess - x) < precision:
            break
    return guess

#求平方根函数（逐次逼近）
def Squareroot(number,y):
    x = number
    precision = y
    v = 1.0  # 初始猜测值
    k = 1.0  # 初始步长
    current_best = 0.0  # 记录当前最佳近似值
    u=[]
    for _ in range(precision):
        for _ in range(10):  # 每轮尝试10次调整
            b = v * v
            if b < x:
                current_best = v  # 更新为当前下界
                v += k
            if b==x:
                u.append(v)
                e = len(u)
                for q in range(e-1):
                    u.pop()
            if b>x:
                v = current_best  # 回退到前一个有效值
                k /= 10          # 缩小步长
                v += k           # 继续逼近
                break            # 跳出内层循环
    if u==[]:
        return(current_best)
    else:
        pre = u[0]
        return(pre)

#质因数分解函数
def prime_factor(on):
    a = on
    factors = []
    if a == 1:
        factors.append(1)
        return(factors)
    if a <= 0:
        return("none")
    else:
        b = 101
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        Break = 0
        while Break == 0:
            for i in range(len(primes)):
                while a % primes[i] == 0:
                    factors.append(primes[i])
                    a = a // primes[i]  
                    if a == 1:
                        Break = 1
                        break
                if Break == 1:
                    break
            if Break == 1:
                break
            if a > 1:
                print(t("17_expanding"))
                b = b * 2
                primes = []
                for num in range(2, b):
                    is_prime = True
                    for p in primes:
                        if p * p > num:
                            break
                        if num % p == 0:
                            is_prime = False
                            break
                    if is_prime:
                        primes.append(num)
        return(factors)

#阶乘函数
def factorial(n):
    if n == 0:
        return 1
    else:
        answer=1
        for index in range(n):
            kook=index+1
            answer=answer*kook
        return answer

#三角函数计算函数
def tri_function(IN,IN2,MODE,Precision):
    k=decimal.Decimal(IN/IN2*3.1415926535897)
    answer=0
    if MODE=="1":
        for index in range(Precision):
            I=(-1)**index
            IB=factorial(2*index+1)
            IC=decimal.Decimal(k**(2*index+1))
            term=decimal.Decimal(decimal.Decimal(I/IB)*IC)
            answer=answer+term
        return(str(answer))
    if MODE=="2":
        for index in range(Precision):
            I=(-1)**index
            IB=factorial(2*index)
            IC=decimal.Decimal(k**(2*index))
            term=(decimal.Decimal(I/IB))*IC
            answer=answer+term
        return(str(answer))
    if MODE=="3":
        Sin=0
        Cos=0
        if 2*IN%IN2==0 and (2*IN//IN2)%2 !=0:
            return("DNE")
        else:
            for index in range(Precision):
                I=(-1)**index
                IB=factorial(2*index+1)
                IC=decimal.Decimal(k**(2*index+1))
                term=decimal.Decimal(decimal.Decimal(I/IB)*IC)
                answer=answer+term
            Sin=decimal.Decimal(answer)
            answer=0
            for index in range(Precision):
                I=(-1)**index
                IB=factorial(2*index)
                IC=decimal.Decimal(k**(2*index))
                term=decimal.Decimal(decimal.Decimal(I/IB)*IC)
                answer=answer+term
            Cos=decimal.Decimal(answer)
            answer=Sin/Cos
            return(str(answer))

#自然对数计算函数
def ln(argument,acc):
    result=0
    pre_result=0
    a_term=(argument-1)/(argument+1)
    for i in range(acc):
        pre_result+=(1/(1+2*i))*(a_term**(1+2*i))
    result=2*pre_result
    return result
#函数表达式安全解析函数
def function_calculation(expression,x):
    safe_symbol_dict={'math': math, 'sin': math.sin, 'cos': math.cos, 
                'tan': math.tan, 'exp': math.exp, 'log': math.log,
                'sqrt': math.sqrt, 'pi': math.pi, 'e': math.e}
    safe_symbol_dict["x"]=x
    try:
        return eval(expression,None,safe_symbol_dict)
    except ValueError:
        return float("nan")
    
#matplotlib函数绘制引擎函数
def plt_func_graph_drawing_engine(expression=str,x_min=None,x_max=None,y_max=None,y_min=None,step=None,axes_type=str,auto_scale=bool,grid=bool):
    warnings.simplefilter("ignore", category="ComplexWarning")
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print(t("0_matplotlib_not_installed"))
        return
    x_min = float(x_min)
    x_max = float(x_max)
    step = float(step)
    x_values=[]
    y_values=[]
    if auto_scale:
        plt.autoscale(axis="both")
    if grid:
        plt.grid()
    plt.xlabel("x",loc="right")
    plt.ylabel("y",rotation=0,loc="top")
    if axes_type=="1":
        ax = plt.gca() 
        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['left'].set_position(('data', 0))
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color("none")

    iterations = int((x_max-x_min)/step)+1
    for i in range(iterations):
        x_min+=step
        x_values.append(x_min)
    for x in x_values:
        y=function_calculation(expression,x)
        if not (math.isinf(y) or math.isnan(y)):
            y_values.append(y)
        else:
            y_values.append(float("nan")) 
    plt.ylim(y_min,y_max)
    plt.plot(x_values,y_values)
    plt.title("y = "+expression)
    plt.show()
#绘制坐标系函数
def draw_coordinate_system(max_x,max_y):
    myPen=turtle.Turtle()
    myPen.penup()
    myPen.goto(0,0)
    myPen.pendown()
    myPen.write("0")
    if abs(max_x)>=abs(max_y):
        myPen.goto(abs(max_x),0)
        myPen.write("x")
        myPen.goto(-abs(max_x),0)
        myPen.penup()
        myPen.goto(0,0)
        myPen.pendown()
        myPen.goto(0,abs(max_x))
        myPen.write("y")
        myPen.goto(0,-abs(max_x))
    else:
        myPen.goto(abs(max_y),0)
        myPen.write("x")
        myPen.goto(-abs(max_y),0)
        myPen.penup()
        myPen.goto(0,0)
        myPen.pendown()
        myPen.goto(0,abs(max_y))
        myPen.write("y")
        myPen.goto(0,-abs(max_y))

#用户交互
history("turn on*")
print(t("0_welcome"))
page="1"
menu=""
#注意：修改本菜单时要同步修改在language命令代码块里的菜单！
menu1="1:" + t("1_title") + ", 2:" + t("2_title") + ", 3:" + t("3_title") + "\n4:" + t("4_title") + ", 5:" + t("5_title") + ", 6:" + t("6_title") + "\n7:" + t("7_title") + ", 8:" + t("8_title") + ", 9:" + t("9_title") + "\n"
menu2="10:" + t("10_title") + ", 11:" + t("11_title") + ", 12:" + t("12_title") + "\n13:" + t("13_title") + ", 14:" + t("14_title") + ", 15:" + t("15_title") + "\n16:" + t("16_title") + ", 17:" + t("17_title") + ", 18:" + t("18_title") + "\n"
menu3="19:" + t("19_title") + ", 20:" + t("20_title") + ", 21:" + t("21_title") + "\n22:" + t("22_title") + ", 23:" + t("23_title") + ", 24:" + t("24_title") + "\n25:" + t("25_title") + ", 26:" + t("26_title") + ", 27:" + t("27_title") + "\n"
menu4="28:" + t("28_title") + ", 29:" + t("29_title") + ", 30:" + t("30_title") + "\n31:" + t("31_title") + ", 32:" + t("32_title") + ", 33:" + t("33_title") + "\n34:"+t("34_title")+", 35:"+t("35_title")+"\n"
menuf="timer:" + ("Start timer" if current_language == "en" else "启动计时器") + ", rr:" + ("View calculation history" if current_language == "en" else "查看历史计算结果") + ", er:" + ("Export calculation history" if current_language == "en" else "导出历史计算结果") + "\ncr:" + ("Clear calculation history" if current_language == "en" else "清空历史计算结果") + ", rh:" + ("View operation history" if current_language == "en" else "查看操作历史") + ", eh:" + ("Export operation history" if current_language == "en" else "导出操作历史") + "\nch:" + ("Clear operation history" if current_language == "en" else "清空操作历史") + ", cs:" + ("Clear screen" if current_language == "en" else "清空屏幕") + ", version:" + ("View version" if current_language == "en" else "查看版本") + ", language:"+("change language" if current_language == "en" else "修改语言")+"\n"

menu=menu1
page="1"
while True:
    a = input(t("0_exit"))
    #菜单
    if a=="amenu":
        print(menu1+menu2+menu3+menu4+menuf)
    if a=="menu":
        while True:
            if page=="1":
                print(t("0_menu_title")+"\n"+t("0_menu_page", page, "5")+"\n"+menu+"\n"+t("0_menu_next"))
            elif page=="f":
                print(t("0_menu_title")+"\n"+t("0_menu_page", page, "5")+"\n"+menu+"\n"+t("0_menu_prev"))
            else:
                print(t("0_menu_title")+"\n"+t("0_menu_page", page, "5")+"\n"+menu+"\n"+t("0_menu_prev")+","+t("0_menu_next"))
            E=input(t("0_menu_quit"))
            if E=="pp":
                if page=="1":
                    print(t("0_menu_first"))
                    continue
                if page=="2":
                    menu=menu1
                    page="1"
                    continue
                if page=="3":
                    menu=menu2
                    page="2"
                    continue
                if page=="4":
                    menu=menu3
                    page="3"
                if page=="f":
                    menu=menu4
                    page="4"
                    continue
            if E=="np":
                if page=="1":
                    menu=menu2
                    page="2"
                    continue
                if page=="2":
                    menu=menu3
                    page="3"
                    continue
                if page=="3":
                    menu=menu4
                    page="4"
                    continue
                if page=="4":
                    menu=menuf
                    page="f"
                    continue
                if page=="f":
                    print(t("0_menu_last"))
                    continue
            if E=="quit":
                break

    #生成质数表
    if a=="1":
        reminder(t("1_title"))
        mode=input(t("0_method", t("1_method")))
        if mode=="1":
            b = int(input(t("0_range") + t("1_range_note") + ":"))
            def prime(b):
                number = (b)
                if number == 1:
                    print(number, t("23_neither" if number == 1 else ""))
                    return False
                for c in range(2, int(math.sqrt(number))+1):
                    if number % c == 0:
                        return False
                return True

            d = []
            for e in range(2, b):
                if prime(e):
                    d.append(e)
            print(t("1_found", len(d)))
            print(d)
            saved("the reply from function 1[1]",str(len(d))+" "+"prime numbers:"+str(d))
            history("1[1]*")
        if mode=="2":
            b = int(input(t("0_range") + t("1_range_note") + ":"))   
            primes = []
            for num in range(2, b): 
                is_prime = True
                for p in primes:
                    if p*p > num:   
                        break
                    if num % p == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)   
            print(t("1_found", len(primes)))
            print(primes)
            saved("the reply from function 1[2]",str(len(primes))+" "+"prime numbers:"+str(primes))
            history("1[2]*")

    #计算算术平方根
    if a == "2":
        reminder(t("2_title"))
        INPUT=input(t("0_method", t("2_method")))
        if INPUT=="1":
            x = float(input(t("0_number") + "："))
            precision = int(input(t("0_iterations") + "（值越大越精确，推荐10000）："))
            v = 1.0  # 初始猜测值
            k = 1.0  # 初始步长
            current_best = 0.0  # 记录当前最佳近似值
            u=[]
            for _ in range(precision):
                for _ in range(10):  # 每轮尝试10次调整
                    b = v * v
                    if b < x:
                        current_best = v  # 更新为当前下界
                        v += k
                    if b==x:
                        u.append(v)
                        e = len(u)
                        for q in range(e-1):
                            u.pop()
                    if b>x:
                        v = current_best  # 回退到前一个有效值
                        k /= 10          # 缩小步长
                        v += k           # 继续逼近
                        break            # 跳出内层循环
            if u==[]:
                print(t("2_approx", current_best))
                saved("the reply from function 2[1]", str(current_best)+", ,"+"the square root of"+str(x))
            else:
                pre = u[0]
                print(t("2_exact", pre))
                saved("the reply from function 2[1]",str(pre)+", ,"+"the square root of"+str(x))
            history("2[1]*")
        if INPUT=="2":
            x = float(input(t("0_number") + "："))
            precision = int(input(t("0_iterations") + "（值越大越精确，推荐10）："))
            result = sqrt_newton(x, max_iter=precision)
            print(t("2_approx", result))
            saved("the reply from function 2[2]",str(result)+", ,"+"the square root of"+str(x))
            history("2[2]*")

    #计算圆周率
    if a =="3":
        reminder(t("3_title"))
        c=int(input(t("0_method", t("3_method"))))
        if c==1:#莱布尼茨级数法
            a=0
            b=1
            d=0
            last_p = -1
            e=int(input(t("0_accuracy") + t("3_accuracy_note")))
            show_progress = input(t("0_progress")) == "1"
            for c in range(1,e):
                d=2*c-1
                if b==1:
                    a+=1/d
                else:
                    a-=1/d
                if show_progress:
                    current_p = int((c/(e-1)*100))  # 当前百分比
                    if current_p != last_p:        # 仅当百分比变化时打印
                        print(f"{t('0_calculating')} {current_p}%")
                        last_p = current_p
                b=b*-1
                d=4*a
            print(t("3_pi_approx", d))
            saved("the reply from function 3",d)
            history("3(1)*")
        if c==2:#几何法
            reset_turtle()
            try:
                import turtle
            except ImportError:
                print(t("turtle_not_available"))
                continue
            myPen = turtle.Turtle()
            Pos =0
            o = 0
            k = 0
            c = 0
            j = int(input(t("0_accuracy") + t("3_accuracy_note")))
            r = 360*j
            py = r/2
            show_progress = input(t("0_progress")) == "1"
            myPen.speed(0)
            for i in range(int(py)):
                if show_progress:
                    print(f"{t('0_calculating')}:{str(i+1)}/{str(py)}")
                myPen.forward(0.0001)
                myPen.left(1/j)
                o = o+1
                if o == r/2:
                    Pos=(myPen.pos())
            Pos1=str(Pos)
            Pos2=Pos1.split("(")
            Pos3=Pos2[1].split(")")
            Pos4=Pos3[0].split(",")
            Pos5=Pos4[1]
            m = float(Pos5)
            q1=r/10000
            t_val = q1/m
            turtle.bye()
            print(t("3_pi_approx", t_val))
            saved("the reply from function 3",t_val)
            history("3(2)*")
        if c==3:#蒙特卡洛法
            import random
            import math
            d=0
            e=int(input(t("3_points")))
            show_progress = input(t("0_progress")) == "1"
            last_p=-1
            for i in range(e):
                a=random.uniform(0,1)
                b=random.uniform(0,1)
                c_val=math.sqrt(a*a+b*b)
                if c_val<1:
                    d=d+1
                if show_progress:
                    current_p = int((i+1)/e*100)
                    if current_p != last_p:
                        print(f"{t('0_calculating')}: {current_p}%")
                        last_p = current_p
            print(t("3_pi_approx", d/e*4))
            qu=d/e*4
            saved("the reply from function 3",qu)
            history("3(3)*")
        if c==4:#拉马努金公式法
            acc=int(input(t("0_accuracy")))
            show_progress = input(t("0_progress")) == "1"
            root2=Squareroot(2,acc)
            coe=root2*2/9801
            latter=0
            last_percent = -1
            for index in range(acc):
                v1=4*index
                v2=factorial(v1)*(1103+26390*index)
                v3=factorial(index)**4
                v4=396**(4*index)
                v5=v3*v4
                v6=v2/v5
                latter=latter+v6
                if show_progress:
                    current_percent = int((index + 1) / acc * 100)  # 计算当前百分比
                    if current_percent != last_percent:  # 仅当百分比变化时打印
                        print(f"{t('0_calculating')}: {current_percent}%")
                        last_percent = current_percent
            r=coe*latter
            answer=r**(-1)
            print(t("3_pi_approx", answer))
            saved("the reply from function 3",answer)
            history("3(4)*")
 
    #求n次幂
    if a=="4":
        reminder(t("4_title"))
        s = int(input(t("4_base")))
        h = int(input(t("4_exponent")))
        u=s
        o=0
        w=s
        l=h-1
        ll=0
        for i in range(l):
            u=u*w   
        print(t("4_result", u))
        saved("the reply from function 4",str(s)+"^"+str(h)+"="+str(u))
        ll=ll+1
        history("4*")

    #四则运算
    if a=="5":
        reminder(t("5_title"))
        s = int(input(t("0_method", t("5_mode"))))
        if s == 1:
            b = int(input(t("5_addend1")))
            c = int(input(t("5_addend2")))
            d = c+b
            print(t("4_result", d))
            ee=0
            saved("the reply from function 5[1]",str(b)+"+"+str(c)+"="+str(d))
            ee=ee+1
            ee=0
            history("5(1)*")
        if s == 2:
            e = int(input(t("5_minuend")))
            f = int(input(t("5_subtrahend")))
            g = e-f
            print(t("4_result", g))
            ff=0
            saved("the reply from function 5[2]",str(e)+"-"+str(f)+"="+str(g))
            ff=ff+1
            ff=0
            history("5(2)*")
        if s == 3:
            h = int(input(t("5_dividend")))
            j = int(input(t("5_divisor")))
            if j == 0:
                print(t("5_divide_zero"))
                saved("the reply from function 5[3]","error")
                history("5(3)(error)")
                continue
            else:
                k = h/j
                print(t("4_result", k))
            jj=0
            saved("the reply from function 5[3]",str(h)+"/"+str(j)+"="+str(k))
            jj=jj+1
            jj=0
            history("5(3)*")
        if s == 4:
            l = int(input(t("5_multiplier1")))
            m = int(input(t("5_multiplier2")))
            n = l*m
            print(t("4_result", n))
            gg=0
            saved("the reply from function 5[4]",str(l)+"*"+str(m)+"="+str(n))
            gg=gg+1
            history("5(4)*")

    #生成斐波那契数列
    if a =="6":
        reminder(t("6_title"))
        a_val = (int(input(t("0_range"))))
        show_progress = input(t("0_progress")) == "1"
        last_p = -1
        b = 1
        c = 0
        d = []
        for i in range(2):
            d.append(b)
        for e in range(a_val):
            f = d[e]+d[e+1]
            d.append(f)
            if show_progress:
                current_p = int((e+1)/a_val*100)
                if current_p != last_p:
                    print(f"{t('0_calculating')} {current_p}%")
                    last_p = current_p
        print(t("6_sequence", d))
        saved("the reply from function 6",d)
        history("6*")

    #计算黄金分割率
    if a =="7":
        reminder(t("7_title"))
        a_val = (int(input(t("0_range"))))
        show_progress = input(t("0_progress")) == "1"
        last_p = -1
        b = 1
        c = 0
        d = []
        for i in range(2):
            d.append(b)
        for e in range(a_val):
            f = d[e]+d[e+1]
            d.append(f)
            if show_progress:
                current_p = int((e+1)/a_val*100)
                if current_p != last_p:
                    print(f"{t('0_calculating')} {current_p}%")
                    last_p = current_p
        s=len(d)
        v=d[s-2]/d[s-1]
        print(t("7_ratio", v))
        saved("the reply from function 7",v)
        history("7*")

    #贪心算法
    if a=="8":
        reminder(t("8_title"))
        target= Input=float(input(t("8_money")))
        money=[100,50,20,10,5,1,0.5,0.1]
        number=[0,0,0,0,0,0,0,0,0]
        saved1=[]

        for i in range(8):
            number[i]=target//money[i]
            target=target%money[i]
        for i in range(8):
            print(t("8_denomination", money[i], number[i]))
            saved1.append(money[i])
            saved1.append(number[i])
        saved("the reply from function 8",saved1)
        history("8*")

    #统计
    if a=="9":
        reminder(t("9_title"))
        b=int(input(t("9_options")))
        if b==1:
            c=[]
            d=[]
            f=2
            while f>0:
                e=input(t("9_data"))
                if e=="f":
                    f=0
                    if len(c)==0:
                        print(t("9_no_data"))
                        break
                else:
                    try:
                        c.append(float(e))
                    except:
                        print(t("0_invalid"))
            if len(c)>0:
                w2=0.0
                for w3 in range(len(c)):
                    w2 += c[w3]
                w4=w2/len(c)
                print(t("9_average", w4))
                saved("the reply from function9(1)",w4)
                history("9(1)*")
        if b==2:
            c=[]
            w1=[]
            f=2
            while f>0:
                e=input(t("9_data"))
                if e=="f":
                    f=0
                    if len(c)==0:
                        print(t("9_no_data"))
                        break
                else:
                    try:
                        c.append(float(e))
                    except:
                        print(t("0_invalid"))
            f=2
            while f>0:
                e=input(t("9_weights"))
                if e=="f":
                    f=0
                    if len(w1)==0:
                        print(t("9_no_weights"))
                        break
                else:
                    try:
                        w1.append(float(e))
                    except:
                        print(t("0_invalid"))
            # 校验数量
            if len(c)!=len(w1):
                print(t("9_count_mismatch"))
            else:
                w11=0.0
                w12=0.0
                for w7 in range(len(c)):
                    w8=c[w7]
                    w9=w1[w7] 
                    w11 += w8*w9
                    w12 += w9
                if w12==0:
                    print(t("9_zero_weights"))
                else:
                    w14=w11/w12
                    print(t("9_weighted_avg", w14))
                    saved("the reply from function9(2)",w14)
                    history("9(2)*")
        if b==3:
            c=[]
            f=2
            while f>0:
                e=input(t("9_data"))
                if e=="f":
                    f=0
                    if len(c)==0:
                        print(t("9_no_data"))
                        break
                else:
                    try:
                        c.append(float(e))
                    except:
                        print(t("0_invalid"))
            if len(c)>0:
                w2=0.0
                for w3 in range(len(c)):  
                    w2 += c[w3]
                w4=w2/len(c)
                w6=0.0
                for w7 in range(len(c)): 
                    w8=c[w7]-w4
                    w6 += w8*w8
                w9=w6/len(c)
                print(t("9_variance", w9))
                saved("the reply from function9(3)",w9)
                history("9(3)*")
        if b==4:
            c=[]
            f=2
            while f>0:
                e=input(t("9_data"))
                if e=="f":
                    f=0
                    if len(c)==0:
                        print(t("9_no_data"))
                        break
                else:
                    try:
                        c.append(float(e))
                    except:
                        print(t("0_invalid"))
            if len(c)>0:
                w2=0.0
                for w3 in range(len(c)):
                    w2 += c[w3]
                w4=w2/len(c)
                w6=0.0
                for w7 in range(len(c)):
                    w8=c[w7]-w4
                    w6 += w8*w8
                w9=w6/len(c)
                x = w9
                d_val = int(input(t("0_accuracy") + "（输入整数）:"))
                current = sqrt_newton(x,d_val)
                print(t("9_std_dev", round(current, 5)))  # 限制小数位数
                saved("the reply from function9(4)",current)
                history("9(4)*")
        if b==5:
            DATA=[]
            Answer=0
            M1=0
            M2=0
            Break=0
            while True:
                data=input(t("9_enter_data"))
                if data=="f":
                    break
                else:
                    try:
                        float(data)
                    except:
                        print(t("9_illegal_param"))
                        Break=1
                        break
                    DATA.append(float(data))
            if Break==1:
                continue
            List=DATA
            def selection_sort(List):
                for i in range(len(List)):
                    index=i
                    for x in range(i+1,len(List)):
                        if List[x]<List[i]:
                            index=x
                    List[i],List[index]=List[index],List[i]
            selection_sort(List)
            if ((len(DATA)+1)/2)%1==0:
                Answer=DATA[int((len(DATA)+1)/2-1)]
            else:
                M1=DATA[int((len(DATA)+1)/2-1.5)]
                M2=DATA[int((len(DATA)+1)/2-0.5)]
                Answer=(M1+M2)/2
            print(t("9_median", Answer))
            saved("the reply from function9(5)",Answer)
            history("9(5)*")
        if b==6:
            DATA=[]
            Frequency={}
            Answer=0
            M1=0
            M2=0
            Break=0
            MAX=0
            MAX2=[]
            nMAX=0
            OL=0
            Answer=""
            while True:
                data=input(t("9_enter_data"))
                if data=="f":
                    break
                else:
                    try:
                        float(data)
                    except:
                        print(t("9_illegal_param"))
                        Break=1
                        break
                    DATA.append(float(data))
            if Break==1:
                history("9(6)[error]")
                continue
            
            # 完整统计所有数据的频率
            for data_point in DATA: 
                if data_point in Frequency:
                    Frequency[data_point] += 1
                else:
                    Frequency[data_point] = 1
            
            # 保存原始数据长度
            OL = len(DATA)
            
            # 获取唯一值用于后续处理
            unique_data = list(set(DATA))
            AL = len(unique_data)
            
            # 计算重复元素数量
            DI = OL - AL
            
            # 查找最大频率值
            for data_point in unique_data:
                if Frequency[data_point] > MAX:
                    MAX = Frequency[data_point]
                    MAX2.clear()
                    MAX2.append(data_point)
                elif Frequency[data_point] == MAX:  
                    MAX2.append(data_point)
            
            # 判断是否有众数
            if len(MAX2) == OL:  # 所有元素出现频率相同
                print(t("9_no_mode"))
                saved("the reply from function9(6)","none")
            else:
                if len(MAX2) != 1:
                    print(t("9_multi_mode", MAX2))
                    saved("the reply from function9(6)",MAX2)
                else:
                    print(t("9_mode", MAX2[0]))
                    saved("the reply from function9(6)",MAX2[0])
            history("9[6]")

    #绘制函数图像
    if a=="10":
        reminder(t("10_title"))
        reset_turtle()
        try:
            import turtle
        except ImportError:
            print(t("turtle_not_available"))
            continue
        x=int(input(t("0_method", t("10_mode"))))
        if x==1:
            myPen=turtle.Turtle()
            b=float(input(t("10_linear_coef")))
            c=float(input(t("10_constant")))
            e=0
            f=int(input(t("10_points_count")))
            j=float(input(t("10_spacing")))
            d=-f/2*j
            for i in range(f):
                e=d*b+c
                if i==0:
                    myPen.penup()
                    myPen.goto(d,e)
                    myPen.pendown()
                else:
                    myPen.goto(d,e)
                    d=d+j
            draw_coordinate_system(d,e)
            print(t("0_drawing"))
            saved_picture()
            turtle.done()
            history("10(1)")
        if x==2:
            myPen=turtle.Turtle()
            a_val=float(input(t("10_quad_coef")))
            b=float(input(t("10_linear_coef")))
            c=float(input(t("10_constant")))
            e=0
            f=int(input(t("10_points_count")))
            j=float(input(t("10_spacing")))
            d=-f/2*j
            for i in range(f):
                e=d**2*a_val+d*b+c
                if i==0:
                    myPen.penup()
                    myPen.goto(d,e)
                    myPen.pendown()
                else:
                    myPen.goto(d,e)
                    d=d+j
            draw_coordinate_system(d,e)
            print(t("0_drawing"))
            saved_picture()
            turtle.done()
            history("10(2)")

#计时器
    if a=="timer":
        import time
        import math
        no_curses=False
        no_msvcrt=False
        try:
            #初始化curses模块
            import curses
            timerscr=curses.initscr()
            curses.cbreak()
            timerscr.keypad(True)
            timerscr.nodelay(1)
            def curses_detect_key():
                key = timerscr.getch()
                if key==ord("a"):
                    return "a"
        except ImportError:
            no_curses=True

        try:
            import msvcrt
            def msvcrt_detect_key():
                if msvcrt.kbhit():  # 检查是否有按键
                    key = msvcrt.getch()  # 获取按键
                    if key == b'a':  # 按a退出
                        return "a"
        except ImportError:
            no_msvcrt=True

        mine=0
        s=0
        start=time.time()
        t2=0
        t3=0
        mine=0
        s=0
        while True:
            end=time.time()
            ti=end-start
            t2=ti//1
            t3=t2//60
            if t3<1:
                if t2==1:
                    print(t("timer_seconds",str(t2)))
                if t2>1:
                    print(t("timer_seconds",str(t2)))
            if t3>1:
                mine=t3
                s=t2-60*t3
                print(t("timer_minutes", mine, s))
            if t3==1:
                mine=t3
                s=t2-60*t3
                print(t("timer_minutes", mine, s))
            try:
                if no_curses:
                    if msvcrt_detect_key()=="a":
                        break
                elif no_msvcrt:
                    if curses_detect_key()=="a":
                        break
                if no_msvcrt and no_curses:
                    print(t("timer_not_supported"))
                    history(t("timer(environment not support)"))
                    continue
            except Exception as er:
                print(er)
        history("timer")

#考试成绩数据整理
    if a=="11":
        reminder(t("11_title"))
        s=2
        Sum=0
        average=0
        Max=0
        Min=0
        Dict={}
        while s>1:
            qu=input(t("11_student"))
            if qu=="f":
                s=0
            else:
                qi=input(t("11_score"))
                Dict[qu]=float(qi)
        keys=[]
        z=[]
        x=0
        y=[]
        name=""
        Max=0
        Sum=0
        average=0
        for l in Dict:
            keys.append(l)
        for i in range(len(keys)):
            z.append(Dict[keys[i]])
            if z[i]>Max:
                Max=z[i]
                x=i
                name=keys[x]
            y.append(i)
        print(t("11_highest", name, Max))
        Min=Max
        for i in range(len(keys)):
            z.append(Dict[keys[i]])
            if z[i]<Min:
                Min=z[i]
                x=i
                name=keys[x]
        print(t("11_lowest", name, Min))
        for l in Dict:
            Sum=Sum+Dict[l]
            average=Sum/len(keys)
        print(t("11_total", Sum))
        print(t("11_class_avg", average))
        saved("the reply from function 11","max:"+str(Max)+" min:"+str(Min)+" all:"+str(Sum)+" average:"+str(average))
        history("11")

#绘制三角函数图像
    if a=="12":
        reminder(t("12_title"))
        reset_turtle()
        try:
            import turtle
        except ImportError:
            print(t("turtle_not_available"))
            continue
        print(t("12_note"))
        Method=input(t("0_method", t("12_method")))
        mode=input(t("0_method", t("12_function")))
        acc4=int(input(t("12_x_start")))
        acc5=int(input(t("12_y_start")))
        Pa=mode
        pi=3.1415926535 
        if Method=="1":#几何法
            myPen=turtle.Turtle()
            acc1=float(input(t("12_angle")))
            acc2=int(input(t("12_step")))
            acc3=int(input(t("12_scale")))
            if Pa=="3":
                print(t("12_no_geometry"))
                history("12[error]")
                turtle.bye()
                continue
            acc6=acc3/((360/acc1*acc2)/(2*pi))
            step=int(2*pi*acc2/(360/acc1))
            Y_co=[]
            myPen.speed(0)
            myPen.penup()
            myPen.goto((360/acc1*acc2)/(2*pi),0)
            myPen.pendown()
            myPen.left(90)
            for i in range(int(360/acc1)):
                myPen.forward(step)
                myPen.left(acc1)
                Pos=myPen.pos()
                Pos1=str(Pos)
                Pos2=Pos1.split("(")
                Pos3=Pos2[1].split(")")
                Pos4=Pos3[0].split(",")
                if Pa=="1":
                    Pos5=Pos4[1]
                if Pa=="2":
                    Pos5=Pos4[0]
                Y_co.append(float(Pos5))
                print(f"{t('0_sampling')}，",i+1,"/",int(360/acc1))
            turtle.clearscreen()
            print(t("12_drawing"))
            for r in range(int(360/acc1)):
                step1=r*acc6
                step2=acc6*float(Y_co[r])
                myPen.penup()
                myPen.goto(acc4+step1,acc5+step2)
                myPen.pendown()
                myPen.dot(2)
            print(t("0_drawing"))
            saved_picture()
            turtle.done()
            history("12[1]")
        if Method=="2":#代数法
            Coordinates_Y=[]
            acc6=int(input(t("0_accuracy") +t("12_recommend_accuracy") ))
            acc7=int(input(t("12_points")))
            acc8=int(input(t("12_scale_alg")))
            show_progress = input(t("0_progress")) == "1"
            last_percent = -1
            C1=2
            C2=acc7
            C3=0
            acc9=acc8*acc7/(2*pi)
            for index in range(acc7):
                try:
                    Coordinates_Y.append(float(tri_function(C3,C2,mode,acc6)))#本处的except意外捕获了原本应该出现的invalidoperation错误，但不意味着问题得到了解决
                except:
                    Coordinates_Y.append("DNE")
                if show_progress:
                    current_percent = int((index + 1) / acc7 * 100)  # 计算当前百分比
                    if current_percent != last_percent:  
                        print(f"{t('12_sampling')} {current_percent}%")
                        last_percent = current_percent
                C3=C3+C1
            turtle.clearscreen()
            print(t("12_drawing"))
            for r in range(acc7):
                step1=acc8*r
                try:
                    step2=acc9*Coordinates_Y[r]
                except:
                    continue
                turtle.speed(0)
                turtle.penup()
                turtle.goto(acc4+step1,acc5+step2)
                turtle.pendown()
                turtle.dot(2)
            print(t("0_drawing"))
            saved_picture()
            turtle.done()
            history("12[2]")

    #求解二次方程
    if a=="13":
        reminder(t("13_title"))
        answer1=0
        answer2=0
        Answer=[]
        Coefficients=[]
        Precision=int(input(t("0_accuracy") + "（数字越大越精确，推荐输入100）"))
        while True:
            Coefficient=input(t("13_coeff"))
            if Coefficient=="f":
                break
            else:
                try:
                    float(Coefficient)
                except:
                    print(t("9_illegal_param"))
                    break
                Coefficients.append(float(Coefficient))
        length=len(Coefficients)
        if length != 3:
            print(t("13_coeff_error"))
        else:
            discriminant = (Coefficients[1] ** 2) - (4 * Coefficients[0] * Coefficients[2])
            if discriminant<0:
                Answer.append("no solution")
            else:
                answer1=((-Coefficients[1])+Squareroot(discriminant,Precision))/(2*Coefficients[0])
                answer2=((-Coefficients[1])-Squareroot(discriminant,Precision))/(2*Coefficients[0])
                if answer1==answer2:
                    Answer.append(answer1)
                else:
                    Answer.append(answer1)
                    Answer.append(answer2)
            print(t("13_roots", Answer))
            saved("the reply from function 13",Answer)
            history("13")

    #计算阶乘
    if a == "14":
        reminder(t("14_title"))
        n = int(input(t("14_input")))
        result = factorial(n)
        print(t("14_result", n, result))
        saved("the reply from function 14", result)
        history("14*")

    #极坐标转换
    if a == "15":
        reminder(t("15_title"))
        import math
        mode = input(t("0_method", t("15_mode")))
        
        try:
            if mode == "1":
                x = float(input(t("15_x")))
                y = float(input(t("15_y")))
                r = math.sqrt(x**2 + y**2)
                theta = math.degrees(math.atan2(y, x))  # 角度制输出
                result = f"Polar coordinates: ({round(r, 4)}, {round(theta, 4)}°)"
                
            elif mode == "2":
                r = float(input(t("15_radius")))
                theta = math.radians(float(input(t("15_angle"))))  # 转换为弧度
                x = r * math.cos(theta)
                y = r * math.sin(theta)
                result = f"Cartesian coordinate: ({round(x, 4)}, {round(y, 4)})"
                
            else:
                print(t("0_invalid"))
                history("15*[error]")
                continue
                
            print(t("0_result",result))
            saved("the reply from function 15", result)
            history("15*")
            
        except ValueError:
            print(t("15_invalid_number"))
            history("15*[invalid_input]")

    #字符串频数统计&定位
    if a=="16":
        reminder(t("16_title"))
        INPUT=input(t("16_filename"))
        b=input(t("16_search"))
        Unit_length=len(b)
        try:
            with open(INPUT+".json","r") as OF:
                File=json.load(OF)
                Str_File=str(File)      
            number=0
            for i in range(len(Str_File)-Unit_length+1):
                if Str_File[i:i+Unit_length]==b:
                    number=number+1
                    print(t("16_found_at", INPUT, i, i+Unit_length-1))
            print(t("16_found_times", b, INPUT, number))
            saved("the reply from function 16","“"+str(b)+"”"+" "+str(number)+" "+"times"+" "+"in"+" "+"“"+str(INPUT)+".json"+"”")
            history("16")
        except:
            print(t("0_file_not_found"))
            saved("the reply from function 16","file not exist")
            history("16[error]")

    #质因数分解
    if a=="17":
        reminder(t("17_title"))
        a_val = int(input(t("0_number")))
        if a_val == 1:
            print(t("17_factors", 1))
            saved("the reply from function 17","factor"+":"+"1")
            history("17")
            continue
        if a_val <= 0:
            print(t("17_no_factors"))
            saved("the reply from function 17","factor"+":"+"none")
            history("17[none]")
            continue
        else:
            b = 101
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
            factors = []
            Break = 0
            while Break == 0:
                for i in range(len(primes)):
                    while a_val % primes[i] == 0:
                        factors.append(primes[i])
                        a_val = a_val // primes[i]  
                        if a_val == 1:
                            Break = 1
                            break
                    if Break == 1:
                        break
                if Break == 1:
                    break
                if a_val > 1:
                    print(t("17_expanding"))
                    b = b * 2
                    primes = []
                    for num in range(2, b):
                        is_prime = True
                        for p in primes:
                            if p * p > num:
                                break
                            if num % p == 0:
                                is_prime = False
                                break
                        if is_prime:
                            primes.append(num)
            print(t("17_factors", factors))
            saved("the reply from function 17","factor(s)"+":"+str(factors))
            history("17")

    #计算GCD与LCM
    if a == "18":
        reminder(t("18_title"))
        choice = input(t("0_method", t("18_mode")) + ": ")   
        UserInput = []
        print(t("18_start"))
        while True:
            Input = input(t("18_enter_number"))
            if Input.lower() == 'f':
                break
            try:
                num = int(Input)
                if num <= 0:
                    print(t("18_positive"))
                    continue
                UserInput.append(num)
            except ValueError:
                print(t("18_invalid_input"))
                continue
        if len(UserInput) < 2:
            print(t("18_min_numbers"))
            history("18*[error]")
        else:
            nums = UserInput  
        
            # 质因数分解验证
            factors_list = []
            valid = True
            for num in nums:
                factors = prime_factor(num)
                if factors == "none":
                    print(t("18_no_factor").format(num))
                    valid = False
                    break
                factors_list.append(factors)
        
            if valid:
                # 统计每个数的质因数次数
                from collections import defaultdict
                counts_list = []
                for factors in factors_list:
                    counts = defaultdict(int)
                    for p in factors:
                        counts[p] += 1
                    counts_list.append(counts)
            
                # 计算GCD或LCM
                if choice == "1":
                    # 计算GCD
                    common_primes = set(counts_list[0].keys())
                    for cnt in counts_list[1:]:
                        common_primes.intersection_update(cnt.keys())
                    gcd = 1
                    for prime in common_primes:
                        min_power = min(cnt[prime] for cnt in counts_list)
                        gcd *= prime ** min_power
                    print(t("18_gcd", gcd))
                    saved("the reply from function 18[GCD]", gcd)
                    history("18[GCD]*")
            
                elif choice == "2":
                    # 计算LCM
                    all_primes = set()
                    for cnt in counts_list:
                        all_primes.update(cnt.keys())
                    lcm = 1
                    for prime in all_primes:
                        max_power = max(cnt.get(prime, 0) for cnt in counts_list)
                        lcm *= prime ** max_power
                    print(t("18_lcm", lcm))
                    saved("the reply from function 18[LCM]", lcm)
                    history("18[LCM]*")
            
                else:
                    print(t("18_invalid_choice"))
                    history("18*[invalid]")

    #十进制转二进制
    if a=="19":
        reminder(t("19_title"))
        INPUT=input(t("19_input"))
        digits=[]
        reverse=[]
        result=""
        try:
            int(INPUT)
        except:
            print(t("19_invalid"))
            history("19([error]")
            continue
        else:
            ten=int(INPUT)
        if ten==0:
            result="0"           
        else:
            while ten>=1:
                digit=ten%2
                digits.append(int(digit))
                ten=ten//2
            reverse=list(reversed(digits))
            for index2 in range(len(reverse)):
                result=result+str(reverse[index2])
        print(t("19_result", INPUT, result))
        saved("the reply from function 19", "Decimal:"+str(INPUT)+" "+"Binary:"+str(result))
        history("19")

    # 计算排列组合
    if a == "20":
        reminder(t("20_title"))
        import math
        mode = input(t("0_method", t("20_mode")) + ": ")
        try:
            n = int(input(t("20_n")))
            r = int(input(t("20_r")))
            if n < 0 or r < 0 or r > n:
                print(t("20_invalid_range"))
                history("20*[error]")
            else:
                if mode == "1":
                    # 计算排列数 nPr = n! / (n-r)!
                    result = factorial(n) // factorial(n - r)
                    print(t("20_permutation", n, r, result))
                    saved("the reply from function 20[nPr]", str(n)+"P"+str(r)+"="+str(result))
                    history("20[nPr]*")
                elif mode == "2":
                    # 计算组合数 nCr = n! / (r!(n-r)!)
                    result = factorial(n) // (factorial(r) * factorial(n - r))
                    print(t("20_combination", n, r, result))
                    saved("the reply from function 20[nCr]",str(n)+"C"+str(r)+"="+str(result))
                    history("20[nCr]*")
                else:
                    print(t("20_invalid_mode"))
                    history("20*[invalid]")
        except ValueError:
            print(t("20_invalid_int"))
            history("20*[invalid_input]")

    #计算三角函数值
    if a=="21":
        reminder(t("21_title"))
        print(t("21_note"))
        IN=int(input(t("21_numerator")))
        IN2=int(input(t("21_denominator")))
        MODE=input(t("0_method", t("21_function")))
        Precision=int(input(t("21_terms")))
        if MODE=="1":
            if IN==0:
                answer="0"
            else:
                answer=tri_function(IN,IN2,MODE,Precision)
            print(t("21_result", "sin", IN, IN2, answer))
            saved("the reply from function 21","sin"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            history("21[1]")
        if MODE=="2":
            if IN==0:
                answer="1"
            else:
                answer=tri_function(IN,IN2,MODE,Precision)
            print(t("21_result", "cos", IN, IN2, answer))
            saved("the reply from function 21","cos"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            history("21[2]")
        if MODE=="3":
            if IN==0:
                answer="0"
            else:
                answer=answer=tri_function(IN,IN2,MODE,Precision)
            print(t("21_result", "tan", IN, IN2, answer))
            saved("the reply from function 21","tan"+str(IN)+"/"+str(IN2)+"pi"+"="+answer)
            history("21[3]")

    #弧度角度制转换
    if a=="22":
        reminder(t("22_title"))
        MODE=input(t("0_method", t("22_mode")))
        if MODE=="1":
            INPUT=input(t("22_degrees"))
            k=float(INPUT)/180
            print(t("22_to_rad", INPUT, k))
            saved("the reply from function 22",INPUT+"°"+"="+str(k)+"pi")
            history("22[1]")
        if MODE=="2":
            print(t("22_rad_note"))
            INPUT=int(input(t("21_numerator")))
            INPUT2=int(input(t("21_denominator")))
            INPUT3=INPUT/INPUT2
            k=INPUT3*180
            print(t("22_to_deg", INPUT, INPUT2, k))
            saved("the reply from function 22",str(INPUT)+"/"+str(INPUT2)+"pi"+"="+str(k)+"°")
            history("22[2]")

    #质数检测
    if a=="23":
        reminder(t("23_title"))
        num = int(input(t("23_input")))
        def prime_check(num):
            res=""
            if num == 1:
                res = "1"
            else:
                factors = prime_factor(num)
                if len(factors) == 1:
                    res = "prime number" 
                else: 
                    res = "composite number"
            return res
        resu=prime_check(num)
        if resu=="1":
            print(t("23_neither"))
            saved("the reply from function 23",str(num)+":"+"neither a prime number nor a composite number")          
        if resu=="prime number":
            print(t("23_prime", num))
            saved("the reply from function 23",str(num)+":"+"prime number")
        if resu=="composite number":
            print(t("23_composite", num))
            saved("the reply from function 23",str(num)+":"+"composite number")
        history("23")

#向量模长计算
    if a=="24":
        reminder(t("24_title"))
        inp=input(t("24_x"))
        inp2=input(t("24_y"))
        answer1=(decimal.Decimal(inp)**2)+(decimal.Decimal(inp2)**2)
        answerf=Squareroot(answer1,1000)
        print(t("24_magnitude", answerf))
        saved("the reply from function 24","("+str(inp)+","+str(inp2)+")"+"=>"+str(answerf))
        history("24")

#计算任意三角形面积
    if a=="25":
        reminder(t("25_title"))
        Mode=input(t("0_method", t("25_mode")))
        if Mode=="1":
            L1=input(t("25_side1"))
            L2=input(t("25_side2"))
            L3=input(t("25_side3"))
            ACC=input(t("0_accuracy") + t("25_acc_recommendation"))
            try:
                a_val=decimal.Decimal(L1)
                b=decimal.Decimal(L2)
                c=decimal.Decimal(L3)
            except:
                print(t("25_input_error"))
                history("25[error]")
                continue
            if a_val+b<=c or a_val+c<=b or b+c<=a_val:
                print(t("25_invalid_triangle"))
                history("25[invalid]")
                continue
            else:
                p=decimal.Decimal((a_val+b+c)/2)
                S1=p*(p-a_val)*(p-b)*(p-c)
                S=Squareroot(S1,int(ACC))
                print(t("25_area", S))
                saved("the reply from function 25[1]",str(S))
                history("25[1]")
        if Mode=="2":
            L=input(t("25_base"))
            H=input(t("25_height"))
            Answer=decimal.Decimal(L)*decimal.Decimal(H)/2
            print(t("25_area", Answer))
            saved("the reply from function 25[2]",str(Answer))
            history("25[2]")

    #向量点乘
    if a=="26":
        reminder(t("26_title"))
        Input1=input(t("26_magnitude1"))
        Input2=input(t("26_magnitude2"))
        Angle1=input(t("26_angle_num"))
        Angle2=input(t("26_angle_den"))
        Pre=input(t("0_accuracy"))
        Answer=float(Input1)*float(Input2)*float(tri_function(float(Angle1),float(Angle2),"2",int(Pre)))
        print(t("0_result", Answer))
        saved("the reply from function 26",str(Answer))
        history("26")

    #十进制转十六进制
    if a=="27":
        reminder(t("27_title"))
        INPUT=input(t("27_input"))
        def decimal_to_hex(n):
            hex_digits = "0123456789ABCDEF"
            if n == 0:
                return "0"
            hex_str = ""
            while n > 0:
                hex_str = hex_digits[n % 16] + hex_str
                n = n // 16
            return hex_str
        Answer=decimal_to_hex(int(INPUT))
        print(t("27_result", INPUT, Answer))
        saved("the reply from function 27",INPUT+" "+"=>"+" "+str(Answer))
        history("27")

    #计算整数系数多项式的有理数解
    if a=="28":
        reminder(t("28_title"))
        from fractions import Fraction
        print(t("28_note"))
        degree=int(input(t("28_degree")))
        coefficients=[]
        roots=[]
        while True:
            coefficient=input(t("28_coeff"))
            if coefficient=="f":
                break
            else:
                int_coefficient=int(coefficient)
                coefficients.append(int_coefficient)
        if len(coefficients) != degree+1:
            print(t("28_coeff_error"))
            history("28[error]")
            continue
        leading_coefficient=coefficients[0]
        constant_term=coefficients[len(coefficients)-1]
        def get_all_factors(original_number):
            """获取数字的所有因子"""
            n=original_number
            factors = []
            if n<0:
                    n=-n
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    factors.append(i)
                    if i != n // i:  # 避免重复添加平方根
                        factors.append(n // i)
            return sorted(factors)
        
        def check_solution(possible_solution):
            global degree,coefficients
            sum=0
            index=0
            for power in range(degree,-1,-1):
                result=coefficients[index]*(possible_solution**power)
                sum+=result
                index+=1
            if int(sum)==0:
                return True
            else:
                return False

        leading_coefficient_factors=get_all_factors(leading_coefficient)
        constant_term_factors=get_all_factors(constant_term)
        for lcf in leading_coefficient_factors:
            for ctf in constant_term_factors:
                possible_solution=Fraction(ctf,lcf)
                if check_solution(possible_solution):
                    roots.append(possible_solution)
                if check_solution(-possible_solution):
                    roots.append(-possible_solution)
        print(t("28_roots", roots))
        saved("the reply from function 28",f"highest_degree:{degree},coefficients{coefficients},rational_roots{roots}")
        history("28") 

    #计算数值积分
    if a=="29":
        reminder(t("29_title"))
        print(t("29_function_note"))
        print(t("29_example"))

        while True:
            func_str = input(t("29_function"))
            if func_str=="cons":
                print(t("29_cons"))
            elif func_str=="func":
                print(t("29_func"))
            else:
                break
        a_val = float(input(t("29_lower")))
        b = float(input(t("29_upper")))
        n = int(input(t("29_intervals")))
        if n <=0 or n% 1 != 0:
            print(t("29_positive_int"))
            history("29[error]")
            continue
        else:
            interval_length=b-a_val
            step=interval_length/n
            sampling_points=[]
            integral_result=0
            for index in range(n):
                sampling_points.append(function_calculation(func_str,a_val+step*index+(interval_length/(2*n))))
            for sp in sampling_points:
                cache=sp*step
                integral_result=integral_result+cache
        print(t("29_integral", a_val, b, func_str, integral_result))
        saved("the reply from function 29", f"∫[{a_val},{b}] {func_str} dx = {integral_result}")
        history("29")

    #三阶方阵行列式计算
    if a=="30":
        reminder(t("30_title"))
        # order=input("请输入方阵的阶数(必需为整数)")
        # order=int(order)
        order=3
        number_elements=int(order**2)
        matrix=[]
        extended_matrix=[]
        def print_matrix():
            global matrix,order
            for i3 in range(len(matrix)):
                print(matrix[i3], end=' ')
                # 如果到达行尾，则换行
                if (i3 + 1) % order == 0:
                    print()  # 换行
        print(t("30_setup"))
        row=0
        for index in range(order):
            row+=1
            print(t("30_row", row))
            for index2 in range(order):
                element = input(t("30_element"))
                try:
                    # 尝试转换为浮点数
                    matrix.append(float(element))
                except ValueError:
                    print(t("30_invalid_element"))
            print_matrix()


        for i in range(order):  # 对于每一行
            # 添加原矩阵的一行
            for j in range(order):
                extended_matrix.append(matrix[i * order + j])
            # 添加第一列的元素
            extended_matrix.append(matrix[i * order])
            # 添加第二列的元素
            extended_matrix.append(matrix[i * order + 1])
        
       
        sum_product=0
        for j in range(3):
            product=1
            for i in range(3):
                product=product*extended_matrix[i * (order + 2) + j + i]
            sum_product+=product
        
        sum_product2=0
        for j in range(3):
            product=1
            for i in range(3):
                product=product*extended_matrix[i * (order + 2) + (4 - j - i)]
            sum_product2+=product

        result=sum_product-sum_product2
        print(t("30_determinant", result))
        saved("the reply from function 30",f"order:3,matrix:{matrix},determinant:{result}")
        history("30")

    #矩阵运算
    if a=="31":
        reminder(t("31_title"))
        class MatrixList:
            """
            (0,0) (1,0) (2,0)
            (0,1) (1,1) (2,1)
            (0,2) (1,2) (2,2)
            """
            def __init__(self,matrix_list,Row,Column):
                self.matrix=matrix_list
                self.num_row=Row
                self.num_column=Column

            def read_element(self,x,y):
                index=y*self.num_column+x
                return self.matrix[index]
            def save_element(self,value,x,y):
                index=y*self.num_column+x
                self.matrix[index]=value
        
        def print_matrix_general(matrix,column):
            for i3 in range(len(matrix)):
                print(matrix[i3], end=' ')
                # 如果到达行尾，则换行
                if (i3 + 1) % column == 0:
                    print()  # 换行
        mode=input(t("0_method", t("31_mode")))
        if mode=="1"or mode=="2":
            matrixs=[]
            matrix_number=int(input(t("31_matrix_count")))
            matrix_row=int(input(t("31_rows")))
            matrix_column=int(input(t("31_cols")))
            matrix_index=1
            for index3 in range(matrix_number):
                print(t("31_set_matrix", matrix_index))
                row=0
                matrix=[]
                for index in range(matrix_row):
                    row+=1
                    print(t("30_row", row))
                    for index2 in range(matrix_column):
                        element = input(t("30_element"))
                        try:
                            # 尝试转换为浮点数
                            matrix.append(float(element))
                        except ValueError:
                            print(t("30_invalid_element"))
                            history("31[error]")
                    print_matrix_general(matrix,matrix_column)
                matrixs.append(matrix)
                matrix_index+=1
            
            if mode=="1":  # 加法
                # 初始化结果矩阵为第一个矩阵
                result = matrixs[0][:]  # 复制第一个矩阵
                # 依次加上后续矩阵
                for matrix_index in range(1, matrix_number):
                    for i in range(len(result)):
                        result[i] += matrixs[matrix_index][i]
                print(t("0_result","") + ":")
                print_matrix_general(result, matrix_column)
                saved("the reply from function 31[1]",f"matrix:{result},column:{matrix_column}")
                history("31[1]")

            if mode=="2":  # 减法
                # 初始化结果矩阵为第一个矩阵
                result = matrixs[0][:]  # 复制第一个矩阵
                # 依次减去后续矩阵
                for matrix_index in range(1, matrix_number):
                    for i in range(len(result)):
                        result[i] -= matrixs[matrix_index][i]
                print(t("0_result","") + ":")
                print_matrix_general(result, matrix_column)
                saved("the reply from function 31[2]",f"matrix:{result},column:{matrix_column}")
                history("31[2]")

        elif mode=="3":
            if mode =="3":
                matrixs=[]
                matrixs_sizes=[]
                result=[]
                matrix_index=1
                for index3 in range(2):#锁定只能是两个矩阵计算
                    print(t("31_set_matrix", matrix_index))
                    matrix_row=int(input(t("31_rows")))
                    matrix_column=int(input(t("31_cols")))
                    row=0
                    matrix=[]
                    for index in range(matrix_row):
                        row+=1
                        print(t("30_row", row))
                        for index2 in range(matrix_column):
                            element = input(t("30_element"))
                            try:
                                # 尝试转换为浮点数
                                matrix.append(float(element))
                            except ValueError:
                                print(t("30_invalid_element"))
                        print_matrix_general(matrix,matrix_column)
                    matrix_size=[matrix_row,matrix_column]
                    matrixs.append(matrix)
                    matrixs_sizes.append(matrix_size)
                    matrix_index+=1
                matrix_0=MatrixList(matrixs[0],matrixs_sizes[0][0],matrixs_sizes[0][1])
                matrix_1=MatrixList(matrixs[1],matrixs_sizes[1][0],matrixs_sizes[1][1])
                result_ob=MatrixList(result,matrixs_sizes[0][0],matrixs_sizes[1][1])
                if matrixs_sizes[0][1] !=matrixs_sizes[1][0]:
                    print(t("31_cannot_multiply"))
                    history("31[error]")
                    continue
                else:
                    # 初始化结果矩阵，大小为第一个矩阵的行数 × 第二个矩阵的列数
                    result_size = matrixs_sizes[0][0] * matrixs_sizes[1][1]
                    result = [0] * result_size
                    result_ob=MatrixList(result,matrixs_sizes[0][0],matrixs_sizes[1][1])
                    
                    # 矩阵乘法计算
                    for i in range(matrixs_sizes[0][0]):  # 遍历第一个矩阵的行
                        for j in range(matrixs_sizes[1][1]):  # 遍历第二个矩阵的列
                            sum_val = 0
                            for k in range(matrixs_sizes[0][1]):  # 遍历第一个矩阵的列/第二个矩阵的行
                                # 第一个矩阵的(i,k)元素 × 第二个矩阵的(k,j)元素
                                a_val = matrix_0.read_element(k, i)  # 注意：x是列索引，y是行索引
                                b_val = matrix_1.read_element(j, k)
                                sum_val += a_val * b_val
                            # 将结果保存到结果矩阵的(i,j)位置
                            result_ob.save_element(sum_val, j, i)
                    
                    print(t("0_result","") + ":")
                    print_matrix_general(result_ob.matrix, matrixs_sizes[1][1])
                    saved("the reply from function 31[3]",f"matrix:{result_ob.matrix},column:{matrixs_sizes[1][1]}")
                    history("31[3]")
        else:
            if mode=="4":
                #输入矩阵（1个）
                result=[]
                matrix_row=int(input(t("31_rows")))
                matrix_column=int(input(t("31_cols")))
                row=0
                matrix=[]
                for index in range(matrix_row):
                    row+=1
                    print(t("30_row", row))
                    for index2 in range(matrix_column):
                        element = input(t("30_element"))
                        try:
                            # 尝试转换为浮点数
                            matrix.append(float(element))
                        except ValueError:
                            print(t("30_invalid_element"))
                    print_matrix_general(matrix,matrix_column)

                #转置运算
                matrix_ob=MatrixList(matrix,matrix_row,matrix_column)
                result_ob=MatrixList(result,matrix_column,matrix_row)
                for i in range(int(matrix_row*matrix_column)):
                    result.append(0)
                for r in range (matrix_row):
                    for c in range(matrix_column):
                        result_ob.save_element(matrix_ob.read_element(c,r),r,c)
                print(t("0_result","")+":")
                print_matrix_general(result_ob.matrix,matrix_row)
                saved("the reply from function 31[4]",f"matrix:{result_ob.matrix},column:{matrix_row}")
                history("31[4]")

    #常见数学模型计算（复利，半衰期，人口增长）
    if a=="32":
        reminder(t("32_title"))
        mode_selection=input(t("0_method", t("32_mode")))
        if mode_selection=="1":
            principal = float(input(t("32_principal")))
            rate = float(input(t("32_rate")))
            years = int(input(t("32_years")))
            compound_times = int(input(t("32_compound")))
            amount = principal * (1 + rate/compound_times) ** (compound_times * years)
            interest = amount - principal
            print(t("32_compound_result", years, amount, interest))
            saved("the reply from function 32[1]",
                  f"principal:{principal},APR:{rate},years:{years},compound times:{compound_times},amount:{amount},interest{interest}")
            history("32[1]")
        if mode_selection=="2":
            initial_amount = float(input(t("32_initial")))
            half_life = float(input(t("32_half_life")))
            time_passed = float(input(t("32_time")))
            remaining = initial_amount * (0.5) ** (time_passed / half_life)
            decayed = initial_amount - remaining
            print(t("32_half_life_result", time_passed, remaining, decayed))
            saved("the reply from function 32[2]",f"initial amount:{initial_amount},half_life:{half_life},time passed:{time_passed},remaining:{remaining}")
            history("32[2]")
        if mode_selection=="3":
            choice = input(t("32_pop_mode"))
            
            if choice == "1":
                P0 = float(input(t("32_pop_initial")))
                r = float(input(t("32_growth_rate")))
                t_val = float(input(t("32_prediction")))
                
                P_t = P0 * math.exp(r * t_val)
                print(t("32_pop_result", t_val, f"{P_t:,.0f}"))
                saved("the reply from function 32[3][1]",f"P0:{P0},r:{r},t:{t_val},P_t:{P_t}")
                history("32[3][1]")
                
            if choice == "2":
                P0 = float(input(t("32_pop_initial")))
                r = float(input(t("32_growth_rate")))
                t_val = float(input(t("32_prediction")))
                K = float(input(t("32_capacity")))
                
                exponent = (K / P0 - 1) * math.exp(-r * t_val)
                P_t = K / (1 + exponent)
                P_t=int(P_t)
                print(t("32_pop_result", t_val, P_t))
                saved("the reply from function 32[3][2]",f"P0:{P0},r:{r},t:{t_val},K:{K},P_t:{P_t}")
                history("32[3][2]")

    #对数计算
    if a=="33":
        reminder(t("33_title"))
        mode_selection=input(t("0_method", t("33_mode")))
        if mode_selection=="2":
            argument=float(input(t("33_argument")))
            base=float(input(t("33_base")))
            precision=int(input(t("33_terms")))
            result=ln(argument,precision)/ln(base,precision)
            print(t("33_log_result", base, argument, result))
            saved("the reply from function 33[2]",f"log_{base}({argument})={result}")
            history("33[2]")
        if mode_selection=="1":  
            argument=float(input(t("33_argument")))
            precision=int(input(t("33_terms")))
            result=ln(argument,precision)
            print(t("33_ln_result", argument, result))
            saved("the reply from function 33[1]",f"ln({argument})={result}")
            history("33[1]")
    #计算数值导数
    if a=="34":
        reminder(t("34_title"))
        print(t("34_function_note"))
        print(t("34_example"))

        while True:
            func_str = input(t("34_function"))
            if func_str=="cons":
                print(t("34_cons"))
            elif func_str=="func":
                print(t("34_func"))
            else:
                break
        x_value=float(input(t("34_enter_derivative_point")))
        acc=float(input(t("34_enter_accuracy")))
        step=10/acc
        lower_sample=x_value-step
        upper_sample=x_value+step
        derivative=(function_calculation(func_str,upper_sample)-function_calculation(func_str,lower_sample))/(2*step)
        print(t("34_output_derivative",x_value,derivative))
        saved("the reply from function 34", f"f(x)= {func_str},f'({x_value}) = {derivative}")
        history("34")
    #任意函数绘图
    if a == "35":
        reminder(t("35_title"))
        print(t("34_function_note"))
        print(t("34_example"))

        while True:
            func_str = input(t("34_function"))
            if func_str == "cons":
                print(t("34_cons"))
            elif func_str == "func":
                print(t("34_func"))
            else:
                break
        x_min = float(input(t("35_x_min")))
        x_max = float(input(t("35_x_max")))
        y_min= float(input(t("35_y_min")))
        y_max= float(input(t("35_y_max")))
        axes_type = input(t("35_axes_type"))
        step = float(input(t("35_step")))
        print(t("35_drawing"))
        if x_max>x_min and y_max>y_min:
            plt_func_graph_drawing_engine(func_str, x_min, x_max, y_max, y_min, step, axes_type, grid=True)
            history("35")
        else:
            print(t("35_limit_error"))
            history("35(limit error)")

#读取计算结果
    if a=="rr":
        with open("result.json","r") as gu:
            eue=json.load(gu)
            print(eue)

#清空计算结果
    if a=="cr":
        with open("result.json","w") as gu:
            eue=json.dump("*",gu)
        print(t("0_cleared"))

#终止运行
    if a =="exit":
        history("turn off")
        break

#读取操作历史
    if a=="rh":
        with open("history.json","r") as yy:
            o1=json.load(yy)
        print(o1)

#清空操作历史
    if a=="ch":
        with open("history.json","w") as yy:
            json.dump("prepare done ",yy)
        print(t("0_cleared"))

#导出操作历史
    if a=="eh":
        export_file("history")
        print(t("0_export", "操作历史", "history"))

#导出历史计算结果
    if a=="er":
        export_file("result")
        print(t("0_export", "历史计算结果", "result"))

#清屏
    if a=="cs":
        print("\033c", end="")

#查看版本
    if a=="version":
        print(t("0_version", Version))

#修改语言
    if a == "language":
        lang_choice = input("Select language / 选择语言 (1 for English, 2 for 中文): ")
        if lang_choice == "1":
            current_language = "en"
        else:
            current_language = "zh"
        config_data["Language"] = current_language
        with open("config.json", "w") as config_file:
            json.dump(config_data, config_file, ensure_ascii=False)
        print("Language changed / 语言已更改")
        #刷新菜单
        menu1="1:" + t("1_title") + ", 2:" + t("2_title") + ", 3:" + t("3_title") + "\n4:" + t("4_title") + ", 5:" + t("5_title") + ", 6:" + t("6_title") + "\n7:" + t("7_title") + ", 8:" + t("8_title") + ", 9:" + t("9_title") + "\n"
        menu2="10:" + t("10_title") + ", 11:" + t("11_title") + ", 12:" + t("12_title") + "\n13:" + t("13_title") + ", 14:" + t("14_title") + ", 15:" + t("15_title") + "\n16:" + t("16_title") + ", 17:" + t("17_title") + ", 18:" + t("18_title") + "\n"
        menu3="19:" + t("19_title") + ", 20:" + t("20_title") + ", 21:" + t("21_title") + "\n22:" + t("22_title") + ", 23:" + t("23_title") + ", 24:" + t("24_title") + "\n25:" + t("25_title") + ", 26:" + t("26_title") + ", 27:" + t("27_title") + "\n"
        menu4="28:" + t("28_title") + ", 29:" + t("29_title") + ", 30:" + t("30_title") + "\n31:" + t("31_title") + ", 32:" + t("32_title") + ", 33:" + t("33_title") + "\n34:"+t("34_title")+", 35:"+t("35_title")+"\n"
        menuf="timer:" + ("Start timer" if current_language == "en" else "启动计时器") + ", rr:" + ("View calculation history" if current_language == "en" else "查看历史计算结果") + ", er:" + ("Export calculation history" if current_language == "en" else "导出历史计算结果") + "\ncr:" + ("Clear calculation history" if current_language == "en" else "清空历史计算结果") + ", rh:" + ("View operation history" if current_language == "en" else "查看操作历史") + ", eh:" + ("Export operation history" if current_language == "en" else "导出操作历史") + "\nch:" + ("Clear operation history" if current_language == "en" else "清空操作历史") + ", cs:" + ("Clear screen" if current_language == "en" else "清空屏幕") + ", version:" + ("View version" if current_language == "en" else "查看版本") + ", language:"+("change language" if current_language == "en" else "修改语言")+"\n"
        menu=menu1
        page="1"
#翻倍计算（已隐藏）
    if a=="benchmark":   
        e = int(input(t("benchmark_input1")))
        f = int(input(t("benchmark_input2")))
        j = 0
        h = 0
        for i in range(f):
            j= e*2
            h += 1
            e = j
            print(t("benchmark_progress", j, h))
            w=j
        saved("the reply from function benchmark",w)
        history("894*")
    if a=="truth":
        print("101010")
print(t("0_goodbye"))
print(t("0_goodbye_en"))