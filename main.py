from todo import Todo

k_todo = Todo(name='Alfred')
e_todo = Todo(name='Emmanuel')
#print(k_todo)

#print(repr(k_todo)) #gives the signature
#print(e_todo)

k_todo.add('buy milk')
k_todo.add('code python')
k_todo.add('cook dinner')

e_todo.add('code')
e_todo.add('wake up')


#creat an object, add one then give me the len

#print(len(k_todo))
#print(len(e_todo))

print(k_todo > e_todo)
print(k_todo < e_todo)

