from django.db import models


class Projects(models.Model):
    
    STATUS_CHOICES = [
        ('Published', 'Published'),
        ('Hide', 'Hide'),
    ]
    STATE_CHOICES = [
        ('Perak', 'Perak'),
        ('Selangor', 'Selangor'),
        ('Johor', 'Johor'),
        ('Kedah', 'Kedah'),
        ('Kelantan', 'Kelantan'),
        ('Melaka', 'Melaka'),
        ('Pahang', 'Pahang'),
        ('Pulau Pinang', 'Pulau Pinang'),
        ('Perlis', 'Perlis'),
        ('Terengganu', 'Terengganu'),
        ('Sabah', 'Sabah'),
        ('Sarawak', 'Sarawak'),
        ('Negeri Sembilan', 'Negeri Sembilan'),
        ('Kuala Lumpur', 'Kuala Lumpur'),
        ('Labuan', 'Labuan'),
        ('Putrajaya', 'Putrajaya'),
    ]
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    banner_img = models.ImageField(upload_to='projects/')
    project_name = models.CharField(max_length=100)
    
    project_state = models.CharField(max_length=50, choices=STATE_CHOICES)

    # IMPORTANT: city is dynamic (no choices)
    city = models.CharField(max_length=100)
    project_desc = models.TextField(blank=True, null=True)

    property_ownership = models.CharField(
        max_length=20,
        choices=[
            ('Freehold', 'Freehold'),
            ('Leasehold', 'Leasehold')
        ]
    )

    progress_tag = models.CharField(
        max_length=20,
        choices=[
            ('Past', 'Past'),
            ('On Going', 'On Going'),
            ('Upcoming', 'Upcoming')
        ]
    )
    
    waze_link = models.URLField(blank=True, null=True, help_text="Paste Waze link here")
    google_maps_link = models.URLField(blank=True, null=True, help_text="Paste Google Maps link here")

    special_features = models.TextField()
    total_units = models.IntegerField()

    floorplan_img = models.ImageField(upload_to='projects/floorplans/', blank=True, null=True)
    gallery_img = models.ImageField(upload_to='projects/gallery/', blank=True, null=True)
    brochure_location = models.ImageField(upload_to='projects/brochures_location/', blank=True, null=True)
    brochure = models.FileField(upload_to='projects/brochures/', blank=True, null=True)

    def __str__(self):
        return self.project_name