import os,shutil

def copydir(src, dst):
  h = os.getcwd()
  src = r"{}".format(src)
  if not os.path.isdir(dst):
     print("\n[!] No Such directory: ["+dst+"] !!!")
     exit(1)

  if not os.path.isdir(src):
     print("\n[!] No Such directory: ["+src+"] !!!")
     exit(1)
  if "\\" in src:
     c = "\\"
     tsrc = src.split("\\")[-1:][0]
  else:
    c = "/"
    tsrc = src.split("/")[-1:][0]

  os.chdir(dst)
  if os.path.isdir(tsrc):
    print("\n[!] The Directory Is already exists !!!")
    exit(1)
  try:
    os.mkdir(tsrc)
  except WindowsError:
    print("\n[!] Error: In[ {} ]\nPlease Check Your Dirctory Path !!!".format(src))
    exit(1)
  os.chdir(h)
  files = []
  for i in os.listdir(src):
    files.append(src+c+i)
  if len(files) > 0:
    for i in files:
        if not os.path.isdir(i):
            shutil.copy2(i, dst+c+tsrc)

  print("\n[*] Done ! :)")

copydir("D:/AI/Face/class", "D:/AI/Face/npy")

# if name=="":
#     self.warning2("Warning", "Enter the Name")
# # if birthyear=="":
# #     self.warning2("Warning", "Enter the Birth Date")
# if records=="":
#     self.warning2("Warning", "Enter the Criminal Record")
# # if gender=="":
# #     self.warning2("Warning", "Choose Gender")
# # if race=="":
# #     self.warning2("Warning", "Enter the Race")
# if self.ImageEdit.text()=="":
#     self.warning2("Warning", "Choose a profile picture")
# if self.folderEdit.text()=="":
#     self.warning2("Warning", "Select training image folder")
# else:
#     print('correct')