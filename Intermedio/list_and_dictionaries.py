def run():

    my_list= [1,"Hello", True,4.5]
    my_dict= {"firstname": "Facundo", "Lastname":"García"}

    superlist=[ 
        {"firstname": "Frank", "Lastname":"Carvajal"},
        {"firstname": "Luigui", "Lastname":"Alarcon"},
        {"firstname": "Miguel", "Lastname":"García"},
    ]

    super_dict={
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-1,-2,0,4,5],        
        "floating_nums" : [2.3,1.2,0.4,4.4]        

    }

    for key,value in super_dict.items():
        print(key,value)
    for values in superlist:
        print(values)
        for key, value in values.items():
            print(f'{key} - {value}')
    for i in superlist:
	    print(i.items(),end=" ")       
if __name__ == "__main__":
    run()