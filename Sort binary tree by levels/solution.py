from collections import deque
def tree_by_levels(root):
    result = []
    if root is None:
        return result

    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.extend(current_level)

    return result