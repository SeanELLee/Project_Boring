import random
import time
import cv2

class cFunctions():
    def __init__(self) -> None:
        pass

    def generate_random_number(self, input_1, input_2):
        number = random.randint(input_1, input_2)
        return number
    
    def read_image_from_disk(self, input_img):
        image = cv2.imread(input_img)
        return image
        
    pass

if __name__ == '__main__':
    print('💩' * 721)
    oFunctions = cFunctions()
    start_time = time.time()

    input_1 = 0                             #Enter lower boundary for the number
    input_2 = 255                           #Enter upper boundary for the number

    while True:
        number_1 = oFunctions.generate_random_number(input_1, input_2)
        number_2 = oFunctions.generate_random_number(input_1, input_2)
        if number_1 == number_2:
            print('matched = ' + str(number_1))
            break
    end_time = time.time()
    time_elapsed = end_time - start_time
    print('time elapsed = ' + str(time_elapsed))
    pass