# Visual Application for our Sales Prediction tool
It will help us interact easily with our model and easily try it.


# 1. Predict Sales

Check out the corresponding medium blog post [https://towardsdatascience.com/how-to-easily-deploy-machine-learning-models-using-flask-b95af8fe34d4](https://towardsdatascience.com/how-to-easily-deploy-machine-learning-models-using-flask-b95af8fe34d4).

## Environment and tools
1. scikit-learn
2. pandas
3. numpy
4. flask
5. werkzeug
6. pickle
7. time

## Usage

First start by installing the requirement :
`pip install scikit-learn pandas numpy flask werkzeug pickle time`

Then you should launch the app in a terminal.
`python app.py`

And finally, through the terminal you will get a


## File Structure

'''bash
.
├── Model
│   ├── Model_reg.py
│   ├── __pycache__
│   │   ├── Model_reg.cpython-36.pyc
│   │   └── extractor.cpython-36.pyc
│   ├── extractor.py
│   └── model_rf.pkl
├── Predictions
│   └── Predictions.csv
├── README.md
├── __pycache__
│   └── preprocess.cpython-36.pyc
├── app.py
├── data
│   ├── store.csv
│   ├── test.csv
│   ├── train.csv
│   └── validation.csv
├── encoder.pkl
├── model.py
├── preprocess.py
├── static
│   ├── chart
│   │   ├── Chart.bundle.js
│   │   ├── Chart.bundle.min.js
│   │   ├── Chart.css
│   │   ├── Chart.js
│   │   ├── Chart.min.css
│   │   └── Chart.min.js
│   ├── chart.js-2.9.3.tgz
│   ├── css
│   │   ├── landing-page.css
│   │   └── landing-page.min.css
│   ├── graph.js
│   ├── img
│   │   ├── alexis.jpeg
│   │   ├── bg-masthead\ copie.jpg
│   │   ├── bg-masthead.jpg
│   │   ├── bg-showcase-1.jpg
│   │   ├── bg-showcase-2.jpg
│   │   ├── bg-showcase-3.jpg
│   │   ├── clotilde.jpg
│   │   ├── d.jpg
│   │   ├── img_analytics_1.jpg
│   │   ├── img_analytics_2.jpg
│   │   ├── img_analytics_3.jpg
│   │   ├── manon.jpeg
│   │   ├── rym.jpeg
│   │   ├── sofiane.jpeg
│   │   ├── testimonials-1.jpg
│   │   ├── testimonials-2.jpg
│   │   └── testimonials-3.jpg
│   ├── package
│   │   ├── LICENSE.md
│   │   ├── README.md
│   │   ├── bower.json
│   │   ├── composer.json
│   │   ├── dist
│   │   │   ├── Chart.bundle.js
│   │   │   ├── Chart.bundle.min.js
│   │   │   ├── Chart.css
│   │   │   ├── Chart.js
│   │   │   ├── Chart.min.css
│   │   │   └── Chart.min.js
│   │   └── package.json
│   ├── scss
│   │   ├── _call-to-action.scss
│   │   ├── _footer.scss
│   │   ├── _global.scss
│   │   ├── _icons.scss
│   │   ├── _masthead.scss
│   │   ├── _mixins.scss
│   │   ├── _showcase.scss
│   │   ├── _testimonials.scss
│   │   ├── _variables.scss
│   │   └── landing-page.scss
│   └── vendor
│       ├── bootstrap
│       │   ├── css
│       │   │   ├── bootstrap-grid.css
│       │   │   ├── bootstrap-grid.css.map
│       │   │   ├── bootstrap-grid.min.css
│       │   │   ├── bootstrap-grid.min.css.map
│       │   │   ├── bootstrap-reboot.css
│       │   │   ├── bootstrap-reboot.css.map
│       │   │   ├── bootstrap-reboot.min.css
│       │   │   ├── bootstrap-reboot.min.css.map
│       │   │   ├── bootstrap.css
│       │   │   ├── bootstrap.css.map
│       │   │   ├── bootstrap.min.css
│       │   │   └── bootstrap.min.css.map
│       │   └── js
│       │       ├── bootstrap.bundle.js
│       │       ├── bootstrap.bundle.js.map
│       │       ├── bootstrap.bundle.min.js
│       │       ├── bootstrap.bundle.min.js.map
│       │       ├── bootstrap.js
│       │       ├── bootstrap.js.map
│       │       ├── bootstrap.min.js
│       │       └── bootstrap.min.js.map
│       ├── fontawesome-free
│       │   ├── css
│       │   │   ├── all.css
│       │   │   ├── all.min.css
│       │   │   ├── brands.css
│       │   │   ├── brands.min.css
│       │   │   ├── fontawesome.css
│       │   │   ├── fontawesome.min.css
│       │   │   ├── regular.css
│       │   │   ├── regular.min.css
│       │   │   ├── solid.css
│       │   │   ├── solid.min.css
│       │   │   ├── svg-with-js.css
│       │   │   ├── svg-with-js.min.css
│       │   │   ├── v4-shims.css
│       │   │   └── v4-shims.min.css
│       │   └── webfonts
│       │       ├── fa-brands-400.eot
│       │       ├── fa-brands-400.svg
│       │       ├── fa-brands-400.ttf
│       │       ├── fa-brands-400.woff
│       │       ├── fa-brands-400.woff2
│       │       ├── fa-regular-400.eot
│       │       ├── fa-regular-400.svg
│       │       ├── fa-regular-400.ttf
│       │       ├── fa-regular-400.woff
│       │       ├── fa-regular-400.woff2
│       │       ├── fa-solid-900.eot
│       │       ├── fa-solid-900.svg
│       │       ├── fa-solid-900.ttf
│       │       ├── fa-solid-900.woff
│       │       └── fa-solid-900.woff2
│       ├── jquery
│       │   ├── jquery.js
│       │   ├── jquery.min.js
│       │   ├── jquery.min.map
│       │   ├── jquery.slim.js
│       │   ├── jquery.slim.min.js
│       │   └── jquery.slim.min.map
│       └── simple-line-icons
│           ├── css
│           │   └── simple-line-icons.css
│           └── fonts
│               ├── Simple-Line-Icons.eot
│               ├── Simple-Line-Icons.svg
│               ├── Simple-Line-Icons.ttf
│               ├── Simple-Line-Icons.woff
│               └── Simple-Line-Icons.woff2
└── templates
    ├── file.html
    ├── index\ copie.html
    ├── index.html
    ├── index_2.html
    ├── pie_chart.html
    └── pred.html

24 directories, 131 files

'''
