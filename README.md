# Steps to run
- Create a virtual enviornment in your directory
- Clone this respository in that directory
- run `pip install -r requirements.txt` in terminal
- run `python -m streamlit run app.py` to run this app in your browser

# Working 
Trained Generator will produce a grid of Anime faces each time the generate button is clicked in App 

# Model Training on batches of images
Dataset was taken from [kaggle](https://www.kaggle.com/datasets/soumikrakshit/anime-faces) 

It contains 21551 Anime Face images which are of 64x64 in dimensions

These images are used to train two neural networks: Generator, Discriminator

Discriminator's job is tell if an image is real or fake

For each epoch, Discriminator is trained on batch of real images and fake images(generated ones) while generator learns to draw fake images which would approved as real by discriminator 

Finally the trained generator is used to generate faces

Hers's how the training process looked:
![evolution](https://github.com/user-attachments/assets/69de35db-2f19-489f-b504-1bf3af5e6154)
