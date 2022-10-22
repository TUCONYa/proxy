import requests, os, sys, time
def run(type):
 while True:
  i = requests.get(f'https://api.proxyscrape.com/v2/?request=getproxies&protocol={type}&timeout=10000&country=all').text
  print (i)
  open('proxy_http.txt', mode='a').write(i)
  time.sleep(3)
  os.system('clear')
  for i in range(300, -1, -1):
   print (f'Vui Lòng Đợi {i} Giây Delay! ', end="\r")
   time.sleep(1)


os.system("clear")
print ("  Tool Auto Get Proxy V2 \n")
time.sleep(1)
print ("  © Bản Quyền By: Nguyễn Đăng Bá Hào  \n")
time.sleep(1)
print ("  MoMo : 0568115698  ")
time.sleep(2.5)
os.system('clear')
time.sleep(0.5)
print (' => Nhập [1]  Để Vào Tool Get Proxy sock5  ')
print (' => Nhập [2] để Vào  Tool Get Proxy sock4  ')
print (' => Nhập [3] Để Vào Tool Get Proxy HTTP  ')
choice = input(' [√]=> Nhập Lựa Chọn: ')
if choice == '1':
 run('sock5')
if choice == '2':
 run('sock4')
if choice == '3':
 run('http')