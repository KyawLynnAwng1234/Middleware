from django.shortcuts import render

class SimpleRequestResponseMiddleware:
    """
    This is a simple middleware to show how requests and responses are processed.
    It prints a message to the console for every incoming request and outgoing response.
    """

    # This method is called once when the middleware is initialized.
    def __init__(self, get_response):
        self.get_response = get_response
        print("SimpleRequestResponseMiddleware is ready!")

    # This method is called for every request.
    def __call__(self, request):
        print("A new request is coming in! Path:", request.path)

        # The request is now passed on to the next middleware or the view function.
        response = self.get_response(request)

        # The response is processed here before it is sent back to the client.
        print("A response is going out! Status code:", response.status_code)

        return response
        
    
