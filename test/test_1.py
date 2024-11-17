def foo():
    for i in range(0, 10):
        cond = (i % 2 == 0)    
        print(f"i = {i}, cond = {cond}")
        if cond % 2 == 0:
            print("четное")
        else:
            print("нечетное")

if __name__ == "__main__":
    foo()