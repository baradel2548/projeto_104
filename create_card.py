import cv2

img = cv2.imread("C:/Users/barad/Downloads/python/PRO_1-1_C104_AtividadeDaProfessora3-main/solar-system.jpg")


text_to_show = "Sol"

cv2.putText(img,  
           text_to_show,
           (100,80),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "Mercurio",
           (130,180),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,0,255)
           )


cv2.imshow("resultado",img)
cv2.waitKey(0)
