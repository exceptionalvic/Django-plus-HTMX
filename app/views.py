from django.shortcuts import render
from .models import Contact
from django.views.generic.list import ListView

def create_contact(request):
    name = request.POST.get('contactname') # get data from form where name="contactname"
    phone_number = request.POST.get('phone_number') # get data from form where name="phone_number"
    
    # add contact
    contact = Contact.objects.create(name=name, phone_number=phone_number) # add contact to databse
    contacts = Contact.objects.all()
    return render(request, 'contact-list.html', {'contacts': contacts}) # display the list of contacts in contact-list.html

class ContactList(ListView):
    template_name = 'contact.html' # html file to display the list of contacts
    model = Contact
    context_object_name = 'contacts' # used in the HTML template to loop through and list contacts

def delete_contact(request, pk):
    # remove the contact from list.
    contact_id = Contact.objects.get(id=pk)
    contact_id.delete()
    contacts = Contact.objects.all()
    return render(request, 'contact-list.html', {'contacts': contacts})