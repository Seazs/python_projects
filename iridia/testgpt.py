import cv2

# Fonction pour détecter les contours correspondant à une porte
def detect_door_contours(frame):
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Appliquer un flou gaussien pour réduire le bruit
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Détection des contours avec un seuil adaptatif
    edged = cv2.Canny(blurred, 50, 150)
    # Trouver les contours dans l'image
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filtre des contours pour ne garder que ceux qui correspondent à une porte
    door_contours = []
    for contour in contours:
        # Approximer le contour à un polygone
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
        # Filtrer les contours basés sur la forme ou la taille
        if len(approx) == 4:  # Une porte est généralement un quadrilatère
            door_contours.append(contour)
    
    return door_contours

# Fonction pour filtrer les contours en fonction de leur position
def filter_contours(contours, frame_width):
    filtered_contours = []
    for contour in contours:
        # Calculer le centre du contour
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            # Filtrer les contours qui sont proches du centre de l'image (axe X)
            if cX > frame_width * 0.4 and cX < frame_width * 0.6:  # Ajuster les valeurs selon l'emplacement de la porte dans l'image
                filtered_contours.append(contour)
    return filtered_contours

# Fonction pour détecter le passage de porte
def detect_door_passage(prev_contours, curr_contours):
    prev_contour_count = len(prev_contours)
    curr_contour_count = len(curr_contours)
    
    if curr_contour_count > prev_contour_count:
        return True
    else:
        return False

# Capturer la vidéo en direct
cap = cv2.VideoCapture(0)

# Initialiser les contours précédents
prev_contours = []

while True:
    # Capture d'une image
    ret, frame = cap.read()
    if not ret:
        break
    
    # Récupérer la largeur de l'image
    frame_width = frame.shape[1]
    
    # Détecter les contours de la porte
    door_contours = detect_door_contours(frame)
    
    # Filtrer les contours en fonction de leur position
    filtered_contours = filter_contours(door_contours, frame_width)
    
    # Dessiner les contours filtrés sur l'image originale
    cv2.drawContours(frame, filtered_contours, -1, (0, 255, 0), 2)
    
    # Détecter le passage de porte
    if prev_contours:
        passage_detected = detect_door_passage(prev_contours, filtered_contours)
        if passage_detected:
            print("Passage de porte détecté !")
    
    # Mettre à jour les contours précédents
    prev_contours = filtered_contours.copy()
    
    # Afficher l'image résultante
    cv2.imshow('Door Detection', frame)
    
    # Sortir de la boucle si la touche 'q' est enfoncée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()
