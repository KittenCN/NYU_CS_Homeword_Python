n = int(input())
int_list = [0] * n
ans = ""
for i in range(n):
    int_list[i] = int(input())
for i in range(n):
    ans += chr(int_list[i])
print(ans)