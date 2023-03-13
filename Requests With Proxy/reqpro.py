import requests, time

def main():
    f = open("http-proxy.txt", "r").read().split('\n')
    #fl = f.readlines()
    for x in f:
       p = {"http":f"http://{x}"}
       print(p)
       try:
          r = requests.get("https://shelterium.com/", proxies=p, timeout=5).status_code
       except KeyboardInterrupt:
          sys.exit()
       except:
          r = "time out"
       print(f"Proxy : {x} ==> Status : {r}")
       
if __name__== "__main__":
  main()
