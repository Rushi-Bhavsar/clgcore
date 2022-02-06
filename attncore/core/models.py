from django.db import models


class Student(models.Model):
    GENDERS = (
        ("M", "Male"),
        ("F", "Female"),
        ("T", "Transgender"),
    )
    name = models.CharField(max_length=50, blank=False, default='Invalid')
    gender = models.CharField(max_length=1, choices=GENDERS, blank=False, default="M")
    email = models.CharField(max_length=45, blank=True)
    cell_no = models.CharField(max_length=15, blank=True, verbose_name='Cell No.')
    parent_cell_no = models.CharField(max_length=15, blank=True, verbose_name='Parents Cell No.')
    prn = models.CharField(max_length=12, blank=True)
    det_app_id = models.CharField(max_length=12, blank=True, verbose_name='DTE App. ID')


class StudentClass(models.Model):
    CLASSES = (
        ("FE", "First Year Engg."),
        ("SE", "Second Year Engg."),
        ("TE", "Third Year Engg."),
        ("BE", "Final Year Engg."),
        ("FYMCA", "First year MCA"),
        ("SYMCA", "Second year MCA"),
        ("ME-I", "First year ME"),
        ("ME-II", "Second Year ME")
    )
    BRANCHES = (
        ("CE", "Computer Engg."),
        ("CV", "Civil Engg."),
        ("ME", "Mechanical Engg."),
        ("EE", "Electrical Engg."),
        ("EC", "Electronics & Tele-comm. Engg."),
        ("MCA", "Masters in Computer Application"),
    )
    ADMSTAT = (
        ("RE", "Regular"),
        ("TD", "To detain"),
        ("DT", "Detained"),
        ("DC", "Discontinued")
    )
    courseclass = models.CharField(max_length=4, choices=CLASSES, verbose_name="Class")
    div = models.CharField(max_length=2, verbose_name="Division")
    Roll_No = models.IntegerField(max_length=2, verbose_name='Roll No.')
    Batch_No = models.CharField(max_length=4, blank=True, verbose_name='Batch No.')
    Branch = models.CharField(max_length=25, choices=BRANCHES)
    exam_seat_no = models.CharField(max_length=12, blank=True, verbose_name='Exam. Seat No.')
    moodle_id = models.CharField(max_length=25, blank=True, verbose_name='Moodle User Name')
    adm_date = models.DateField(blank=True, null=True, verbose_name='Admission Date')
    adm_status = models.CharField(max_length=2, blank=False, default="RE", choices=ADMSTAT,
                                  verbose_name="Admission Status")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class CourseStruct(models.Model):
    SEMS = (
        ("I", "Sem-I"),
        ("II", "Sem-II"),
        ("III", "Sem-III"),
        ("IV", "Sem-IV"),
        ("V", "Sem-V"),
        ("VI", "Sem-VI"),
        ("VII", "Sem-VII"),
        ("VIII", "Sem-VIII")
    )
    TEACHSCHM = (
        ("TH", "Theory"),
        ("PR", "Practical"),
        ("TU", "Tutorial")
    )
    EXAMSCHM = (
        ("TH", "Theory"),
        ("INSEM", "In-Sem Exam."),
        ("ENDSEM", "End-Sem Exam."),
        ("PR", "Practical"),
        ("TW", "Term-work"),
        ("OR", "Oral"),
        ("SM", "Seminar"),
        ("PROJ", "Project")
    )
    coursePattern = models.CharField(max_length=40),
    semester = models.CharField(max_length=4, choices=SEMS),
    courseName = models.CharField(max_length=50),
    courseCode = models.CharField(max_length=15, verbose_name="Course Name"),
    teachScheme = models.CharField(max_length=2, choices=TEACHSCHM, verbose_name="Teaching Scheme"),
    examScheme = models.CharField(max_length=5, choices=EXAMSCHM, verbose_name="Exam Scheme"),
    max_marks1 = models.CharField
