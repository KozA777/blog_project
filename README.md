# Blog Application

A Django-powered blog application that allows users to register, log in, and create, edit, and manage blog posts. It includes features like displaying latest posts on the homepage, a search functionality, and a personalized "My Articles" section for logged-in users.

## Features

- **User Registration & Authentication**: Users can sign up, log in, and log out.
- **Create & Edit Blog Posts**: Logged-in users can create new blog posts and edit their existing ones.
- **Latest Posts on Homepage**: Displays a list of the latest posts in reverse chronological order.
- **Search**: Users can search for posts by title or author.
- **My Articles**: A section for logged-in users to view, add, and delete their own articles.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-blog.git
   ```

2. Navigate to the project directory:
```bash
cd django-blog
```

3. Create a virtual environment:
```bash
python -m venv venv
```

4. Activate the virtual environment:
- On Windows:
  
```bash
venv\Scripts\activate
```

- On macOS/Linux:
```bash
source venv/bin/activate
```

5. Install dependencies:
```bash
pip install -r requirements.txt
```

6. Apply migrations:
```bash
python manage.py migrate
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```

9. Open your browser and go to:
```bash
http://127.0.0.1:8000
```

## Usage
- Register/Login: Create a new account or log in with existing credentials to start creating posts.
- Create Post: After logging in, navigate to the "My Articles" section and click "Add New Article" to create a new blog post.
- Edit/Delete Posts: In the "My Articles" section, you can view all your posts and have options to edit or delete them.
- Search: Use the search bar on the homepage to find articles by title or author.

## Customization
- Menu Buttons: The navigation menu has been customized to use buttons instead of hyperlinks.
- Layout: Elements such as the "My Articles" link are positioned below the "Logout" button for better accessibility. Buttons and elements are enlarged with more spacing, and a banner with a background and the text "Miejsce na Twoje myśli" has been added at the top of the page.

## Development
This project can be extended to include additional features such as:

- Categorizing articles by tags or topics.
- Adding comment functionality for users to interact with posts.
- Implementing an archive for old posts.
- Ability to print or download the article as a PDF
- Ability to add images to articles
- Complete redesign of the existing interface to improve the visual experience for the user 

## License
This project is licensed under the MIT License - see the LICENSE file for details.
