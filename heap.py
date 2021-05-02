class Heap:
    def __init__(self, size):
        self.heap_size = 0
        self.max_size = size + 1
        self.custom_list = (size+1) * [None]


def peek_heap(root):
    if not root:
        return
    else:
        return root.custom_list[1]


def size_of_heap(root):
    if not root.custom_list:
        return 'empty!'
    else:
        return root.heap_size+1


def level_order_traverse(root):
    if not root:
        return 'empty!'
    else:
        for i in range(1, root.heap_size + 1):
            print(root.custom_list[i])


def heapify_insert(root, index, heaptype):
    parent_index = index // 2
    if index <= 1:
        return
    if heaptype == "min":
        if root.custom_list[index] < root.custom_list[parent_index]:
            root.custom_list[index], root.custom_list[parent_index] = root.custom_list[parent_index], root.custom_list[
                index]
        heapify_insert(root, parent_index, heaptype)
    if heaptype == "max":
        if root.custom_list[index] > root.custom_list[parent_index]:
            root.custom_list[index], root.custom_list[parent_index] = root.custom_list[parent_index], root.custom_list[
                index]
        heapify_insert(root, parent_index, heaptype)


def insertion(root, value, heap_type):
    if root.heap_size + 1 == root.max_size:
        return " full!"
    else:
        root.custom_list[root.heap_size + 1] = value
        root.heap_size += 1
        heapify_insert(root, root.heap_size, heap_type)
        return 'value inserted!'


def heapify_extract(root, index, type):
    left_index = 2 * index
    right_index = index * 2 + 1
    swap_child = 0

    if root.heap_size < left_index:
        return
    elif root.heap_size == left_index:
        if type == 'min':
            if root.custom_list[index] > root.custom_list[left_index]:
                root.custom_list[index], root.custom_list[left_index] = root.custom_list[left_index], root.custom_list[
                    index]
            return
        else: # for max heap case
            if root.custom_list[index] < root.custom_list[left_index]:
                temp = root.custom_list[index]
                root.custom_list[index] = root.custom_list[left_index]
                root.custom_list[left_index] = temp
            return
    else: # for right index 
        if type == 'min':
            if root.custom_list[left_index] < root.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root.custom_list[index] > root.custom_list[swap_child]:
                root.custom_list[index], root.custom_list[swap_child] = root.custom_list[swap_child], root.custom_list[
                    index]
        else:
            if root.custom_list[left_index] > root.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root.custom_list[index] < root.custom_list[swap_child]:
                root.custom_list[index], root.custom_list[swap_child] = root.custom_list[swap_child], root.custom_list[
                    index]
    heapify_extract(root, swap_child, type)


def extract_node(root, type):
    if root.heap_size == 0:
        return
    else:
        extracted_node = root.custom_list[1]
        root.custom_list[1] = root.custom_list[root.heap_size]
        root.custom_list[root.heap_size] = None
        root.heap_size -= 1
        heapify_extract(root, 1, type)
        return extracted_node


def delete_tree(root):
    root.custom_list = None


new_heap = Heap(5)
insertion(new_heap, 4, 'min')
insertion(new_heap, 5, 'min')
insertion(new_heap, 2, 'min')
insertion(new_heap, 1, 'min')
level_order_traverse(new_heap)
print(extract_node(new_heap, 'min'))
print(size_of_heap(new_heap))
delete_tree(new_heap)
print(size_of_heap(new_heap))
