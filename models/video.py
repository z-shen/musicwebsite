from common.database import Database

class Video(object):
    def __init__(self,account,title='None',link='None',image='None',time='None'):
        self.account = account
        self.title = title
        self.link = link
        self.image = image
        self.time = time
        self.database = Database('localhost:27017','videos')

    def save_to_db(self):
        print("save_to_db")

        self.database.insert(collection='video',data=self.json())

    def fine_video(self,account):
        result = self.database.find(collection='video', data={'account': account})
        return result

    def delete_video(self,account,link):
         self.database.remove(collection='video', data={'account': account,'link': link})


    def json(self):
        return {
            'account': self.account,
            'title' : self.title,
            'link' : self.link,
            'image' : self.image,
            'time' : self.time
        }



