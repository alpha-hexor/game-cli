import httpx


class Torrent:
    def __init__(self):
        self.url = "http://127.0.0.1:8080/api/v2/"
        self.client = httpx.Client()
        
    def login(self,username,password):
        """
        function to login into the webui
        parameters={
            "username" : "admin"
            "password" : "adminadmin"
        }
        """
        try:
            r=self.client.post(
                f"{self.url}auth/login",
                data={
                    "username" : username,
                    "password" : password
                }
            )
            if r.text == "Ok.":
                return 1
            else:
                return 0
        except:
            print("[*]Please qbit torrent first")
            exit()
            
    def add_link(self,magnet_link,save_path):
        """
        function to add a link in the torrent
        parameters={
            'urls' : magnet_link,
            'savepath': save_path
            'paused' : true //for testing only 
        }
        """
        r=self.client.post(
            f"{self.url}torrents/add",
            data={
                "urls" : magnet_link,
                "savepath" : save_path
            }
            
        )
        if r.text == "Ok.":
            return 1
        else:
            return 0
        