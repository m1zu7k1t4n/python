# coding: UTF-8
def main(){
strs = []
num = []
strs = raw_input('>>>')
strs = strs.split()
num = map(int,strs)
maxs = num[0]
for i in range(len(num)):
    if maxs < num[i]:
        maxs = num[i]
print maxs
}

if __name__ == '__main__':
    main()