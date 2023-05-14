import cv2
from pyzbar.pyzbar import decode

# Open the first webcam attached to the computer
cap = cv2.VideoCapture(0)
cap.set(3,640) # set video width
cap.set(4,480) # set video height

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Use pyzbar to find and decode barcodes in the image
    decoded_objects = decode(frame)
    for obj in decoded_objects:
        # Draw the barcode bounding box on the image
        cv2.rectangle(frame, (obj.rect.left, obj.rect.top), 
                      (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height), 
                      (0, 255, 0), 2)
        
        # Print the barcode type and data to the console
        print("Type:", obj.type)
        print("Data:", obj.data.decode("utf-8"))  # Decoding byte object into string

        # Display the data on the image
        cv2.putText(frame, obj.data.decode("utf-8"), (obj.rect.left, obj.rect.top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # Wait for a key press and then exit the program
        cv2.waitKey(0)
        cap.release()
        cv2.destroyAllWindows()
        exit()
        
    # Display the resulting frame even if no barcode is detected
    cv2.imshow('frame', frame)
    
    # Exit if ESC key is pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
