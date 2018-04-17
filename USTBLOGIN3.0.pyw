import urllib.request
import urllib.parse
from lxml import etree
import http.cookiejar
import tkinter as tk

def login(username, password):
    url = 'http://202.204.48.66/'

    # 创建一个cookie对象来保存cookie
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)  # 创建一个cookie的处理器
    opener = urllib.request.build_opener(handler)  # 构建一个handler对象,定制opener

    data = {'DDDDD': username,
            'upass': password,
            'v6ip': '2001%3A0da8%3A0208%3Ac240%3A5d90%3A03aa%3A49c7%3Ae136',
            '0MKKey': '123456789'}

    data1 = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data1)
    # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')
    req.add_header('User-Agent',
                   'Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116Safari/537.36Edge/15.15063')
    response = opener.open(req)

    html = response.read().decode('gb2312')
    # print(html)
    html = etree.HTML(html)

    test = html.xpath('//div[@class="d"]/form[@style="width:100%;"]/p/span/text()')
    '''test2 = html.xpath('//div[@class="m"]/div[@class="m_r"]/div[@class="d"]/form[@style="width:100%;"]/p/span/text()')   
    print(test2)'''
    if test == []:
        end_str = '登陆失败，请“返回”检查账户密码！'
    else:
        end_str = '登陆成功，欢迎！'
    return end_str
def keycontral(event):
    if event.keysym=='Return':
        main_login()
def keycontral2(event):
    if event.keysym == 'Return':
        win.destroy()
def main_login():
    win.withdraw()
    username = var_username.get()
    password = var_password.get()
    end_str = login(username, password)
    end_win = tk.Toplevel(win)
    end_win.geometry('350x150')
    end_win.title('登陆结果')
    end_win.focus_force()
    tk.Label(end_win, text=end_str, width=30, height=2, justify='center').place(x=70, y=30)
    if len(end_str)==8:
        OK_btn=tk.Button(end_win, text='OK(退出)', width=10, command=win.destroy)
        OK_btn.place(x=135, y=70)
        OK_btn.bind_all('<Return>', keycontral2)
    else:
        tk.Button(end_win, text='放弃登录', width=10, command=win.destroy).place(x=90, y=70)
        def re_com():
            end_win.destroy()
            win.deiconify()
        tk.Button(end_win, text='返回', width=10, command=re_com).place(x=180, y=70)

# 搭建窗口&全局变量
win = tk.Tk()
win.title('USTB校园网登陆')
win.geometry('400x300')
var_username = tk.StringVar()
var_password = tk.StringVar()
#窗体初始化

canvas = tk.Canvas(win, height=101, width=579)
#image_file = tk.PhotoImage(file='.//常用文件//校园网登陆.GIF')
image_file = tk.PhotoImage(file='.//校园网登陆.GIF')
canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

def initwin():
    # userinformation
    tk.Label(win, text='登陆账号：').place(x=80, y=110)
    tk.Label(win, text='登陆密码：').place(x=80, y=150)
    var_username.set('41521238')
    entry_username = tk.Entry(win, textvariable=var_username)
    entry_username.place(x=160, y=110)
    var_password.set('08228739')
    entry_password = tk.Entry(win, textvariable=var_password, show='*')
    entry_password.place(x=160, y=150)
    btn_login = tk.Button(win, text='登陆', width=10, command=main_login)
    btn_login.bind_all('<Return>',keycontral)
    btn_login.place(x=100, y=200)
    btn_close = tk.Button(win, text='退出', width=10, command=win.destroy)
    btn_close.place(x=200, y=200)

initwin()
win.mainloop()
