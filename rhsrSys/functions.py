def handle_uploaded_file(f):  
    with open('rhsrSys/static/rhsrSys/assets/uploaded/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  