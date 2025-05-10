from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='fk_tasks_category', null=True, blank=True)
    
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['id']

    def __str__(self):
        if self.category is None:
            return f"{self.title} - No Category"
        return f"{self.title} - {self.category.name}"

