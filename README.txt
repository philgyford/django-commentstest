An example of an as-simple-as-possible weblog with custom comments.

The site's comments are an extended version of the standard 
django.contrib.comments framework.

You can add an Entry in the Admin screens, go to the front page of the 
public site, and you'll see the Entry. Click through to see the Entry 
page with a comment form.


If you set the "Enable comments" setting for an Entry, then submitting 
a comment will work or fail appropriately.

BUT, if you add the line "from weblog.models import Entry" to either 
customcomments/forms.py or customcomments/models.py then comment 
submissions will ALWAYS succeed, no matter what the "Enable comments" 
setting is. 

Why is this...?
