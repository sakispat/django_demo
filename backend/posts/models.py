from django.db import models


class Post(models.Model):
	title = models.CharField('Title', max_length=100, null=True)
	publiced_date = models.DateTimeField('Published Date')

	class Meta:
		db_table = 'posts'
		ordering = ('-publiced_date', )

	def __str__(self):
		return self.title