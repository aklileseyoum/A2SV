# Enter your code here. Read input from STDIN. Print output to STDOUT
no_shoe = int(input())
shoe_size = list(map(int, input().split(" ")))
no_customer = int(input())
money = 0
for i in range(no_customer):
    customer = list(map(int, input().split(" ")))
    if customer[0] in shoe_size:
        money += customer[1]
        shoe_size.remove(customer[0])
        
print(money)
