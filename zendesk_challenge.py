#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


class Zendesk_Api:

    def Zendesk_ticket_app(self):
        # In[67]:


        response = requests.get("https://zccticketdomain.zendesk.com/api/v2/tickets.json",auth=('user_auth', 'user_pass'))
        if(response.status_code!=200):
            print("Sorry,Maybe API is unavailable or  check connection details  ")
            raise Exception("Bad request")


        # In[59]:


        tickets= response.json()

        # In[ ]:


        print("Welcome to the ticket viewer")

        menu = input("Type 'menu' to view options or 'quit' to exit : ")
        if(menu =='quit'):
            return 0
        elif(menu !='menu'): 
            return 0

        #display the menu
        print("Select view options ")
        print("*1 to view all tickets")
        print("*2 to view a specific ticket")
        print("*3 type'quit' to exit")

        #input the selection
        selection = input()

        if(selection == 'quit'):
                return 0
        else:
                selection= int(selection)


            
        onclick =1
        #selection 1 then show all tickets else request ticket number and show specific ticket
        if(selection==1):
            ticket_list = tickets['tickets'][:]
            print("Currently on page 1 ")
            ctr = 0
            for ticket in ticket_list:
                subject = ticket['subject']
                date_created =  ticket['created_at']
                print("Ticket with subject ",subject," was created on",date_created)
                ctr+=1
                if(ctr==100):
                    break
                if(ctr%25==0):
                    onclick = input("Press N to display next page or type quit to exit : ")
                if(onclick == 'quit'):
                    return 0
                elif(onclick == 'N'):
                    continue
                    
                
                
        else:
        #     url = "https://zccticketdomain.zendesk.com/api/v2/tickets.json"
        #     response = requests.get(url, auth=('ssnemman@ncsu.edu', 'zccpass066'),params='tickets')
        #     ticket_temp = response.json()
        #     print(ticket_temp)

            ticket_number = int(input("Enter ticket number : "))
            #check condition if ticket is valid
            ticket_list = tickets['tickets'][:]
            result =''
            for spec in ticket_list:
                if(spec['id']==ticket_number):
        #             print(spec)
                    result = spec
            
            if(result == ''):
                print("Something is wrong .Please check the ticket number.")
                raise SystemExit
                
            #display contents for that particular ticket.
            subject = result['subject']
            date_created =  result['created_at']
            print("Ticket with subject ",subject," was created on",date_created)
        
        return 1
            
if __name__ == "__main__":
        zendesk_instance = Zendesk_Api()
        zendesk_instance.Zendesk_ticket_app()


