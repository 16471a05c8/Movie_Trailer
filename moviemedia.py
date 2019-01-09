import webbrowser

class Animation():
     def __init__(self,m_title,m_storyline,m_poster,m_youtube):
          self.title=m_title
          self.story=m_storyline
          self.poster=m_poster
          self.youtube=m_youtube
     def show_movie_traile(self):
          webbrowser.open(self.youtube)
