# notes_api
Project for api in django


In this I have created following apis

● POST /register: Let visitors register into the system
    In this I have created django project named notetaking and inside this i have created app called notes, then added this app in installed apps for migrattion process
    run make migration and migrate models
    In  model.py added models and in serializer.py mapped those models for registation.
    created urls.py in notes app and mapped that urls.py file in main project's url.py
    In views.py I have added class UserRegistrationAPIView and in that function I have added post method for registation.

    
● POST /login: Let the user log in to the system using email and password
    In this api I have made class UserLoginAPIView in views.py and in that called UserLoginSerializer for login process

● POST /notes: Create a new note 
    In this In views.py -> NoteCreateAPIView I have called NoteSerializer for create notes
    
● GET /notes/{noteId}: Retrieve a specific note by its ID
    In this In views.py -> NoteRetrieveAPIView I have passed object in serializer class to retrive the data.

● PUT /notes/{noteId}: Update an existing note by its ID
     To edit notes In views.py -> NoteUpdateAPIView -> I have also passed object with Note model to update that object. 
      
● DELETE /notes/{noteId}: Delete a note by its ID
    In this to delete note I have created NoteDeleteAPIView in views.py with object to delete that note object in Note model


Please note that this assignment is new to me and couldn't complete the whole task within time limit I also wants to admit that I use internet resources and go though django documentation to complete this
  
