rid ="980115-1234567"

def solution(rid):
  rid = list(rid)
  ans =[]
  # print(rid[7])
  if(rid[7]=='1' or rid[7]=='3'):
    sex= "M"
  if(rid[7]=='2' or rid[7]=='4'):
    sex= "F"

  if(rid[7]=='3' or rid[7]=='4'):
    ans = int(rid[0] + rid[1])
    year = 2000+ans;
    print(year)
    return year;

  if(rid[7]=='1' or rid[7]=='2'):
    a = int(rid[0] + rid[1])
    year = 1900+a;
    print(year);
    # year = str(year)
    ans.append(str(year))
    ans.append(str(sex));
    string = '/'.join(ans)
    # return ans;
    return string
print(solution(rid))