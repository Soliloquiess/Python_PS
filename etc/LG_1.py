def solve(nums):
    mp = {}
    for i in set(nums):
        x = nums.count(i)
        try:
            mp[x].append(i)
        except:
            mp[x] = [i]
    ans = []

    for i in sorted(mp, reverse=True):
      for j in sorted(mp[i]):
      # for j in sorted(mp[i], reverse=True):
      #       ans.extend([j] * i)
              ans.extend([j])
    return ans


nums = ["spy", "ray", "spy", "room", "once", "ray", "spy", "once"]
print(solve(nums))