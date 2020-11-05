''' Examples of read/write files '''

file = open("D:\prova_python.txt", 'w')     # if the file does not exist, it will be created
                                            # 'a' -> append
file.write("Riga 1")
file.close()