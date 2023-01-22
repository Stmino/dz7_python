import  create_txt as model
import view
import read_txt as read

def button_click(): 
    id = view.get_id()
    fi = view.get_fi()
    num=view.get_num()
    comment=view.get_com()
    model.init(id,fi,num,comment)
    model.do_it(id,fi,num,comment)
    read.read_txt_sorted()
    cont= view.cont()
    if cont == 'da':
        return button_click()
    else:
        print (read.read_txt())
        print (read.read_txt_id())
        
    
   
    

    
    

    