#remove duplicates
li = [4,4,5,8,4,8,8]
print(li)
ans = []
for i in li:
    if i not in ans:
        ans.append(i)
print(ans)

