f = open("input.txt", "r")
arr = (f.read().split("\n"))
arr = list(map(int, arr))
arr = sorted(arr)