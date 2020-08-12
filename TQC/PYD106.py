'''
1. 題目說明:
請開啟PYD106.py檔案，依下列題意進行作答，計算選手賽跑每小時平均速度，使輸出值符合題意要求。作答完成請另存新檔為PYA106.py再進行評分。

2. 設計說明：
假設一賽跑選手在x分y秒的時間跑完z公里，請撰寫一程式，輸入x、y、z數值，最後顯示此選手每小時的平均英哩速度（1英哩等於1.6公里）。

提示：輸出浮點數到小數點後第一位。

3. 輸入輸出：
輸入說明
x（min）、y（sec）、z（km）數值

輸出說明
速度

輸入輸出範例
範例輸入
10
25
3
範例輸出
Speed = 10.8
'''

x = eval(input())
y = eval(input())
z = eval(input())

avg_speed = (z/1.6)/(60*x+y) * 60 * 60
print("Speed = %.1f" % avg_speed)