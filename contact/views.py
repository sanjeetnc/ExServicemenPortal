from django.shortcuts import render, redirect
from .forms import EnquiryForm


def contact_page(request):

    if request.method == "POST":

        form = EnquiryForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
    
            form.save()

            messages.success(
                request,
                "Your enquiry has been submitted successfully."
            )

            return redirect('contact')

    else:

        form = EnquiryForm()

    return render(
        request,
        'contact/contact.html',
        {
            'form': form
        }
    )