

from collections import OrderedDict

##################################################################
class BaseCaching():
    """ BaseCaching defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
###################################

# MRUCache
class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        
    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item
            # self.cache_data.move_to_end(key, last=False)
        
    def get(self, key):
        if key not in self.cache_data:
            return 
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)

# class LRUCache(BaseCaching):
#     def __init__(self):
#         super().__init__()
#         self.cache_data = OrderedDict()
        
#     def put(self, key, item):
#         if key in self.cache_data:
#             self.cache_data.move_to_end(key)
#         self.cache_data[key] = item
        
#         if len(self.cache_data) > BaseCaching.MAX_ITEMS:
#             lru_key, _ = self.cache_data.popitem(last=False)
#             print("DISCARD:",lru_key)
#             # self.cache_data.popitem(last=False)
        
        
        
        
#     def get(self, key):
#         if key not in self.cache_data:
#             return -1
        
#         if key in self.cache_data:
#             self.cache_data.move_to_end(key)
#         return self.cache_data[key]



# class LIFOCache(BaseCaching):
#     def __init__(self):
#         super().__init__()
#         self.cache_data = OrderedDict()
#     def put(self, key, item):
#         if key in self.cache_data:
#             self.cache_data.pop(key)
        
#         if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
#             first_key,_ = self.cache_data.popitem(last=True)
#             print("DISCARD:", first_key)
#         self.cache_data[key] = item
#     def get(self, key):
#         return self.cache_data.get(key, None)
    
    
    
# class BasicCache(BaseCaching):
#     def put(self, key, item):
#         if key and item:
#             self.cache_data[key] = item
#     def get(self, key):
#             return self.cache_data.get(key,None)
        
#######################3



my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()


# my_cache = LRUCache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.put("D", "School")
# my_cache.print_cache()
# print(my_cache.get("B"))
# my_cache.put("E", "Battery")
# my_cache.print_cache()
# my_cache.put("C", "Street")
# my_cache.print_cache()
# print(my_cache.get("A"))
# print(my_cache.get("B"))
# print(my_cache.get("C"))
# my_cache.put("F", "Mission")
# my_cache.print_cache()
# my_cache.put("G", "San Francisco")
# my_cache.print_cache()
# my_cache.put("H", "H")
# my_cache.print_cache()
# my_cache.put("I", "I")
# my_cache.print_cache()
# my_cache.put("J", "J")
# my_cache.print_cache()
# my_cache.put("K", "K")
# my_cache.print_cache()


# my_cache = LIFOCache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.put("D", "School")
# my_cache.print_cache()
# my_cache.put("E", "Battery")
# my_cache.print_cache()
# my_cache.put("C", "Street")
# my_cache.print_cache()
# my_cache.put("F", "Mission")
# my_cache.print_cache()
# my_cache.put("G", "San Francisco")
# my_cache.print_cache()










# my_cache = FIFOCache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.put("D", "School")
# my_cache.print_cache()
# my_cache.put("E", "Battery")
# my_cache.print_cache()
# my_cache.put("C", "Street")
# my_cache.print_cache()
# my_cache.put("F", "Mission")
# my_cache.print_cache()




# my_cache = BasicCache()
# my_cache.print_cache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.print_cache()
# print(my_cache.get("A"))
# print(my_cache.get("B"))
# print(my_cache.get("C"))
# print(my_cache.get("D"))
# my_cache.print_cache()
# my_cache.put("D", "School")
# my_cache.put("E", "Battery")
# my_cache.put("A", "Street")
# my_cache.print_cache()
# print(my_cache.get("A"))
