def buscar(self, prev_data = []):
    if self._children:
        child_data = []
        for child in self.children:
            child_data.extend(child.tree2list(prev_data + self._data))
        return child_data
    else:
        return [prev_data + self._data]

tree = (3, (1, None, None), (8, None, (13, (9, None, None), None)))

print (buscar(tree))