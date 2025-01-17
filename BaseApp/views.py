from django.shortcuts import render,redirect
from BaseApp.models import FeedbackDb
from BaseApp.models import RecipesDb

# Create your views here.
def HomeView(request):
    return render(request,"Home.html")

def RecipesView(request):
    recipes = RecipesDb.objects.all()
    return render(request, 'Recipes.html', {'recipes': recipes})

def Add_RecipeView(request):
    return render(request,"Add_recipe.html")

def SaveRecipes(request):
    if request.method == 'POST':
        username = request.POST['username']
        dishname = request.POST['dishname']
        ingredients = request.POST['ingredients']
        recipe = request.POST['recipe']
        data = RecipesDb(username=username, dishname=dishname,ingredients=ingredients, recipe=recipe)
        data.save()
    return redirect('Add_Recipe')  # Redirect to refresh the page

def FeedbackView(request):
    feedbacks = FeedbackDb.objects.all()
    return render(request, "Feedback.html",{'feedbacks':feedbacks})

def SaveFeedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('query')
        feedback = request.POST.get('feedback')
        data = FeedbackDb(name=name,email=email,query=query,feedback=feedback)
        data.save()
    return redirect("Feedback")

def AboutView(request):
    return render(request, "About.html")