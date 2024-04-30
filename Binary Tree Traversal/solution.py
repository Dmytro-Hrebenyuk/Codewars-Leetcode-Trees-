# Pre-order traversal
def pre_order(node):
    lst = []
    if node:
        lst.append(node.data)
        lst.extend(pre_order(node.left))
        lst.extend(pre_order(node.right))
    return lst

# In-order traversal
def in_order(node):
    lst = []
    if node:
        lst.extend(in_order(node.left))
        lst.append(node.data)
        lst.extend(in_order(node.right))
    return lst

# Post-order traversal
def post_order(node):
    lst = []
    if node:
        lst.extend(post_order(node.left))
        lst.extend(post_order(node.right))
        lst.append(node.data)
    return lst
