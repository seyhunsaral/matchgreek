from setuptools import setup, find_packages 
  
with open('requirements.txt') as f: 
    requirements = f.readlines() 
  
long_description = """matchgreek is a tool to see which greek 
      letters you use in your TeX file."""
  
setup( 
        name ='matchgreek', 
        version ='0.1.1', 
        author ='Ali Seyhun Saral', 
        author_email ='saral@posteo.de',
        url ='https://github.com/seyhunsaral/matchgreek',
        description ='See which greek letters you used in your TeX file',
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='GNU GPL-3', 
        packages = find_packages(), 
        entry_points ={ 
            'console_scripts': [ 
                'matchgreek = matchgreek.matchgreek:main'
            ] 
        }, 
        classifiers =( 
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Operating System :: OS Independent", 
        ), 
        keywords ='Tex LaTeX greek letters', 
        install_requires = requirements, 
        zip_safe = False
) 
