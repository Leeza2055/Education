from django.db import models

# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Slider(TimeStamp):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="slider")

    def __str__(self):
        return self.title


class Organization(TimeStamp):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="logo")
    about = models.TextField(null=True, blank=True)
    about_image1 = models.ImageField(upload_to="organization")
    about_image2 = models.ImageField(upload_to="organization")
    mission_vision = models.TextField(null=True, blank=True)
    graduated_students = models.PositiveIntegerField()
    certified_teachers = models.PositiveIntegerField()
    years = models.PositiveIntegerField()
    email = models.EmailField()
    phone_no = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Program(TimeStamp):
    title = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    image = models.ImageField(upload_to="program")

    def __str__(self):
        return self.title


class Semester(TimeStamp):
    title = models.CharField(max_length=50)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    syllabus = models.FileField(upload_to="syllabus")

    def __str__(self):
        return self.title


class Subject(TimeStamp):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=200, unique=True)
    credit_hour = models.CharField(max_length=50)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


POST = (
    ("lecturer", "Lecturer"),
    ("assistant_professor", "Assistant Professor"),
    ("professor", "Professor"),
)


class Teacher(TimeStamp):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="teacher")
    program = models.ManyToManyField(Program)
    is_hod = models.BooleanField(default=False)
    education = models.CharField(max_length=50)
    post = models.CharField(max_length=100, choices=POST)

    def __str__(self):
        return self.name


class Facility(TimeStamp):
    title = models.CharField(max_length=20)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Facility")

    def __str__(self):
        return self.title


class Event(TimeStamp):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="event")
    content = models.TextField()
    date = models.DateField()
    venue = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Testimonials(TimeStamp):
    name = models.CharField(max_length=20)
    sayings = models.TextField()
    current_engagement = models.CharField(max_length=50)
    image = models.ImageField(upload_to="testimonials")

    def __str__(self):
        return self.name


GENDER = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
)


PROGRAM_TIME = (
    ('day', 'Day'),
    ('morning', 'Morning'),
)


class Application(TimeStamp):
    name = models.CharField(max_length=20)
    date_of_birth = models.DateField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    program_time = models.CharField(max_length=50, choices=PROGRAM_TIME)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.PositiveIntegerField()
    slc_pct = models.DecimalField(max_digits=5, decimal_places=2)
    plus2_pct = models.DecimalField(max_digits=5, decimal_places=2)
    slc_marksheet = models.FileField(upload_to="slc")
    plus2_transcript = models.FileField(upload_to="plus2")

    def __str__(self):
        return self.name
