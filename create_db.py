from ChatbotWebsite import db, create_app
from ChatbotWebsite.models import User  

app = create_app()
app.app_context().push()
db.create_all()