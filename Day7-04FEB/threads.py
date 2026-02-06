#FEB 4, 2026

#with threading
import threading
import time

# def say_hello():
#     print("Hello World!\n")

# t=threading.Thread(target=say_hello)
# t.start()

# print("Main Thread")


#without threading
# import time
# def task():
#     print("Task started")
#     time.sleep(2)
#     print("Task completed")

# task()
# print("Program finished")

# def greet(name):
#     print(f"Hello,{name}")
# t=threading.Thread(target=greet, args=("Alice",))
# t.start()


# def worker(num):
#     print(f"Worker {num} is running")
#     time.sleep(1)
#     print(f"Worker {num} has finished")

# threads = []

# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()


# import time 
# import threading
# import urllib.request
# import json
# import ssl

# def download_file():
#   try:
#     print("connecting to API...")
#     time.sleep(2)
#     url='https://fakestoreapi.com/products'
#     header={
#        "user-Agent":"Mozilla/5.0"
#     }
#     res=urllib.request.Request(url,headers=header)
#     context=ssl._create_unverified_context()
#     with urllib.request.urlopen(res,context=context) as response:
#       data=response.read()
#     print("Download completed")

#     posts=json.loads(data)
#     with open("products.json","w") as f:
#         json.dump(posts,f,indent=4)
#     print("Data saved to products.json")
#   except Exception as e:
#         print("An error occurred:",e)
# t=threading.Thread(target=download_file)
# t.start()
# print("Main thread continues execution...")


