def towers(stacks):
    def move(n, origin, dest, buffer):
        if n > 0:
            # Put everything in the buffer using dest as the buffer
            move(n - 1, origin, buffer, dest)
            # Move the last stack in the correct place
            dest.append(origin.pop())
            # Move everything from buffer to the final destination
            move(n - 1, buffer, dest, origin)

    t1 = [i for i in reversed(range(stacks))]
    t2 = []
    t3 = []
    print(t1)
    print(t2)
    print(t3)
    print("-"*10)
    move(stacks, t1,t2,t3)
    print(t1)
    print(t2)
    print(t3)

towers(10)



