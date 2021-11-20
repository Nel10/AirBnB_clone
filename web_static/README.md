<h1 class="gap" style="box-sizing: border-box; font-size: 36px; margin-top: 50px !important; margin-right: 0px; margin-bottom: 10px; margin-left: 0px; font-family: aktiv-grotesk, sans-serif; font-weight: 500; line-height: 1.1; color: rgb(51, 51, 51); font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">AirBnB clone - Web static</h1>
<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2021/9/135ef103cf7ed150c9760aadc66844113dfc3d35.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20211119%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211119T212351Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9b714dc0e9310b7a8ac40549631f17d1245ad5c939bc69ab33382fdac91d41cd" alt="" style="box-sizing: border-box; border: 0px; height: auto; max-width: 100%;"></p>
<h2 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 30px;">Background Context</h2>
<h3 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 24px;">Web static, what?</h3>
<p style="box-sizing: border-box; margin: 0px 0px 10px;">Now that you have a command interpreter for managing your AirBnB objects, it&rsquo;s time to make them alive!</p>
<p style="box-sizing: border-box; margin: 0px 0px 10px;">Before developing a big and complex web application, we will build the front end step-by-step.</p>
<p style="box-sizing: border-box; margin: 0px 0px 10px;">The first step is to &ldquo;design&rdquo; / &ldquo;sketch&rdquo; / &ldquo;prototype&rdquo; each element:</p>
<ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
    <li style="box-sizing: border-box;">Create simple HTML static pages</li>
    <li style="box-sizing: border-box;">Style guide</li>
    <li style="box-sizing: border-box;">Fake contents</li>
    <li style="box-sizing: border-box;">No Javascript</li>
    <li style="box-sizing: border-box;">No data loaded from anything</li>
    <li>During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can&rsquo;t apply any design.</li>
</ul>
<p style="box-sizing: border-box; margin: 0px 0px 10px;"></p>
<p style="box-sizing: border-box; margin: 0px 0px 10px;">Before starting, please fork or clone the repository <code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>AirBnB_clone</code> from your partner if you were not the owner of the previous project.</p>
<h2 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 30px;">Resources</h2>
<p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Read or watch</strong>:</p>
<ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
    <li style="box-sizing: border-box;"><a href="https://intranet.hbtn.io/rltoken/qq7qrSgdVRuD1kPd_jf7Fw" style="box-sizing: border-box; background-color: transparent; color: rgb(224, 0, 60); text-decoration: none;" target="_blank" title="Learn to Code HTML & CSS">Learn to Code HTML &amp; CSS</a> (<em style="box-sizing: border-box;">until &ldquo;Creating Lists&rdquo; included</em>)</li>
    <li style="box-sizing: border-box;"><a href="https://intranet.hbtn.io/rltoken/Hx5KFagrj9L-HtAZ8SHK1Q" style="box-sizing: border-box; background-color: transparent; color: rgb(224, 0, 60); text-decoration: none;" target="_blank" title="Inline Styles in HTML">Inline Styles in HTML</a></li>
    <li style="box-sizing: border-box;"><a href="https://intranet.hbtn.io/rltoken/sO3wz-QbhwYdKJqvokC4PA" style="box-sizing: border-box; background-color: transparent; color: rgb(224, 0, 60); text-decoration: none;" target="_blank" title="Specifics on CSS Specificity">Specifics on CSS Specificity</a></li>
    <li style="box-sizing: border-box;"><a href="https://intranet.hbtn.io/rltoken/NvqQf3dgY64bb-QWC5Cueg" style="box-sizing: border-box; background-color: transparent; color: rgb(224, 0, 60); text-decoration: none;" target="_blank" title="CSS SpeciFishity">CSS SpeciFishity</a></li>
    <li style="box-sizing: border-box;"><a href="https://intranet.hbtn.io/rltoken/STaxnOI5qv1enUuwIALelw" style="box-sizing: border-box; background-color: transparent; color: rgb(224, 0, 60); text-decoration: none;" target="_blank" title="Introduction to HTML">Introduction to HTML</a></li>
    <li style="box-sizing: border-box;"><a href="https://intranet.hbtn.io/rltoken/g-uj9Azx1rALX49xCZHK0w" style="box-sizing: border-box; background-color: transparent; color: rgb(224, 0, 60); text-decoration: none;" target="_blank" title="CSS">CSS</a></li>
    <li style="box-sizing: border-box;"><a href="https://intranet.hbtn.io/rltoken/El1BHRNNO2hPEcOt_XwF-Q" style="box-sizing: border-box; background-color: transparent; color: rgb(224, 0, 60); text-decoration: none;" target="_blank" title="MDN">MDN</a></li>
    <li style="box-sizing: border-box;"><a href="https://intranet.hbtn.io/rltoken/HI0qRNDq20cgICIhO18kUQ" style="box-sizing: border-box; background-color: transparent; color: rgb(224, 0, 60); text-decoration: none;" target="_blank" title="center boxes">center boxes</a></li>
    <li>Learning Objectives</li>
