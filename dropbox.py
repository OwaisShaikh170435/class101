import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AxG2PW4MbhmztSbOUzQeEWy8eOKR3-Rzb-OuEpksO4CmH1YWLMt_otWYHTWAVqjSQ84o_605Z7yt3Duf0gMuqpbQqt9TfPI70fRcVGtPcpLMy9Y0Y6yOavGiHeJYvYQGa-2Bpcc'
    transerData = TransferData(access_token)

    file_from = input("enter the file paths to transfer:")
    file_to = input("enter the full path to upload to dropbox:")

    transferData.upload_file(file_from, file_to)
    print("file has been moved")

main()    
