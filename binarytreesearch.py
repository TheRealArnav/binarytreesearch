

class Tree():
    def __init__(self,data):
       
        self.data = data
        self.leftnode = None
        self.rightnode =None

    def insert(self,root,i):
        if root == None:
            return Tree(i)
        if root.data > i:
            root.leftnode = self.insert(root.leftnode, i)
        if root.data < i:
            root.rightnode = self.insert(root.rightnode, i)
        return root
    
    def InOrderTraversal(self,root):
        if root.leftnode != None:
            self.InOrderTraversal(root.leftnode)
        print(root.data)
        if root.rightnode != None:
            self.InOrderTraversal(root.leftnode)

    def PreOrderTraversal(self,root):
        print(root.data)
        if root.leftnode != None:
            self.PreOrderTraversal(root.leftnode)
        if root.rightnode != None:
            self.PreOrderTraversal(root.rightnode)

    def PostOrderTraversal(self,root):
        if root.leftnode != None:
            self.PostOrderTraversal(root.leftnode)
        if root.rightnode != None:
            self.PostOrderTraversal(root.rightnode)
        print(root.data)



tree = Tree(0)
root = None

root = tree.insert(root,30)
tree.insert(root,15)
tree.insert(root,32)
tree.insert(root,29)
tree.insert(root,70)
tree.insert(root,31)

tree.PreOrderTraversal(root)
print("Inorder")
#tree.InOrderTraversal(root)
print("PostOrder")
tree.PostOrderTraversal(root)