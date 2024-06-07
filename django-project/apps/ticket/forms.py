from django import forms


class PurchaseTicketForm(forms.Form):
    QUANTITY_CHOICES = [
        (1, '1 Ticket'),
        (2, '2 Tickets'),
        (3, '3 Tickets'),
        (4, '4 Tickets'),
        (5, '5 Tickets'),
    ]

    TICKET_CLASS_CHOICES = [
        ('first', 'First'),
        ('second', 'Second'),
        ('Third', 'First third'),
    ]

    SEAT_LOCATION_CHOICES = [
        ('window', 'Window'),
        ('aisle', 'Aisle'),
        ('middle', 'Middle'),
    ]

    quantity = forms.ChoiceField(choices=QUANTITY_CHOICES)
    ticket_class = forms.ChoiceField(choices=TICKET_CLASS_CHOICES)
    seat_location = forms.ChoiceField(choices=SEAT_LOCATION_CHOICES)