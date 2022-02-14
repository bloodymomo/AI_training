# def getMaximumGenerated(n: int) -> int:
#     nums = [0]*(n+1)
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     i = 1
#     nums[0] = 0
#     nums[1] = 1

#     for i in range(1, (n//2)+1):
#         nums[2*i] = nums[i]
#         if 2*i < n:
#             nums[2*i+1] = nums[i] + nums[i+1]
#             print(nums[2*i+1])
#         i +=1
#     print(nums)
#     return max(nums)

# print(getMaximumGenerated(7))
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
# def BinaryTree(r):
#     return [r, [], []]
# def insertLeft(root,newBranch):
#     t = root.pop(1)
#     if len(t) > 1:
#         root.insert(1,[newBranch,t,[]])
#     else:
#         root.insert(1,[newBranch, [], []])
#     return root
# def insertRight(root,newBranch):
#     t = root.pop(2)
#     if len(t) > 1:
#         root.insert(2,[newBranch,[],t])
#     else:
#         root.insert(2,[newBranch, [], []])
#     return root


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)#入栈下降
    currentTree = eTree
    #print(eTree.postorder())
    count = 0
    for i in fplist:
        if i == '(':     
            count +=1   
            print(count, "step")                                 #表达式开始
            currentTree.insertLeft('')
            pStack.push(currentTree)           #入栈下降
            currentTree = currentTree.getLeftChild()#现节点到了左子节点上
            print(eTree.postorder())
            
        elif i not in ['+','-','*','/',')']: #操作数
            count +=1
            print(count, "step") 
            currentTree.setRootVal(int(i)) #
            parent = pStack.pop()                             #出栈上升
            currentTree = parent
            print(eTree.postorder())
        elif i in ['+','-','*','/']:  #操作符
            count +=1
            print(count, "step") 
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
            print(eTree.postorder())
        elif i == ')':
            count +=1
            print(count, "step") 
            currentTree = pStack.pop()   #出栈上升
            print(eTree.postorder())
        else:
            raise ValueError
    return eTree

pt = buildParseTree("( 3 + ( 4 * 5 ) )")
pt.postorder()

def printexp(tree):
    sVal = ''
    if tree:
        if tree.getRightChild() not in ['+','-','*','/'] and len(sVal) ==0: #and (sVal[-1] in ['+','-','*','/'] or sVal ==''):
            sVal = '('+ printexp(tree.getLeftChild())
        if len(sVal)>= 2:
            
            sVal =  printexp(tree.getLeftChild())
        sVal = sVal+ str(tree.getRootVal())
        if tree.getLeftChild() not in ['+','-','*','/'] and sVal[-1] not in ['+','-','*','/']:
            sVal = sVal+printexp(tree.getRightChild())
        else:
            sVal = sVal+printexp(tree.getRightChild()) + ')'
    return sVal

print(printexp(pt))