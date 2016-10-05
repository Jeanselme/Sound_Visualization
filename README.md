# Sound_Visualization
Computes a visualization of the Fourier Transformation of a wav file.

## Execution
```
python3.5 sound_visualisation.py FileName.wav [-f frequencyNumber > 0]
          [-s sampleNumber > 0] [-d heightOfResultInPixels > 0] [-o resultFileName]
```
This command divides the sound into sampleNumber samples and computes a fft for each sample.  
The script gathers the different frequencies (in frequencyNumber clusters) and creates an image in order to visualize the sound.  
Result is a frequencyNumber x heightOfResultInPixels height and sampleNumber x heightOfResultInPixels width image.  

By default :
  - frequencyNumber = 15
  - sampleNumber = 15
  - heightOfResultInPixels = 20
  - File is not saved except if you precise an output filename.

## Result
This is the computed result :  
![Result](https://raw.githubusercontent.com/Jeanselme/Sound_Visualization/master/images/result.png)


## Libraries
Needs my library color_mapping.
Needs numpy, scipy and sys. Executed with python3.5
