for i in range(10):
    if i<0:
        print('ok')
        break
else:
    print('hello')

for i in range(10):
    if i < 5:
        print('break')
        break
else:
    print('ok')
#for 与 else 搭配时如果for语句是非正常结束的，则不执行else语句。