</ul>
<h2 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 30px;"></h2>
<p style="box-sizing: border-box; margin: 0px 0px 10px;">At the end of this project, you are expected to be able to <a href="https://intranet.hbtn.io/rltoken/O8BWXDOfoda19l0QdcprUg" style="box-sizing: border-box; background-color: transparent; color: rgb(224, 0, 60); text-decoration: none;" target="_blank" title="explain to anyone">explain to anyone</a>, <strong style="box-sizing: border-box; font-weight: bold;">without the help of Google</strong>:</p>
<h3 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 24px;">General</h3>
<ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
    <li style="box-sizing: border-box;">What is HTML</li>
    <li style="box-sizing: border-box;">How to create an HTML page</li>
    <li style="box-sizing: border-box;">What is a markup language</li>
    <li style="box-sizing: border-box;">What is the DOM</li>
    <li style="box-sizing: border-box;">What is an element / tag</li>
    <li style="box-sizing: border-box;">What is an attribute</li>
    <li style="box-sizing: border-box;">How does the browser load a webpage</li>
    <li style="box-sizing: border-box;">What is CSS</li>
    <li style="box-sizing: border-box;">How to add style to an element</li>
    <li style="box-sizing: border-box;">What is a class</li>
    <li style="box-sizing: border-box;">What is a selector</li>
    <li style="box-sizing: border-box;">How to compute CSS Specificity Value</li>
    <li style="box-sizing: border-box;">What are Box properties in CSS</li>
    <li>Requirements</li>
</ul>
<h2 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 30px;"></h2>
<h3 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 24px;">General</h3>
<ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
    <li style="box-sizing: border-box;">Allowed editors: <code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>vi</code>, <code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>vim</code>, <code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>emacs</code></li>
    <li style="box-sizing: border-box;">All your files should end with a new line</li>
    <li style="box-sizing: border-box;">A <code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>README.md</code> file, at the root of the folder of the project, is mandatory</li>
    <li style="box-sizing: border-box;">Your code should be W3C compliant and validate with <a href="https://intranet.hbtn.io/rltoken/4dtXqWSyIeSCFVqQ9Eo6NA" style="box-sizing: border-box; background-color: transparent; color: rgb(224, 0, 60); text-decoration: none;" target="_blank" title="W3C-Validator">W3C-Validator</a></li>
    <li style="box-sizing: border-box;">All your CSS files should be in <code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>styles</code> folder</li>
    <li style="box-sizing: border-box;">All your images should be in <code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>images</code> folder</li>
    <li style="box-sizing: border-box;">You are not allowed to use <code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>!important</code> and <code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>id</code> (<code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>#...</code> in the CSS file)</li>
    <li style="box-sizing: border-box;">You are not allowed to use tags <code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>img</code>, <code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>embed</code> and <code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>iframe</code></li>
    <li style="box-sizing: border-box;">You are not allowed to use Javascript</li>
    <li style="box-sizing: border-box;">Current screenshots have been done on <code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>Chrome 56</code> or more.</li>
    <li style="box-sizing: border-box;">No cross browsers</li>
    <li style="box-sizing: border-box;">You have to follow all requirements but some <code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>margin</code>/<code style='box-sizing: border-box; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;'>padding</code> are missing - you should try to fit as much as you can to screenshots</li>
</ul>

<img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step1.png"> 
