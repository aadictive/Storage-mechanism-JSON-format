################################################################################
### Storage-mechanism-JSON-format
# The project implements a simple JSON formatted storage mechanism to store documents.
# The document structure can be arbitrary and we need to return all the entities that
# match the given query
# Author : Aditya Chaudhari
# Created: August 18, 2021

################################## TESTCASES ###################################
example_input1 = ['add_record {"id":100,"lastname":"Peck","firstname":"Jane","location":{"city":"Binghamton","state":"NY","postalCode":"13905"},"active":true}',
'add_record {"id":101,"lastname":"Gardner","firstname":"Stanley","location":{"city":"Buffalo","state":"NY","postalCode":"14201"},"active":true}',
'add_record {"id":103,"lastname":"Cross","firstname":"Victor","location":{"city":"San Francisco","state":"CA","postalCode":"94105"},"active":true}',
'add_record {"id":104,"lastname":"Peck","firstname":"Jane","location":{"city":"Seattle","state":"WA","postalCode":"98204"},"active":false}',
'get_record {"location":{"state":"NY"},"active":true}',
'get_record {"id":101}']

#### Output:
# {"id":100,"lastname":"Peck","firstname":"Jane","location":{"city":"Binghamton","state":"NY","postalCode":"13905"},"active":true}
# {"id":101,"lastname":"Gardner","firstname":"Stanley","location":{"city":"Buffalo","state":"NY","postalCode":"14201"},"active":true}
# {"id":101,"lastname":"Gardner","firstname":"Stanley","location":{"city":"Buffalo","state":"NY","postalCode":"14201"},"active":true}


example_input2 = ['add_record {"id":100,"lastname":"Peck","firstname":"Jane","location":{"city":"Binghamton","state":"NY","postalCode":"13905"},"active":true}',
'add_record {"id":101,"lastname":"Gardner","firstname":"Stanley","location":{"city":"Buffalo","state":"NY","postalCode":"14201"},"active":true}',
'add_record {"id":103,"lastname":"Cross","firstname":"Victor","location":{"city":"San Francisco","state":"CA","postalCode":"94105"},"active":true}',
'add_record {"id":104,"lastname":"Peck","firstname":"Jane","location":{"city":"Seattle","state":"WA","postalCode":"98204"},"active":false}',
'delete_record {"active":true}',
'get_record {}']

#### Output:
# {"id":104,"lastname":"Peck","firstname":"Jane","location":{"city":"Seattle","state":"WA","postalCode":"98204"},"active":false}


example_input3 = ['add_record {"type":"list","list":[11,12,13,14]}',
'add_record {"type":"list","list":[12,13,14,15]}',
'add_record {"type":"list","list":[13,14,15,16]}',
'add_record {"type":"list","list":[14,15,16,17]}',
'add_record {"type":"list","list":[15,16,17,18]}',
'add_record {"type":"list","list":[16,17,18,19]}',
'get_record {"type":"list","list":[11]}',
'get_record {"type":"list","list":[13,14]}']

#### Output:
# {"type":"list","list":[11,12,13,14]}
# {"type":"list","list":[11,12,13,14]}
# {"type":"list","list":[12,13,14,15]}
# {"type":"list","list":[13,14,15,16]}

############################ MAIN CODE #########################################

import json

class StoreMechanism:
    def __init__(self):
        self.mainStore = {}
    
    def add_record(self,payload,entry_id):
        data = json.loads(payload)
        self.mainStore[entry_id] = data
    
    def get_record(self,payload):
        data = json.loads(payload)
        if data:
            for i in self.mainStore:
                flag_prev, flag_curr = True, False
                for key,value in data.items():
                    if type(value) == dict:
                        for k,v in value.items():
                            if i in self.mainStore and key in self.mainStore[i] and k in self.mainStore[i][key]:
                                if self.mainStore[i][key][k]== v:
                                    flag_curr=True
                                else:
                                    flag_curr=False
                                flag_prev = flag_prev and flag_curr      
                    elif type(value) == list:
                        for v in value:
                            if v in self.mainStore[i][key]:
                                flag_curr = True
                            else:
                                flag_curr = False
                            flag_prev = flag_prev and flag_curr
                    else:
                        if i in self.mainStore and key in self.mainStore[i]:
                            if self.mainStore[i][key] == value:
                                flag_curr=True
                            else:
                                flag_curr=False
                            flag_prev = flag_prev and flag_curr                 
                if flag_prev:
                    try:
                        print(json.dumps(self.mainStore[i],separators=(',', ':')))
                    except BrokenPipeError:
                        pass
        else:
            for i in self.mainStore:
                try:
                    print(json.dumps(self.mainStore[i],separators=(',', ':')))
                except BrokenPipeError:
                    pass
    
    def delete_record(self,payload):
        delArr = []
        data = json.loads(payload)
        if data:
            for i in range(0,len(self.mainStore)):
                flag_prev, flag_curr = True, False
                for key,value in data.items():
                    if type(value) == dict:
                        for k,v in value.items():
                            if i in self.mainStore and key in self.mainStore[i] and k in self.mainStore[i][key]:
                                if self.mainStore[i][key][k]== v:
                                    flag_curr=True
                                else:
                                    flag_curr=False
                                flag_prev = flag_prev and flag_curr
                    elif type(value) == list:
                        for v in value:
                            if v in self.mainStore[i][key]:
                                flag_curr = True
                            else:
                                flag_curr = False
                            flag_prev = flag_prev and flag_curr  
                    else:
                        if i in self.mainStore and key in self.mainStore[i]:
                            if self.mainStore[i][key] == value:
                                flag_curr=True
                            else:
                                flag_curr=False
                            flag_prev = flag_prev and flag_curr
                            
                if flag_prev:
                    delArr.append(i)
        self.update_store(delArr)
                    
    def update_store(self,delArr):
        for ele in delArr:
            if ele in self.mainStore:
                del self.mainStore[ele]

def getInput(queries):
    storemech = StoreMechanism()
    entry_id = 0
    for command in queries:
        if not command:
            return
        operation,payload = command.split(" ",maxsplit=1)
        if operation == "add_record":
            storemech.add_record(payload,entry_id)
            entry_id +=1
        elif operation == "get_record":
            storemech.get_record(payload)
        elif operation == "delete_record":
            storemech.delete_record(payload)
        else:
            return
    
if __name__ == "__main__":
  getInput(example_input1)