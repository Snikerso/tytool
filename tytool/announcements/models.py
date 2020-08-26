from django.db import models



class AnnouncmentsScienceTool(models.Model):
    title = models.TextField(max_length=32,blank=False,null=False)
    description = models.TextField(max_length=32,blank=False,null=False)

    
    def __str__(self):
        return self.title


class AnnouncmentsArtTool(models.Model):
    title = models.TextField(max_length=32,blank=False,null=False)
    description = models.TextField(max_length=32,blank=False,null=False)

    
    def __str__(self):
        return self.title
