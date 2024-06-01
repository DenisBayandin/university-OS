from my_system import System


system = System()
system.touch("test.txt", "Hello! This is test.txt")
system.touch("test1.txt", "Hello! This is test1.txt")
system.touch("denis.txt", "Hello! This is denis.txt")
print(f"All file system:\n{system.ls}")
system.rm("denis.txt")
print(f"All file system after delete file:\n{system.ls}")
print(f"Search files by 'tes':\n{system.search_file('tes')}")
print(f"Read file 'test.txt':\n{system.cat('test.txt')}")


#  Raise error after validation!!
#system.touch("testtesttesttesttesttesttesttesttesttesttesttesttest.txt", "Hello! This is test.txt")
#system.touch("test", "Hello! This is test.txt")
#system.touch("test.dsadad", "Hello! This is test.txt")
#system.touch("test.txt", "testtesttesttesttesttesttesttesttesttesttesttesttestasdasdasdasdsatesttesttestt"
#                            "esttesttesttesttesttesttesttesttesttestasdasdasdasdsa")
#system.cat("sadsa")
#system.rm("asdadas")
