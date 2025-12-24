from django.core.management.base import BaseCommand
from portfolio.models import Profile, Project, Skill, Education, Experience

class Command(BaseCommand):
    help = 'Seeds the database with portfolio data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Profile.objects.all().delete()
        Project.objects.all().delete()
        Skill.objects.all().delete()
        Education.objects.all().delete()
        Experience.objects.all().delete()

        # Create Profile
        Profile.objects.create(
            name="Gurram Prem Sai",
            role="Python Developer | Django Backend Engineer",
            bio="I am a backend-oriented Python developer based in Bengaluru. With a strong foundation in Django and Python, I build scalable web applications. My passion lies in solving complex problems and creating educational platforms.",
            email="premsaiachari1213@gmail.com",
            github_link="https://github.com/premsai08",
            linkedin_link="https://www.linkedin.com/in/prem-sai-achaari-739571236",
            profile_image="profile/profile.jpg"
        )

        # Projects
        Project.objects.create(
            title="Addition – Full Stack Web Application",
            description="An educational web application for children to learn addition using interactive games, animations, randomized questions, and score tracking. Backend developed using Python and Django.",
            tech_stack="Python, Django, HTML5, CSS3, JavaScript",
            is_featured=True,
            image="projects/addition.jpg"
        )

        Project.objects.create(
            title="Urdhva–Tiryagbhyam Learning Platform",
            description="A Vedic Mathematics based learning platform that teaches fast mathematical techniques using interactive explanations, practice modules, and animations. Backend built using Python and Django.",
            tech_stack="Python, Django, SQLite, Vedic Math Logic",
            is_featured=True,
            image="projects/urdhva_1.jpg"
        )

        # Skills
        skills_data = [
            ("Python", 95, "fab fa-python", True),
            ("Django", 90, "fas fa-server", True),
            ("SQL", 85, "fas fa-database", False),
            ("REST APIs", 85, "fas fa-globe", False),
            ("HTML5", 80, "fab fa-html5", False),
            ("CSS3", 75, "fab fa-css3-alt", False),
            ("JavaScript", 70, "fab fa-js", False),
            ("Git & GitHub", 80, "fab fa-github", False),
        ]

        for name, prof, icon, primary in skills_data:
            Skill.objects.create(name=name, proficiency=prof, icon_class=icon, is_primary=primary)

        # Education
        Education.objects.create(
            institution="Annamacharya Institute of Technology and Sciences, Tirupati",
            degree="B.Tech in ECE",
            year="2021–2025",
            grade="7.08",
            order=1
        )
        Education.objects.create(
            institution="College Name (Intermediate)",
            degree="Intermediate (MPC)",
            year="2019-2021",
            grade="A",
            order=2
        )
         # Added placeholder for SSC as requested, details weren't fully provided but structure is there.
        Education.objects.create(
            institution="School Name (SSC)",
            degree="SSC",
            year="2019",
            grade="A",
            order=3
        )

        # Experience
        Experience.objects.create(
            company="Slashmark",
            role="Python Development Intern",
            duration="Recent",
            description="Worked on Python modules, OOP concepts, file handling, and writing clean, maintainable code."
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded portfolio data'))
