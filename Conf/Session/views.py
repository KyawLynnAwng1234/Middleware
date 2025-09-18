from django.shortcuts import render
from django.http import HttpResponse

def set_session_data(request):
    """
    This view sets the user's name and visit count in the session.
    It checks if 'username' is already in the session.
    """
    if 'username' not in request.session:
        request.session['username'] = 'Guest'
        request.session['visit_count'] = 0
        return HttpResponse("Session data has been set. Go to /show_session to see it.")
    else:
        return HttpResponse("Session data already exists. Go to /show_session.")

def show_session_data(request):
    """
    This view retrieves data from the session and displays it.
    It also increments the visit count for every page refresh.
    """
    # Get the data from the session. If it doesn't exist, use default values.
    username = request.session.get('username', 'User')
    visit_count = request.session.get('visit_count', 0)

    # Increment the visit count and save it back to the session.
    visit_count += 1
    request.session['visit_count'] = visit_count

    # Prepare the response text.
    response_text = f"Hello, {username}! You have visited this page {visit_count} times."

    return HttpResponse(response_text)
