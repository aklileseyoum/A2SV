# Enter your code here. Read input from STDIN. Print output to STDOUT222222221
english_no = int(input())
english = set(map(int, input().split()))
french_no = int(input())
french = set(map(int, input().split()))
answer = list(english.difference(french))
print(len(answer))
