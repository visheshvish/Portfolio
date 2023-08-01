import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# Visheshkumar Vishwakarma
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Exploring technologies such as Cloud Computing, Artificial Intelligence, Machine Learning, Software Development, and working towards Real-Life problems to build unique and persist solutions.
- Expertise in Python Programming and efficiently skilled Core Java, SQL, GIT, Docker, PYQT6, Computer Vision, Shell/Bash Scripting, Terraform, MongoDB, AWS, Oracle Cloud Infrastructure (OCI), Flask, Django.
- Strong verbal and written communication skills, self directed learner & self assertive.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/visheshv/" target="_blank">Visheshkumar Vishwakarma</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Certification">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Catch-me-on">Catch me on</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text


def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


#####################
st.markdown('''
## Education
''')

txt('**Master of Science - Computer Science** (M.Sc CS), S K Somaiya Degree College, *Somaiya Vidyavihar University*, Mumbai, Maharashtra, India',
    '2021-2023')
st.markdown('''
- CGPA: `9.40`
''')


txt('**Bachelor of Science - Computer Science** (B.Sc CS), NES Ratnam College, *University Of Mumbai*, Maharashtra, India',
    '2018-2021')
st.markdown('''
- CGPA: `8.56`
- Graduated with First Class Honors.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Technology Associate 2**, Detect Technologies PVT LTD, IIT Madras Research Park, Chennai, Tamilnadu, India.',
    'November 2021 - September 2023')
st.markdown('''
- Designed and developed end-to-end python application, service and deployed into EC2 Instance (linux) to extract the Image data from the API and upload to AWS S3.
- Created an automation script using bash scripting to monitor AWS and Azure cloud infrastructure usage. Additionally, successfully optimized Docker images by 50% and pushed them to the Docker Registry.
- Engaged in complete DevOps lifecycle for computer vision applications, including installation, configuration, testing, and deployment on on-prem Linux servers, IoT devices (CCTV Camera), and EC2 Instances.
- Developed a Classification model utilizing Inception and trained it on a dataset of 10,000 images, achieving an accuracy of 80%.
''')

#####################
st.markdown('''
## Certifications
''')

txt('**AWS Cloud Practitioner Essentials**, [AWS](https://www.coursera.org/account/accomplishments/certificate/G267XZ332TN7)','Feb 2022 - March 2022')
txt('**Oracle Cloud Infrastructure Foundations 2021 Certified Associate**, [Oracle University](https://drive.google.com/file/d/1M3rKCTRaK6jv9HVO0P4dUy9nw7aGMyLt/view?usp=sharing), [Badge](https://catalog-education.oracle.com/pls/certview/sharebadge?id=9D05AA3A478E52613BA5A80FF126EF60D9EAC91EF7A0C523E612E6AA40EC284B)',
    'Jan 2022 - Feb 2022')
txt('**Crash Course On Python**, Coursera, Google, [View](https://www.coursera.org/account/accomplishments/certificate/LE9ZD69UZ24U)', 'April 2021 - June 2021')
txt('**IBM Data Science**, Coursera, IBM', 'Nov 2021 - Present')
txt('**Introduction to SQL**, [Datacamp](https://www.datacamp.com/statement-of-accomplishment/course/67ac07a978b578b6ee4379b1d0a987dcc3bc085a?share=true)', 'Sep 2021 - Sep 2021')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`,`OpenCV`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`')
txt3('Model deployment',
     '`streamlit`, `gradio`, `Heroku`, `AWS`, `Microsoft Azure`')
txt3('IaC', '`Terraform`')
txt3('SCM and VCS', '`GIT`, `Github`, `Gitlab`')
txt3('Containarization', '`Docker`')

#####################
st.markdown('''
## Catch Me On
''')
txt2('LinkedIn', '[Visheshkumar Vishwakarma](https://www.linkedin.com/in/visheshv/)')

txt2('GitHub', '[Visheshvish](https://github.com/visheshvish)')

txt2('Email', 'visheshv97@gmail.com')

txt2('Contact', '+91-9768764743')
