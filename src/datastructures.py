
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
        "id": self._generateId(),
        "first_name": "John",
        "last_name": "Jackson",
        "age": 33,
        "lucky_numbers": [7, 13, 22]
        },
        {
        "id": self._generateId(),
        "first_name": "Jane",
        "last_name": "Jackson",
        "age": 35,
        "lucky_numbers": [10, 14, 3]
        },
        {
        "id": self._generateId(),
        "first_name": "Jimmy",
        "last_name": "Jackson",
        "age": 5,
        "lucky_numbers": [1]
        }
        ]
         
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if member["id"] == None:
             member["id"]=self._generateId()
        member["last_name"]="Jackson"
        self._members.append(member)
        return member

    def delete_member(self, id):
        # fill this method and update the return
        delete_member = list(filter(lambda person:person["id"]==id, self._members))
        
        if len(delete_member)==0:
            return "no encontrado"
        else:
             self._members.remove(delete_member[0])
             return self._members

    def get_member(self, id):
        # fill this method and update the return
        member = list(filter(lambda person:person["id"]==id, self._members))
        if len(member)==0:
            return "sin datos"
        else:
            getmember={
                "first_name": member[0]["first_name"],
                "age": member[0]["age"],
                "lucky_numbers": member[0]["lucky_numbers"],
                "id":id
            }
            return getmember
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
