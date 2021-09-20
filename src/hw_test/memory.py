import gc
mem_alloc = gc.mem_alloc()
mem_free = gc.mem_free()
capacity = mem_alloc + mem_free
print("    capacity\tfree\tusage")
print("    {}\t{}\t{}%".format(capacity, mem_free, int(
    ((capacity - mem_free) / capacity) * 100.0)))
import micropython
micropython.mem_info(1) 
