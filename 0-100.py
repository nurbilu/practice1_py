'''
create array for number from 0-100 
'''
def arr_100():
    arr = []
    for i in range(101):
        if i % 2 == 0:
            arr.append(i)
    print(arr)

if __name__ == '__main__':
    arr_100()
