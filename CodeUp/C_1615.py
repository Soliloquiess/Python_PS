def self(start,fin):
    set_have_gen = set()

    for n in range(1,fin+1): #1부터 fin까지 (1+1 = 2)
        n_1000 = n//1000
        n = n%1000

        n_100 = n // 100
        n = n % 100

        n_10 = n // 10
        n_1 = n % 10

        generator = n_1 + n_10 + n_100 + n_1000 + n

        if(start <= generator <= fin):
            set_have_gen.add(generator)
    return set_have_gen


#값 입력
a,b = map(int, input().split())

set_total = set()
for i in range(a,b+1):
    set_total.add(i)
    # #int(generator가질 때), none type(self일 때)
    # if(type(self(i,a,b)) == int):
    #     sum_gen += self(i,a,b)

    # sum_total += i

set_self = set_total - self(a,b)
print(set_self)
print(sum(set_self))