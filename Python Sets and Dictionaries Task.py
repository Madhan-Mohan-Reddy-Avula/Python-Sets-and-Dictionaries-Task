class DataAnalyzer:
    def __init__(self):
        self.data_set = set()
        self.data_dict = {}

    def add_to_set(self, elements):
        self.data_set.update(elements)

    def remove_from_set(self, element):
        if element in self.data_set:
            self.data_set.remove(element)

    def get_set(self):
        return self.data_set

    def create_dictionary(self, keys, values):
        if len(keys) == len(values):
            self.data_dict = dict(zip(keys, values))
        else:
            print("Error: The lengths of keys and values lists are not equal.")

    def update_dictionary(self, key, value):
        self.data_dict[key] = value

    def get_dictionary(self):
        return self.data_dict

    def search_dictionary(self, key):
        return key in self.data_dict

    def remove_from_dictionary(self, key):
        if key in self.data_dict:
            del self.data_dict[key]

# Example usage:
da = DataAnalyzer()
da.add_to_set([1, 2, 3, 4, 2, 3, 5])
print("Current Set:", da.get_set())

da.remove_from_set(3)
print("Set after removing element 3:", da.get_set())

da.create_dictionary(['a', 'b', 'c'], [1, 2, 3])
print("Current Dictionary:", da.get_dictionary())

da.update_dictionary('d', 4)
print("Dictionary after update:", da.get_dictionary())

print("Is 'b' in dictionary?", da.search_dictionary('b'))

da.remove_from_dictionary('b')
print("Dictionary after removing 'b':", da.get_dictionary())
