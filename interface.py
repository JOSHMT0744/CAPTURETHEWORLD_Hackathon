import ipywidgets as widgets

### All the functions are defined here ###

def getReceiptImage(uploader):
    #display(uploader)

    uploaded_file = uploader.value[0]

    #image = widgets.Image(value=uploaded_file.content.tobytes())
    return uploaded_file