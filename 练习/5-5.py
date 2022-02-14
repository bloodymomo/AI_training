def moveTower(height, fromPole, withPole, toPole):
    if height >=1:
        moveTower(height -1, fromPole, toPole, withPole)#上层n-1移动到经过柱
        moveDisk(height, fromPole, toPole)#第n个disk到目的柱
        moveTower(height-1, withPole, fromPole, toPole)#上层n-1到目的柱

def moveDisk(disk, fromPole, toPole):
    print(f"Moving disk[{disk}] from {fromPole} to {toPole}")

moveTower(64, "#1","#2","#3")

