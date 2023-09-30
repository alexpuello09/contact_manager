from flask import Flask,request

app = Flask(__name__)
contacts = [
        {
            "id":"id",
            "name": "name",
            "phone number": "phone number",
            "address": "address",
            "email": "email",
        }
            ]

#Request the list of contacts 
@app.route("/contact", methods = ["GET"])
def request_contact():
    return contacts

#Create a contact
@app.route("/contact", methods = ["POST"])
def create_contact():
    data_contact = request.get_json()
    new_contact = {
            "id": len(contacts) + 1,
            "name": data_contact['name'],
            "phone number": data_contact['phone number'],
            "address": data_contact['address'],
            "email": data_contact['email'],
        }
    contacts.append(new_contact)
    return "Contact created successfully"

#Update a contact
@app.route("/contact/<int:id_contact>", methods = ["PUT"])
def update_contact(id_contact):
    data_updated = request.get_json()
    for contact in contacts:
        if contact['id'] == id_contact:
            contact['name'] = data_updated["name"]
            contact['phone number'] = data_updated["phone number"]
            contact['address'] = data_updated["address"]
            contact['email'] = data_updated["email"]
            return f"Contact updated successfully"
    return f"Contact with id {id_contact} not found"


#Delete a contact
@app.route("/contact/<int:id_delete>", methods = ["DELETE"])
def delete_contact(id_delete):
    for contact_del in contacts:
        if contact_del["id"] == id_delete:
            contacts.remove(contact_del)
            return f"Contact with id {id_delete} deleted successfully"
    return f"Error: Contact with id {id_delete} not found"
        
