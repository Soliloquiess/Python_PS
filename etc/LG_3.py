# price = [13000, 88000, 10000]
# discounts = [30, 20]

price = [32000, 18000, 42500]
discounts = [50, 20, 65]

def solution(price, discounts):
  ans = []
  price.sort(reverse=True)
  discounts.sort(reverse=True)
  print(price)
  print(discounts)
  # if(len(discounts) == len(price)):
  for i in range(len(discounts)):
    a = int(price[i] * (100-discounts[i])/100);
    ans.append(a);

  if(len(price)>len(discounts)):
  # else:
    for i in range(len(price)-len(discounts)+1, len(price)):
      b= price[i];
      ans.append(b)
  print(sum(ans));
  return sum(ans);
print(solution(price, discounts))