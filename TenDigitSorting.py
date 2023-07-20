def TenDigitSorting(array):
    return sorted(array,key=lambda x :((x//10)%10,-x))
if __name__ == '__main__':
    array=list(map(int,input().split()))
    print(*TenDigitSorting(array))