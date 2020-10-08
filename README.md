# web-development
This a repository for my **web-development** projects. 
I am not very keen about the front-end, 
but I like working in the Django framework.

The idea for my current project comes from my final project for CS50x. 
At first, it was going to be a simple Django blogging application(minimum style, 
simple posts, simple comments). 
However, now it is more of a personal site with a nice blogging system.

* Some of the noticeable features of the **personal_site** project:
    * Three models in *blog/models.py*: post, comment, and category
    * Couple of forms in *blog/forms.py* for the user to leave comments, 
    make posts, and choose categories in the web interface (to make them more appealing,
    I used an extension, [crispy](https://github.com/django-crispy-forms/django-crispy-forms) 
    and to have a better text editor, I used [ckeditor](https://github.com/ckeditor/ckeditor5))
    * Bunch of views in *blog/views.py* that are responsible for connecting Back-End with Front-End.
    They basically feed dicts into *templates* where the data is then parsed. 
    Note that some of them are Django generic views, others are just function-based views
    * URLs for all of the views are in *blog/urls.py*. 
    Each view has a url mapping, including sitemaps
    * Sitemaps for posts (django.contrib.sitemaps).

**Sidenote**

Today's web applications have become so dynamic that they basically may push 
all software to the web rather than phone and computer applications.
Why installing software when you can just open a browser and have it? 
If things like AWS and Azure will keep pushing hardware access for low prices,
cloud computing will become universal, and this is where webdev is a key.

