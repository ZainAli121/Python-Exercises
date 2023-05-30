import os
files= os.listdir("clusttered folder")
i=1
for file in files:
  if file.endswith(".png"):
    os.rename(f"clusttered folder/{file}", f"clusttered folder/{i}.png")
    i=i+1
    print(file)
print("Cluster Cleared!")