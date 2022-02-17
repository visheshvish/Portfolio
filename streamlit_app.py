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
- Master's student of Computer Science specialized in Artificial Intelligence, Machine Learning, Computer Vision, Deep Learning and Software Development.
- Skilled in Python Programming, java, SQL, GIT, Docker, PYQT5, Computer Vision, Shell Scripting, MongoDB, AWS, Oracle Cloud (OCI), Flask, Django.
- Strong verbal and written communication skills, self directed learner & Self assertive.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Visheshkumar Vishwakarma</a>
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
        <a class="nav-link" href="#social-media">Social Media</a>
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

txt('**Master of Science - Computer Science** (M.Sc CS), S K Somiaya Degree College, *Somaiya Vidyavihar University*, Mumbai, Maharashtra, India',
    '2021-2023')
st.markdown('''
- GPA: `9.40` Sem 1
''')


txt('**Bachelor of Science - Computer Science** (B.Sc CS), NES Ratnam College of Arts Science And Commerce, *University Of Mumbai*, Maharashtra, India',
    '2018-2021')
st.markdown('''
- CGPA: `8.56`
- Graduated with First Class Honors.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Computer Vision Operation Engineer**, Detect Technologies PVT LTD, IIT Madras Research Park, Chennai, Tamilnadu, India.',
    'Nov 2021-present')
st.markdown('''
- Handeling and maintaining life cycle of AI Technologies and Linux Servers on AWS, and setting up the Intelligence Video Analytics (IVA) for Object Detection, Face Detection, Mask Detection, Intrusion Detection etc.
- Visiting client site within india to understand AI business requirement and suggesting them a better and effiecient solution to shape the future.
- Co-ordinating with multiple teams within organization to get the smooth workflow and helping them with solutions throughout the projects .
- Working on Python, linux, GIT, Docker, AWS, Shell Scripting, Computer Vision, OpenCV, Numpy, Pandas & many more.
- Currently learning app development using PYQT5/6 & improving existing skills.
''')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`,`Java`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`,`OpenCV`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`, `Django`')
txt3('Model deployment',
     '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')
txt3('Others', '`GIT`, `Docker`, `PYQT5`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/visheshv/')

txt2('GitHub', 'https://github.com/visheshvish')
