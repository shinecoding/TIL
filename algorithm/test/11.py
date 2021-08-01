class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None

def Solution(node):
    cur_node = node
    runner_node = None
    while cur_node is not None:
        runner_node = cur_node
        while runner_node is not None:
            if runner_node.next.data == cur_node.data :
                runner_node.next = runner_node.next.next
            else :
                runner_node = runner_node.next
        cur_node = cur_node.next
    return



