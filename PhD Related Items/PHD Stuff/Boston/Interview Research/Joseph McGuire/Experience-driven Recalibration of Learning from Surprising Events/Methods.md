### Participants

Experiment 1:
	Consisted of BU community
	N = 29, 18 Female, 11 Male
	Age: Mean = 20.5, range = 18-24
Experiment 2
	Consisted of BU community
	N = 63, 48 Female, 15 Male
	Age: Mean = 20.3, range = 18-31
Normal or corrected-to-normal vision

### Task

In two experiments, participants performed an implicit spatial prediction task based on (Another paper)programmed in Python using PsychoPy while their eye movements were tracked. Gaze position was collected monocularly at 1000 Hz. Head position was stabilized using a chin rest positioned 57 cm from the display, and the eye tracker was calibrated at the beginning of each run.

>[!note] IMPORTANT INFORMATION!!!!
>An additional post-hoc calibration was performed following data collection. The nominal task was to report whether briefly presented numerical digits were even or odd in order to earn reward. The digits were presented in varying locations, implicitly requiring participants to anticipate the location of the next digit so that they could use central vision to make the odd/even judgement.
>Each digit appeared between two flanking Xs for 180 ms before being backward-masked by another X. The participant then had unlimited time to respond by pressing "1" with their left hand for "odd" or "0" with their right hand for "even". Accuracy feed back was then displayed in the same location as a digit for 500 ms, followed by a 750-ms inter-trial interval. Thus, there was a fixed 1250 ms interval between the keypress and appearance of the next digit, making targets temporally predictable.

Two types of trials occurred:
1) <mark style="background: #FF5582A6;">Central trials</mark> displayed the digit at the center of the screen, which was marked by a small white point throughout the task.
2) <mark style="background: #FF5582A6;">Peripheral trials</mark> displayed the digit somewhere on the perimeter of a circle centered on the screen with a radius of 6.9 degrees of visual angle, which was marked throughout the task with a white outline.

Two conditions: Change point (CP) and Random Walk (RW) governed the peripheral digit locations. Average spatial predictability was similar between the two conditions but the sequential contingencies differed. In the CP condition, each digit's location was drawn from a Gaussian distribution with a fixed width(sig = 11.25 degrees in angular distance around the circle) and a meant that usually remained fixed from one peripheral trial to the next but was resampled from a uniform dist spanning the entire circle as occasional unsignaled change points.
