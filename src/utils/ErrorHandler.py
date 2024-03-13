class ErrorHandler():
    def error_handler(err):
        error_name = type(err)
        error_parameters = err.args
        error_message = str(err)
        return {
            "error_name": type(err).__name__,
            "error_parameters": err.args,
            "error_message": str(err)
        }, 400