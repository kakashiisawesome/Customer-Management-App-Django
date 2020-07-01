def simple_middleware(get_response):
    # One-time configuration and initialization.
    print('Init called')

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print('before view')

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        print('after view')

        return response

    return middleware
