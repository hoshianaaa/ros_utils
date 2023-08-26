import os,sys
import subprocess

# input: string list (ex. ["aaa","bbb","ccc"])
# output: string (ex. "aaa,bbb,ccc")
def list2string(list):
  ret = ""
  for l in list:
    ret = ret + l + ","
  return ret[:-1]

# https://softhints.com/python-change-directory-parent/
def getud_name():
  return os.path.abspath(os.curdir).split("/")[-2]

def bash_cmd(cmd):
  ret = subprocess.Popen(cmd, shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
  out,err = ret.communicate()
  return out,err

# https://yumarublog.com/python/os-path1/#:~:text=%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%80%81%E3%81%BE%E3%81%9F%E3%81%AF%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E3%81%AE%E5%AD%98%E5%9C%A8,()%20%E9%96%A2%E6%95%B0%E3%82%92%E4%BD%BF%E3%81%84%E3%81%BE%E3%81%99%E3%80%82&text=path%20%E5%BC%95%E6%95%B0%E3%81%AB%E6%8C%87%E5%AE%9A%E3%81%97%E3%81%9F%E3%83%91%E3%82%B9%E3%81%AE%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%83%BB%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E3%81%8C,%E3%81%A9%E3%81%A1%E3%82%89%E3%82%82%E6%8C%87%E5%AE%9A%E5%8F%AF%E8%83%BD%E3%81%A7%E3%81%99%E3%80%82
# ~ => HOME_DIR: https://www.lifewithpython.com/2015/10/python-get-current-user-home-directory-path.html
def isfile(path):
  if path[0] == "~":
    path = os.path.expanduser('~') + path[1:]
  return os.path.isfile(path)

def isdir(path):
  return os.path.isdir(path)

'''
8 => 3
3,3,2
int(8/3) = 2
8%(2*3) = 2

def divite(index):
'''
  


if __name__ == '__main__':
  out,err = bash_cmd("ls")
  print("*** out ***")
  print(out)
  print("*** error ***")
  print(err)

  print("*** isfile ***")

  r = isfile("./python_utils.py")
  print(r)

  r = isfile("./xxx.y")
  print(r)

  print(isfile("python_utils.py"))
  path = "/home/dev/2d_vision_detector_ws/src/2d_vision_detector/ros_sampler/scripts/python_utils/"
  path2 = "~/2d_vision_detector_ws/src/2d_vision_detector/ros_sampler/scripts/python_utils/"
  f = "python_utils.py"
  print(isfile(f))
  print(isfile(path + f))
  print(isfile(path2 + f))
