from django.shortcuts import render, redirect
from .models import Package, Membership
from .forms import MembershipForm

def home(request):
    packages = Package.objects.all()
    return render(request, 'gym/home.html', {'packages': packages})

def about_us(request):
    return render(request, 'gym/about_us.html')

def membership(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            membership = form.save(commit=False)
            membership.price = membership.package.price
            membership.save()
            return redirect('confirmation', membership_id=membership.id)
    else:
        form = MembershipForm()
    return render(request, 'gym/membership.html', {'form': form})

def confirmation(request, membership_id):
    membership = Membership.objects.get(id=membership_id)
    return render(request, 'gym/confirmation.html', {'membership': membership})

def trainer(request):
    return render(request, 'gym/trainer.html')