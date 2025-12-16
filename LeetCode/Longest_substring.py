#This code is to find the longest substring count like "abcabcacb" => "abc"=3 ,"bbbb" => "b"=1
class long_substring:
    def count_long_substring(self,string_org):
        count_all=0
        for i in range(len(string_org)):
            count=0
            for j in range(i+1,len(string_org)):
                if string_org[j] in string_org[i:j]:
                    count=len(string_org[i:j])
                    break
            else:
                count=len(string_org[i:len(string_org)])
            if count_all<count:
                count_all=count
        return count_all

l1=long_substring()
ans=l1.count_long_substring("aab")
print("The longest substring count is",ans)

