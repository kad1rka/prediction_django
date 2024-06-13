from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import os



def upload_image(request): 
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        file_name = uploaded_file.name 
        products = predict(f"/static/images/{uploaded_file.name}")
        return render(request, 'upload_image.html', {'path' : f"/static/images/{uploaded_file.name}",                    
                                                    'image1' : products[0], 
                                                     'image2' : products[1],
                                                     'image3' : products[2],
                                                     'image4' : products[3],
                                                     'image5' : products[4]
                                                    } )
    return render(request, 'upload_image.html')

def predict(given_img):
    df = pd.read_csv("input.csv")
    nb_closest_images = 5
    products = []
    closest_imgs = df[given_img].sort_values(ascending=False)[1:nb_closest_images+1].index
    closest_imgs_scores = 100*df[given_img].sort_values(ascending=False)[1:nb_closest_images+1]
    for i in range(0, len(closest_imgs)):
        # products[df.columns[closest_imgs[i]]] = closest_imgs_scores[closest_imgs[i]]
        products.append(df.columns[closest_imgs[i]])
    return products

