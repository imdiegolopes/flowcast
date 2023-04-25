# Use Case: Adding a new video to the system

## Primary Actor

Content Creator

## Pre-Conditions

    The Content Creator is authenticated and authorized to add a new video to the system.
    The Content Creator has access to the video file to be uploaded.

## Steps

    The Content Creator opens the video upload form in the system.
    The Content Creator fills out the form, including the title, description, URL, duration, thumbnail URL, and publishing date.
    The system creates a new Video object with the provided information.
    The system calls the validate() method on the Video object to ensure that all required fields are present and that the URLs are valid.
    If the validate() method raises a ValueError exception, the system displays an error message to the Content Creator and does not save the video.
    If the validate() method succeeds, the system saves the video object to the database.
    The Content Creator receives a confirmation message that the video has been added to the system.

## Post-Conditions

    The new video is added to the system and is available for viewing by users with the appropriate permissions.
